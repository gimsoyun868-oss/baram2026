# BARAM 2026 - 풍력발전량 예측 AI 경진대회

기상예보 데이터(LDAPS, GFS)와 SCADA 실측 데이터를 활용해 3개 KPX 그룹의
시간 단위 풍력발전량을 예측하는 프로젝트 뼈대입니다.

## 1. 폴더 구조

```
baram2026/
├── data/
│   ├── raw/                  # 원본 데이터 (git 추적 제외, 대회 제공 파일 그대로)
│   │   ├── train/
│   │   │   ├── ldaps_train.csv
│   │   │   ├── gfs_train.csv
│   │   │   ├── train_labels.csv
│   │   │   ├── scada_vestas_train.csv
│   │   │   └── scada_unison_train.csv
│   │   ├── test/
│   │   │   ├── ldaps_test.csv
│   │   │   └── gfs_test.csv
│   │   ├── sample_submission.csv
│   │   ├── info.xlsx
│   │   └── data_description.md
│   └── processed/            # 전처리/피처 캐시 저장용 (직접 생성)
├── notebooks/                 # EDA, 실험용 노트북
├── src/                        # 실제 파이프라인 코드
│   ├── config.py               # 경로/상수 (설비용량, 기간 등)
│   ├── data_loader.py           # 원본 CSV/XLSX 로딩
│   ├── features.py              # 피처 엔지니어링 (뼈대, TODO 포함)
│   ├── metrics.py                # NMAE / FICR 평가지표 (FICR은 TODO)
│   ├── train.py                  # 학습 스크립트 (LightGBM 예시)
│   ├── predict.py                # 예측 및 제출 파일 생성 스크립트
│   └── utils.py                  # 시드 고정, 로거
├── outputs/
│   ├── models/                    # 학습된 모델 저장
│   └── submissions/               # 생성된 제출 CSV
├── requirements.txt
├── .gitignore
└── README.md
```

## 2. 환경 설정 (VSCode 기준)

```bash
cd baram2026
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

VSCode에서 폴더를 열고, 우측 하단 또는 Command Palette
(`Python: Select Interpreter`)에서 방금 만든 `.venv`를 선택하세요.

## 3. 실행 순서 (뼈대 기준)

1. `notebooks/`에서 EDA 진행 (grid 위치, 결측 구간, 발전량-풍속 관계 등 확인)
2. `src/features.py`의 `build_feature_table()` 구현
   - LDAPS/GFS 격자 pivot 또는 집계
   - u/v 성분 → 풍속/풍향 변환 (`add_wind_speed_dir`)
   - SCADA 10분 → 시간 단위 집계 (`resample_scada_hourly`, 보조 피처용)
   - 시간 피처 추가 (`add_time_features`)
3. 프로젝트 루트에서 학습 실행
   ```bash
   python -m src.train
   ```
4. 예측 및 제출 파일 생성
   ```bash
   python -m src.predict
   ```
   → `outputs/submissions/submission_YYYYMMDD_HHMMSS.csv` 생성

## 4. 주의사항 (data_description.md 기준 요약)

- 모든 시간은 KST, `YYYY-MM-DD HH:MM:SS` 형식이며 CSV는 `utf-8-sig` 인코딩.
- 기상 예보는 매일 09:00 KST에 초기화되며, 각 예보는 해당일 **13:00 KST부터
  사용 가능**(`data_available_kst_dtm`)한 것으로 간주 — 실시간 운영을
  가정한 피처 생성 시 이 시차를 반드시 고려해야 함 (미래 정보 누출 방지).
- `kpx_group_3`은 2022년 라벨이 없음 (2023년부터 제공) → 학습 데이터
  구성 시 그룹별로 분리 처리 필요.
- 평가 기간의 실제 발전량/SCADA/비공개 운영자료/재분석자료는 예측에 사용 불가.
- 제출 파일은 반드시 코드로 생성 (Excel로 열고 저장하면 시간 포맷이 깨질 수 있음).
- `forecast_id`, `forecast_kst_dtm`은 절대 변경 금지.

## 5. 미확정/확인 필요 사항

- **FICR(정산금획득률) 계산식**: `data_description.md`에는 정확한 산식이
  없어 `src/metrics.py`의 `ficr()`는 `NotImplementedError` 상태입니다.
  대회 공지/규정 페이지에서 확인 후 구현하세요.
- SCADA `power_kw10m` 컬럼의 정확한 정의(순간값 vs 10분 평균값)는
  원본 데이터 소스 문서를 통해 재확인 권장 (현재 `resample_scada_hourly`는
  10분 평균 출력으로 가정).
