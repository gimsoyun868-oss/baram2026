"""
데이터 로딩 모듈

각 원본 CSV를 읽고, 이후 피처 엔지니어링에서 다루기 쉬운 형태로
1차 가공(타입 변환, wide-format 변환 등)까지만 수행합니다.
실제 피처 생성(풍속 계산, 그룹 집계 등)은 features.py에서 처리합니다.
"""

from __future__ import annotations

import pandas as pd

from . import config


def load_train_labels() -> pd.DataFrame:
    """train_labels.csv 로드. kst_dtm을 datetime으로 변환."""
    df = pd.read_csv(config.TRAIN_LABELS_PATH, encoding=config.CSV_ENCODING)
    df["kst_dtm"] = pd.to_datetime(df["kst_dtm"])
    return df


def _load_forecast_raw(path) -> pd.DataFrame:
    """LDAPS/GFS 공통 로딩: datetime 컬럼 변환."""
    df = pd.read_csv(path, encoding=config.CSV_ENCODING)
    df["forecast_kst_dtm"] = pd.to_datetime(df["forecast_kst_dtm"])
    df["data_available_kst_dtm"] = pd.to_datetime(df["data_available_kst_dtm"])
    return df


def load_ldaps_train() -> pd.DataFrame:
    return _load_forecast_raw(config.LDAPS_TRAIN_PATH)


def load_ldaps_test() -> pd.DataFrame:
    return _load_forecast_raw(config.LDAPS_TEST_PATH)


def load_gfs_train() -> pd.DataFrame:
    return _load_forecast_raw(config.GFS_TRAIN_PATH)


def load_gfs_test() -> pd.DataFrame:
    return _load_forecast_raw(config.GFS_TEST_PATH)


def load_scada_vestas_train() -> pd.DataFrame:
    df = pd.read_csv(config.SCADA_VESTAS_TRAIN_PATH, encoding=config.CSV_ENCODING)
    df["kst_dtm"] = pd.to_datetime(df["kst_dtm"])
    return df


def load_scada_unison_train() -> pd.DataFrame:
    df = pd.read_csv(config.SCADA_UNISON_TRAIN_PATH, encoding=config.CSV_ENCODING)
    df["kst_dtm"] = pd.to_datetime(df["kst_dtm"])
    return df


def load_sample_submission() -> pd.DataFrame:
    df = pd.read_csv(config.SAMPLE_SUBMISSION_PATH, encoding=config.CSV_ENCODING)
    df["forecast_kst_dtm"] = pd.to_datetime(df["forecast_kst_dtm"])
    return df


def load_info() -> pd.DataFrame:
    """info.xlsx의 info 시트 로드 (헤더가 4번째 행부터 시작)."""
    df = pd.read_excel(config.INFO_XLSX_PATH, sheet_name="info", header=3)
    # 완전 빈 행/열 제거
    df = df.dropna(how="all").dropna(axis=1, how="all")
    return df


if __name__ == "__main__":
    # 간단한 동작 확인용
    labels = load_train_labels()
    print("train_labels:", labels.shape, labels["kst_dtm"].min(), "~", labels["kst_dtm"].max())

    ldaps = load_ldaps_train()
    print("ldaps_train:", ldaps.shape, "grid_id unique:", ldaps["grid_id"].nunique())

    gfs = load_gfs_train()
    print("gfs_train:", gfs.shape, "grid_id unique:", gfs["grid_id"].nunique())

    info = load_info()
    print("info:", info.shape)
    print(info.head())
