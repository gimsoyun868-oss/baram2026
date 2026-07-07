"""
피처 엔지니어링 모듈

- LDAPS/GFS: grid_id별로 long-format인 데이터를 wide-format으로 변환하고,
  격자 간 평균/최대/최소 등 집계 피처를 생성합니다.
  u/v 성분 바람으로부터 풍속(speed)과 풍향(direction)도 계산합니다.
- SCADA: 10분 단위 발전량(kW10m)을 시간 단위로 집계합니다.
  주의: kW10m은 10분 구간 평균 출력으로 가정. 시간 발전량(kWh) 근사값은
  각 10분 구간 에너지(kWh) = power_kW * (10/60) 의 합으로 계산합니다.
  실제 컨벤션은 원본 SCADA 정의를 다시 확인해야 합니다.

TODO: 아래 함수들은 뼈대만 잡아둔 상태입니다. 실제 대회 데이터 특성에
맞춰 집계 방식, 결측 처리, 시차(lag) 피처 등을 채워 넣어야 합니다.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def add_wind_speed_dir(df: pd.DataFrame, u_col: str, v_col: str, prefix: str) -> pd.DataFrame:
    """u, v 성분으로부터 풍속과 기상학적 풍향(도)을 계산해 컬럼 추가."""
    df = df.copy()
    u = df[u_col]
    v = df[v_col]
    df[f"{prefix}_speed"] = np.sqrt(u**2 + v**2)
    # 기상학적 풍향(바람이 불어오는 방향, 0=북, 시계방향)
    df[f"{prefix}_dir"] = (np.degrees(np.arctan2(-u, -v))) % 360
    return df


def pivot_forecast_wide(df: pd.DataFrame, value_cols: list[str]) -> pd.DataFrame:
    """
    LDAPS/GFS long-format(격자별 행) 데이터를 forecast_kst_dtm 기준
    wide-format으로 변환. 컬럼명은 f"{col}_grid{grid_id}" 형태.

    격자가 많을 경우(LDAPS 16개) 피처 수가 급증하므로, 필요시
    grid_agg_features()의 집계 피처와 병행 사용을 권장합니다.
    """
    wide = df.pivot(index="forecast_kst_dtm", columns="grid_id", values=value_cols)
    wide.columns = [f"{col}_grid{grid}" for col, grid in wide.columns]
    return wide.reset_index()


def grid_agg_features(df: pd.DataFrame, value_cols: list[str]) -> pd.DataFrame:
    """forecast_kst_dtm 기준 격자 간 평균/표준편차/최댓값/최솟값 집계."""
    agg = df.groupby("forecast_kst_dtm")[value_cols].agg(["mean", "std", "max", "min"])
    agg.columns = [f"{col}_{stat}" for col, stat in agg.columns]
    return agg.reset_index()


def resample_scada_hourly(df: pd.DataFrame, power_cols: list[str]) -> pd.DataFrame:
    """
    10분 단위 SCADA power(kW10m) 컬럼들을 시간 단위 발전량(kWh)으로 집계.
    kst_dtm은 각 10분 구간의 시각. 시간 라벨(kst_dtm, 정시)은
    train_labels.csv의 종료 시각 컨벤션에 맞춰 이후 정렬 필요.
    """
    df = df.copy().set_index("kst_dtm").sort_index()
    energy_kwh = df[power_cols] * (10 / 60)
    hourly = energy_kwh.resample("1h", label="right", closed="right").sum()
    hourly.columns = [f"{c}_kwh_1h" for c in hourly.columns]
    return hourly.reset_index()


def add_time_features(df: pd.DataFrame, dt_col: str) -> pd.DataFrame:
    """시간 관련 파생 피처 (월, 시간, 요일, 사인/코사인 인코딩 등)."""
    df = df.copy()
    dt = df[dt_col]
    df["month"] = dt.dt.month
    df["hour"] = dt.dt.hour
    df["dayofyear"] = dt.dt.dayofyear
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    df["doy_sin"] = np.sin(2 * np.pi * df["dayofyear"] / 365)
    df["doy_cos"] = np.cos(2 * np.pi * df["dayofyear"] / 365)
    return df


def build_feature_table(
    labels: pd.DataFrame,
    ldaps: pd.DataFrame,
    gfs: pd.DataFrame,
    is_train: bool = True,
) -> pd.DataFrame:
    """
    최종 학습/예측용 피처 테이블 생성 뼈대.

    TODO:
    - ldaps, gfs 각각 pivot_forecast_wide 또는 grid_agg_features 적용
    - 두 소스를 forecast_kst_dtm 기준 merge
    - add_time_features 적용
    - is_train=True면 labels와 merge하여 학습셋 구성
    """
    raise NotImplementedError("피처 테이블 생성 로직을 채워 넣으세요.")
