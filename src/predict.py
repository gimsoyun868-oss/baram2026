"""
예측 및 제출 파일 생성 스크립트 뼈대

python -m src.predict 로 실행 (프로젝트 루트에서).

주의:
- 평가 기간의 실제 발전량/SCADA/비공개 자료는 사용 불가 (data_description.md 12장)
- forecast_id, forecast_kst_dtm은 절대 변경하지 말 것
- 제출 파일은 코드로 생성 (Excel에서 열고 저장 금지)
"""

from __future__ import annotations

from datetime import datetime

import lightgbm as lgb
import pandas as pd

from . import config, data_loader, features, utils

logger = utils.get_logger(__name__)


def load_models() -> dict[str, lgb.Booster]:
    models = {}
    for col in config.TARGET_COLS:
        path = config.MODEL_DIR / f"model_{col}.txt"
        models[col] = lgb.Booster(model_file=str(path))
    return models


def main() -> None:
    logger.info("테스트 원본 데이터 로딩 중...")
    ldaps_test = data_loader.load_ldaps_test()
    gfs_test = data_loader.load_gfs_test()
    submission = data_loader.load_sample_submission()

    logger.info("피처 테이블 생성 중...")
    feature_df = features.build_feature_table(
        labels=None, ldaps=ldaps_test, gfs=gfs_test, is_train=False
    )

    models = load_models()
    feature_cols = [
        c for c in feature_df.columns if c not in ["forecast_kst_dtm", "kst_dtm"]
    ]

    pred_df = feature_df[["forecast_kst_dtm"]].copy()
    for col, model in models.items():
        pred_df[col] = model.predict(feature_df[feature_cols])
        # 음수 발전량 방지, 설비용량 초과 방지 클리핑
        pred_df[col] = pred_df[col].clip(lower=0, upper=config.CAPACITY_KWH_1H[col])

    result = submission[["forecast_id", "forecast_kst_dtm"]].merge(
        pred_df, on="forecast_kst_dtm", how="left"
    )
    result = result[["forecast_id", "forecast_kst_dtm", *config.TARGET_COLS]]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = config.SUBMISSION_DIR / f"submission_{timestamp}.csv"
    result.to_csv(out_path, index=False, encoding=config.CSV_ENCODING)
    logger.info(f"제출 파일 저장: {out_path}")


if __name__ == "__main__":
    main()
