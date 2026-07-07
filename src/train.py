"""
학습 스크립트 뼈대

python -m src.train 로 실행 (프로젝트 루트에서).

TODO:
1. data_loader로 원본 로드
2. features.build_feature_table 구현 후 호출
3. 그룹별(kpx_group_1/2/3) 모델 학습
   - kpx_group_3는 2023년부터 라벨 존재 -> 학습 구간 분리 필요
4. 시계열이므로 랜덤 K-Fold보다 시간 기준 분할(TimeSeriesSplit 또는
   holdout) 권장
5. 학습된 모델을 outputs/models/에 저장
"""

from __future__ import annotations

import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit

from . import config, data_loader, features, utils

logger = utils.get_logger(__name__)


def load_all_raw():
    labels = data_loader.load_train_labels()
    ldaps = data_loader.load_ldaps_train()
    gfs = data_loader.load_gfs_train()
    return labels, ldaps, gfs


def train_one_group(
    feature_df: pd.DataFrame, target_col: str, feature_cols: list[str]
) -> lgb.LGBMRegressor:
    """단일 KPX 그룹에 대한 LightGBM 회귀 모델 학습 (시간순 홀드아웃)."""
    df = feature_df.dropna(subset=[target_col]).sort_values("forecast_kst_dtm")
    X = df[feature_cols]
    y = df[target_col]

    tscv = TimeSeriesSplit(n_splits=5)
    model = lgb.LGBMRegressor(
        n_estimators=1000,
        learning_rate=0.03,
        random_state=config.SEED,
    )

    for fold, (train_idx, valid_idx) in enumerate(tscv.split(X)):
        X_train, X_valid = X.iloc[train_idx], X.iloc[valid_idx]
        y_train, y_valid = y.iloc[train_idx], y.iloc[valid_idx]
        model.fit(
            X_train,
            y_train,
            eval_set=[(X_valid, y_valid)],
            callbacks=[lgb.early_stopping(50, verbose=False)],
        )
        logger.info(f"[{target_col}] fold {fold} best_iteration={model.best_iteration_}")

    return model


def main() -> None:
    utils.set_seed(config.SEED)
    logger.info("원본 데이터 로딩 중...")
    labels, ldaps, gfs = load_all_raw()

    logger.info("피처 테이블 생성 중...")
    feature_df = features.build_feature_table(labels, ldaps, gfs, is_train=True)

    feature_cols = [
        c
        for c in feature_df.columns
        if c not in ["forecast_kst_dtm", "kst_dtm", *config.TARGET_COLS]
    ]

    for target_col in config.TARGET_COLS:
        logger.info(f"=== {target_col} 학습 시작 ===")
        model = train_one_group(feature_df, target_col, feature_cols)
        model_path = config.MODEL_DIR / f"model_{target_col}.txt"
        model.booster_.save_model(str(model_path))
        logger.info(f"모델 저장: {model_path}")


if __name__ == "__main__":
    main()
