"""
평가지표 모듈

대회 설명(주최측 공지)에 따르면 1차 리더보드 평가는
- 평균 예측오차율 (1 - NMAE)
- 정산금획득률 (FICR)
두 가지를 기반으로 합니다.

data_description.md에는 NMAE/FICR의 정확한 계산식이 명시되어 있지
않으므로, 아래 nmae()는 일반적인 정의(설비용량 대비 정규화 MAE)로
우선 구현해 두었습니다. 대회 규정 페이지에서 정확한 산식(오차 허용
구간, 정산금 요율 등)을 확인한 뒤 ficr()을 채워야 합니다.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from . import config


def nmae(y_true: pd.Series, y_pred: pd.Series, capacity_kwh: float) -> float:
    """
    설비용량 대비 정규화 MAE.
    NMAE = mean(|y_true - y_pred|) / capacity_kwh
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return np.mean(np.abs(y_true - y_pred)) / capacity_kwh


def evaluate_all_groups(df_true: pd.DataFrame, df_pred: pd.DataFrame) -> dict:
    """
    df_true, df_pred: kst_dtm/forecast_kst_dtm + kpx_group_1/2/3 컬럼을 가진 DF.
    그룹별 NMAE와 (1 - NMAE) 평균을 반환.
    """
    results = {}
    for col in config.TARGET_COLS:
        cap = config.CAPACITY_KWH_1H[col]
        mask = df_true[col].notna()
        score = nmae(df_true.loc[mask, col], df_pred.loc[mask, col], cap)
        results[col] = {"nmae": score, "one_minus_nmae": 1 - score}
    results["mean_one_minus_nmae"] = np.mean(
        [v["one_minus_nmae"] for v in results.values() if isinstance(v, dict)]
    )
    return results


def ficr(y_true: pd.Series, y_pred: pd.Series, capacity_kwh: float) -> float:
    """
    정산금획득률(FICR) placeholder.

    TODO: 재생에너지 발전량 예측제도의 오차율 구간별 정산금 요율표를
    확인한 뒤 실제 산식으로 교체하세요. 현재는 구현되어 있지 않습니다.
    """
    raise NotImplementedError("FICR 산식을 대회 규정 확인 후 구현하세요.")
