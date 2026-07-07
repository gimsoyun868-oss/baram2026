"""
BARAM 2026 - 풍력발전량 예측 AI 경진대회
공통 설정 (경로, 상수) 모듈

프로젝트 루트 기준 상대경로로 모든 경로를 정의합니다.
다른 모듈에서는 절대 하드코딩하지 말고 이 모듈을 통해 경로를 가져오세요.
"""

from pathlib import Path

# ------------------------------------------------------------------
# 경로
# ------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
TRAIN_DIR = RAW_DIR / "train"
TEST_DIR = RAW_DIR / "test"
PROCESSED_DIR = DATA_DIR / "processed"

OUTPUT_DIR = ROOT_DIR / "outputs"
MODEL_DIR = OUTPUT_DIR / "models"
SUBMISSION_DIR = OUTPUT_DIR / "submissions"

# 원본 파일
LDAPS_TRAIN_PATH = TRAIN_DIR / "ldaps_train.csv"
GFS_TRAIN_PATH = TRAIN_DIR / "gfs_train.csv"
TRAIN_LABELS_PATH = TRAIN_DIR / "train_labels.csv"
SCADA_VESTAS_TRAIN_PATH = TRAIN_DIR / "scada_vestas_train.csv"
SCADA_UNISON_TRAIN_PATH = TRAIN_DIR / "scada_unison_train.csv"

LDAPS_TEST_PATH = TEST_DIR / "ldaps_test.csv"
GFS_TEST_PATH = TEST_DIR / "gfs_test.csv"

SAMPLE_SUBMISSION_PATH = RAW_DIR / "sample_submission.csv"
INFO_XLSX_PATH = RAW_DIR / "info.xlsx"

# CSV 인코딩: 명세서에 따라 모든 CSV는 BOM 포함 UTF-8
CSV_ENCODING = "utf-8-sig"

# ------------------------------------------------------------------
# 예측 대상 (KPX 그룹)
# ------------------------------------------------------------------
TARGET_COLS = ["kpx_group_1", "kpx_group_2", "kpx_group_3"]

# 설비용량 (MW) 및 1시간 기준 kWh 환산값
CAPACITY_MW = {
    "kpx_group_1": 21.6,
    "kpx_group_2": 21.6,
    "kpx_group_3": 21.0,
}
CAPACITY_KWH_1H = {k: v * 1000 for k, v in CAPACITY_MW.items()}

# kpx_group_3은 2023년부터 라벨이 존재 (2022년 구간은 결측)
LABEL_START_YEAR = {
    "kpx_group_1": 2022,
    "kpx_group_2": 2022,
    "kpx_group_3": 2023,
}

# ------------------------------------------------------------------
# 기간
# ------------------------------------------------------------------
TRAIN_START = "2022-01-01 01:00:00"
TRAIN_END = "2025-01-01 00:00:00"
TEST_START = "2025-01-01 01:00:00"
TEST_END = "2026-01-01 00:00:00"

# ------------------------------------------------------------------
# 랜덤 시드
# ------------------------------------------------------------------
SEED = 42
