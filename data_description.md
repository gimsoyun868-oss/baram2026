# 풍력발전량 예측 AI 공모전 Data Understanding Report

> 범위: 데이터 구조/품질/탐색 리포트입니다. 모델링, 학습, 하이퍼파라미터 튜닝 코드는 포함하지 않았습니다.

## STEP 1

### 프로젝트 구조

| Section | Path | Extension | Size |
| --- | --- | --- | --- |
| metadata | data_description.md | .md | 11.42 KB |
| metadata | info.xlsx | .xlsx | 3.65 MB |
| sample_submission | sample_submission.csv | .csv | 350.81 KB |
| test | test/gfs_test.csv | .csv | 26.74 MB |
| test | test/ldaps_test.csv | .csv | 41.12 MB |
| train | train/gfs_train.csv | .csv | 80.41 MB |
| train | train/ldaps_train.csv | .csv | 123.68 MB |
| train | train/scada_unison_train.csv | .csv | 16.01 MB |
| train | train/scada_vestas_train.csv | .csv | 31.91 MB |
| train | train/train_labels.csv | .csv | 1.09 MB |

```text
metadata/ data_description.md (11.42 KB)
metadata/ info.xlsx (3.65 MB)
sample_submission/ sample_submission.csv (350.81 KB)
test/ test/gfs_test.csv (26.74 MB)
test/ test/ldaps_test.csv (41.12 MB)
train/ train/gfs_train.csv (80.41 MB)
train/ train/ldaps_train.csv (123.68 MB)
train/ train/scada_unison_train.csv (16.01 MB)
train/ train/scada_vestas_train.csv (31.91 MB)
train/ train/train_labels.csv (1.09 MB)
```

## STEP 2

### 모든 CSV 로드 요약

| Dataset | Rows | Columns | Shape | Memory | Column Names |
| --- | --- | --- | --- | --- | --- |
| sample_submission.csv | 8,760 | 5 | (8760, 5) | 1.29 MB | forecast_id, forecast_kst_dtm, kpx_group_1, kpx_group_2, kpx_group_3 |
| test/gfs_test.csv | 78,840 | 40 | (78840, 40) | 33.08 MB | forecast_kst_dtm, data_available_kst_dtm, grid_id, latitude, longitude, heightAboveGround_10_10u, heightAboveGround_10_10v, heightAboveGround_80_u, heightAboveGround_80_v, heightAboveGround_100_100u, heightAboveGround_100_100v, heightAboveGround_2_2t, heightAboveGround_2_2d, heightAboveGround_2_2r, heightAboveGround_2_2sh, planetaryBoundaryLayer_0_u, planetaryBoundaryLayer_0_v, planetaryBoundaryLayer_0_VRATE, surface_0_dswrf, surface_0_dlwrf, surface_0_prate, surface_0_tp, surface_0_sp, meanSea_0_prmsl, surface_0_gust, lowCloudLayer_0_lcc, middleCloudLayer_0_mcc, highCloudLayer_0_hcc, atmosphere_0_tcc, isobaricInhPa_850_t, isobaricInhPa_850_u, isobaricInhPa_850_v, isobaricInhPa_850_r, isobaricInhPa_700_t, isobaricInhPa_700_u, isobaricInhPa_700_v, isobaricInhPa_500_gh, isobaricInhPa_500_t, isobaricInhPa_500_u, isobaricInhPa_500_v |
| test/ldaps_test.csv | 140,160 | 35 | (140160, 35) | 53.47 MB | forecast_kst_dtm, data_available_kst_dtm, grid_id, latitude, longitude, heightAboveGround_10_10u, heightAboveGround_10_10v, heightAboveGround_50_50MUmax, heightAboveGround_50_50MUmin, heightAboveGround_50_50MVmax, heightAboveGround_50_50MVmin, heightAboveGround_5_XBLWS, heightAboveGround_5_YBLWS, heightAboveGround_2_t, heightAboveGround_2_dpt, heightAboveGround_2_r, heightAboveGround_2_q, surface_0_sp, meanSea_0_prmsl, etc_0_blh, surface_0_NDNSW, surface_0_NDNLW, heightAboveGround_2_SWDIR, heightAboveGround_2_SWDIF, etc_0_hcc, etc_0_mcc, etc_0_lcc, etc_0_VLCDC, surface_0_avg_lsprate, surface_0_lssrate, surface_0_ncpcp, surface_0_snol, surface_0_SNOM, surface_0_lsm, surface_0_h |
| train/gfs_train.csv | 236,736 | 40 | (236736, 40) | 99.34 MB | forecast_kst_dtm, data_available_kst_dtm, grid_id, latitude, longitude, heightAboveGround_10_10u, heightAboveGround_10_10v, heightAboveGround_80_u, heightAboveGround_80_v, heightAboveGround_100_100u, heightAboveGround_100_100v, heightAboveGround_2_2t, heightAboveGround_2_2d, heightAboveGround_2_2r, heightAboveGround_2_2sh, planetaryBoundaryLayer_0_u, planetaryBoundaryLayer_0_v, planetaryBoundaryLayer_0_VRATE, surface_0_dswrf, surface_0_dlwrf, surface_0_prate, surface_0_tp, surface_0_sp, meanSea_0_prmsl, surface_0_gust, lowCloudLayer_0_lcc, middleCloudLayer_0_mcc, highCloudLayer_0_hcc, atmosphere_0_tcc, isobaricInhPa_850_t, isobaricInhPa_850_u, isobaricInhPa_850_v, isobaricInhPa_850_r, isobaricInhPa_700_t, isobaricInhPa_700_u, isobaricInhPa_700_v, isobaricInhPa_500_gh, isobaricInhPa_500_t, isobaricInhPa_500_u, isobaricInhPa_500_v |
| train/ldaps_train.csv | 420,864 | 35 | (420864, 35) | 160.55 MB | forecast_kst_dtm, data_available_kst_dtm, grid_id, latitude, longitude, heightAboveGround_10_10u, heightAboveGround_10_10v, heightAboveGround_50_50MUmax, heightAboveGround_50_50MUmin, heightAboveGround_50_50MVmax, heightAboveGround_50_50MVmin, heightAboveGround_5_XBLWS, heightAboveGround_5_YBLWS, heightAboveGround_2_t, heightAboveGround_2_dpt, heightAboveGround_2_r, heightAboveGround_2_q, surface_0_sp, meanSea_0_prmsl, etc_0_blh, surface_0_NDNSW, surface_0_NDNLW, heightAboveGround_2_SWDIR, heightAboveGround_2_SWDIF, etc_0_hcc, etc_0_mcc, etc_0_lcc, etc_0_VLCDC, surface_0_avg_lsprate, surface_0_lssrate, surface_0_ncpcp, surface_0_snol, surface_0_SNOM, surface_0_lsm, surface_0_h |
| train/scada_unison_train.csv | 105,264 | 16 | (105264, 16) | 18.87 MB | kst_dtm, unison_wtg01_power_kw10m, unison_wtg02_power_kw10m, unison_wtg03_power_kw10m, unison_wtg04_power_kw10m, unison_wtg05_power_kw10m, unison_wtg01_ws, unison_wtg02_ws, unison_wtg03_ws, unison_wtg04_ws, unison_wtg05_ws, unison_wtg01_wd, unison_wtg02_wd, unison_wtg03_wd, unison_wtg04_wd, unison_wtg05_wd |
| train/scada_vestas_train.csv | 157,819 | 37 | (157819, 37) | 53.58 MB | kst_dtm, vestas_wtg01_power_kw10m, vestas_wtg02_power_kw10m, vestas_wtg03_power_kw10m, vestas_wtg04_power_kw10m, vestas_wtg05_power_kw10m, vestas_wtg06_power_kw10m, vestas_wtg07_power_kw10m, vestas_wtg08_power_kw10m, vestas_wtg09_power_kw10m, vestas_wtg10_power_kw10m, vestas_wtg11_power_kw10m, vestas_wtg12_power_kw10m, vestas_wtg01_ws, vestas_wtg02_ws, vestas_wtg03_ws, vestas_wtg04_ws, vestas_wtg05_ws, vestas_wtg06_ws, vestas_wtg07_ws, vestas_wtg08_ws, vestas_wtg09_ws, vestas_wtg10_ws, vestas_wtg11_ws, vestas_wtg12_ws, vestas_wtg01_wd, vestas_wtg02_wd, vestas_wtg03_wd, vestas_wtg04_wd, vestas_wtg05_wd, vestas_wtg06_wd, vestas_wtg07_wd, vestas_wtg08_wd, vestas_wtg09_wd, vestas_wtg10_wd, vestas_wtg11_wd, vestas_wtg12_wd |
| train/train_labels.csv | 26,304 | 4 | (26304, 4) | 2.31 MB | kst_dtm, kpx_group_1, kpx_group_2, kpx_group_3 |

### 컬럼별 dtype

| Dataset | Column | Dtype |
| --- | --- | --- |
| sample_submission.csv | forecast_id | str |
| sample_submission.csv | forecast_kst_dtm | str |
| sample_submission.csv | kpx_group_1 | int64 |
| sample_submission.csv | kpx_group_2 | int64 |
| sample_submission.csv | kpx_group_3 | int64 |
| test/gfs_test.csv | forecast_kst_dtm | str |
| test/gfs_test.csv | data_available_kst_dtm | str |
| test/gfs_test.csv | grid_id | int64 |
| test/gfs_test.csv | latitude | float64 |
| test/gfs_test.csv | longitude | float64 |
| test/gfs_test.csv | heightAboveGround_10_10u | float64 |
| test/gfs_test.csv | heightAboveGround_10_10v | float64 |
| test/gfs_test.csv | heightAboveGround_80_u | float64 |
| test/gfs_test.csv | heightAboveGround_80_v | float64 |
| test/gfs_test.csv | heightAboveGround_100_100u | float64 |
| test/gfs_test.csv | heightAboveGround_100_100v | float64 |
| test/gfs_test.csv | heightAboveGround_2_2t | float64 |
| test/gfs_test.csv | heightAboveGround_2_2d | float64 |
| test/gfs_test.csv | heightAboveGround_2_2r | float64 |
| test/gfs_test.csv | heightAboveGround_2_2sh | float64 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_u | float64 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_v | float64 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_VRATE | float64 |
| test/gfs_test.csv | surface_0_dswrf | float64 |
| test/gfs_test.csv | surface_0_dlwrf | float64 |
| test/gfs_test.csv | surface_0_prate | float64 |
| test/gfs_test.csv | surface_0_tp | float64 |
| test/gfs_test.csv | surface_0_sp | float64 |
| test/gfs_test.csv | meanSea_0_prmsl | float64 |
| test/gfs_test.csv | surface_0_gust | float64 |
| test/gfs_test.csv | lowCloudLayer_0_lcc | float64 |
| test/gfs_test.csv | middleCloudLayer_0_mcc | float64 |
| test/gfs_test.csv | highCloudLayer_0_hcc | float64 |
| test/gfs_test.csv | atmosphere_0_tcc | float64 |
| test/gfs_test.csv | isobaricInhPa_850_t | float64 |
| test/gfs_test.csv | isobaricInhPa_850_u | float64 |
| test/gfs_test.csv | isobaricInhPa_850_v | float64 |
| test/gfs_test.csv | isobaricInhPa_850_r | float64 |
| test/gfs_test.csv | isobaricInhPa_700_t | float64 |
| test/gfs_test.csv | isobaricInhPa_700_u | float64 |
| test/gfs_test.csv | isobaricInhPa_700_v | float64 |
| test/gfs_test.csv | isobaricInhPa_500_gh | float64 |
| test/gfs_test.csv | isobaricInhPa_500_t | float64 |
| test/gfs_test.csv | isobaricInhPa_500_u | float64 |
| test/gfs_test.csv | isobaricInhPa_500_v | float64 |
| test/ldaps_test.csv | forecast_kst_dtm | str |
| test/ldaps_test.csv | data_available_kst_dtm | str |
| test/ldaps_test.csv | grid_id | int64 |
| test/ldaps_test.csv | latitude | float64 |
| test/ldaps_test.csv | longitude | float64 |
| test/ldaps_test.csv | heightAboveGround_10_10u | float64 |
| test/ldaps_test.csv | heightAboveGround_10_10v | float64 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmax | float64 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmin | float64 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmax | float64 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmin | float64 |
| test/ldaps_test.csv | heightAboveGround_5_XBLWS | float64 |
| test/ldaps_test.csv | heightAboveGround_5_YBLWS | float64 |
| test/ldaps_test.csv | heightAboveGround_2_t | float64 |
| test/ldaps_test.csv | heightAboveGround_2_dpt | float64 |
| test/ldaps_test.csv | heightAboveGround_2_r | float64 |
| test/ldaps_test.csv | heightAboveGround_2_q | float64 |
| test/ldaps_test.csv | surface_0_sp | float64 |
| test/ldaps_test.csv | meanSea_0_prmsl | float64 |
| test/ldaps_test.csv | etc_0_blh | float64 |
| test/ldaps_test.csv | surface_0_NDNSW | float64 |
| test/ldaps_test.csv | surface_0_NDNLW | float64 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIR | float64 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIF | float64 |
| test/ldaps_test.csv | etc_0_hcc | float64 |
| test/ldaps_test.csv | etc_0_mcc | float64 |
| test/ldaps_test.csv | etc_0_lcc | float64 |
| test/ldaps_test.csv | etc_0_VLCDC | float64 |
| test/ldaps_test.csv | surface_0_avg_lsprate | float64 |
| test/ldaps_test.csv | surface_0_lssrate | float64 |
| test/ldaps_test.csv | surface_0_ncpcp | float64 |
| test/ldaps_test.csv | surface_0_snol | float64 |
| test/ldaps_test.csv | surface_0_SNOM | float64 |
| test/ldaps_test.csv | surface_0_lsm | float64 |
| test/ldaps_test.csv | surface_0_h | float64 |
| train/gfs_train.csv | forecast_kst_dtm | str |
| train/gfs_train.csv | data_available_kst_dtm | str |
| train/gfs_train.csv | grid_id | int64 |
| train/gfs_train.csv | latitude | float64 |
| train/gfs_train.csv | longitude | float64 |
| train/gfs_train.csv | heightAboveGround_10_10u | float64 |
| train/gfs_train.csv | heightAboveGround_10_10v | float64 |
| train/gfs_train.csv | heightAboveGround_80_u | float64 |
| train/gfs_train.csv | heightAboveGround_80_v | float64 |
| train/gfs_train.csv | heightAboveGround_100_100u | float64 |
| train/gfs_train.csv | heightAboveGround_100_100v | float64 |
| train/gfs_train.csv | heightAboveGround_2_2t | float64 |
| train/gfs_train.csv | heightAboveGround_2_2d | float64 |
| train/gfs_train.csv | heightAboveGround_2_2r | float64 |
| train/gfs_train.csv | heightAboveGround_2_2sh | float64 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_u | float64 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_v | float64 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_VRATE | float64 |
| train/gfs_train.csv | surface_0_dswrf | float64 |
| train/gfs_train.csv | surface_0_dlwrf | float64 |
| train/gfs_train.csv | surface_0_prate | float64 |
| train/gfs_train.csv | surface_0_tp | float64 |
| train/gfs_train.csv | surface_0_sp | float64 |
| train/gfs_train.csv | meanSea_0_prmsl | float64 |
| train/gfs_train.csv | surface_0_gust | float64 |
| train/gfs_train.csv | lowCloudLayer_0_lcc | float64 |
| train/gfs_train.csv | middleCloudLayer_0_mcc | float64 |
| train/gfs_train.csv | highCloudLayer_0_hcc | float64 |
| train/gfs_train.csv | atmosphere_0_tcc | float64 |
| train/gfs_train.csv | isobaricInhPa_850_t | float64 |
| train/gfs_train.csv | isobaricInhPa_850_u | float64 |
| train/gfs_train.csv | isobaricInhPa_850_v | float64 |
| train/gfs_train.csv | isobaricInhPa_850_r | float64 |
| train/gfs_train.csv | isobaricInhPa_700_t | float64 |
| train/gfs_train.csv | isobaricInhPa_700_u | float64 |
| train/gfs_train.csv | isobaricInhPa_700_v | float64 |
| train/gfs_train.csv | isobaricInhPa_500_gh | float64 |
| train/gfs_train.csv | isobaricInhPa_500_t | float64 |
| train/gfs_train.csv | isobaricInhPa_500_u | float64 |
| train/gfs_train.csv | isobaricInhPa_500_v | float64 |
| train/ldaps_train.csv | forecast_kst_dtm | str |
| train/ldaps_train.csv | data_available_kst_dtm | str |
| train/ldaps_train.csv | grid_id | int64 |
| train/ldaps_train.csv | latitude | float64 |
| train/ldaps_train.csv | longitude | float64 |
| train/ldaps_train.csv | heightAboveGround_10_10u | float64 |
| train/ldaps_train.csv | heightAboveGround_10_10v | float64 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmax | float64 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmin | float64 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmax | float64 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmin | float64 |
| train/ldaps_train.csv | heightAboveGround_5_XBLWS | float64 |
| train/ldaps_train.csv | heightAboveGround_5_YBLWS | float64 |
| train/ldaps_train.csv | heightAboveGround_2_t | float64 |
| train/ldaps_train.csv | heightAboveGround_2_dpt | float64 |
| train/ldaps_train.csv | heightAboveGround_2_r | float64 |
| train/ldaps_train.csv | heightAboveGround_2_q | float64 |
| train/ldaps_train.csv | surface_0_sp | float64 |
| train/ldaps_train.csv | meanSea_0_prmsl | float64 |
| train/ldaps_train.csv | etc_0_blh | float64 |
| train/ldaps_train.csv | surface_0_NDNSW | float64 |
| train/ldaps_train.csv | surface_0_NDNLW | float64 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIR | float64 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIF | float64 |
| train/ldaps_train.csv | etc_0_hcc | float64 |
| train/ldaps_train.csv | etc_0_mcc | float64 |
| train/ldaps_train.csv | etc_0_lcc | float64 |
| train/ldaps_train.csv | etc_0_VLCDC | float64 |
| train/ldaps_train.csv | surface_0_avg_lsprate | float64 |
| train/ldaps_train.csv | surface_0_lssrate | float64 |
| train/ldaps_train.csv | surface_0_ncpcp | float64 |
| train/ldaps_train.csv | surface_0_snol | float64 |
| train/ldaps_train.csv | surface_0_SNOM | float64 |
| train/ldaps_train.csv | surface_0_lsm | float64 |
| train/ldaps_train.csv | surface_0_h | float64 |
| train/scada_unison_train.csv | kst_dtm | str |
| train/scada_unison_train.csv | unison_wtg01_power_kw10m | float64 |
| train/scada_unison_train.csv | unison_wtg02_power_kw10m | float64 |
| train/scada_unison_train.csv | unison_wtg03_power_kw10m | float64 |
| train/scada_unison_train.csv | unison_wtg04_power_kw10m | float64 |
| train/scada_unison_train.csv | unison_wtg05_power_kw10m | float64 |
| train/scada_unison_train.csv | unison_wtg01_ws | float64 |
| train/scada_unison_train.csv | unison_wtg02_ws | float64 |
| train/scada_unison_train.csv | unison_wtg03_ws | float64 |
| train/scada_unison_train.csv | unison_wtg04_ws | float64 |
| train/scada_unison_train.csv | unison_wtg05_ws | float64 |
| train/scada_unison_train.csv | unison_wtg01_wd | float64 |
| train/scada_unison_train.csv | unison_wtg02_wd | float64 |
| train/scada_unison_train.csv | unison_wtg03_wd | float64 |
| train/scada_unison_train.csv | unison_wtg04_wd | float64 |
| train/scada_unison_train.csv | unison_wtg05_wd | float64 |
| train/scada_vestas_train.csv | kst_dtm | str |
| train/scada_vestas_train.csv | vestas_wtg01_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg02_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg03_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg04_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg05_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg06_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg07_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg08_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg09_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg10_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg11_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg12_power_kw10m | int64 |
| train/scada_vestas_train.csv | vestas_wtg01_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg02_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg03_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg04_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg05_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg06_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg07_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg08_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg09_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg10_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg11_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg12_ws | float64 |
| train/scada_vestas_train.csv | vestas_wtg01_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg02_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg03_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg04_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg05_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg06_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg07_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg08_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg09_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg10_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg11_wd | float64 |
| train/scada_vestas_train.csv | vestas_wtg12_wd | float64 |
| train/train_labels.csv | kst_dtm | str |
| train/train_labels.csv | kpx_group_1 | float64 |
| train/train_labels.csv | kpx_group_2 | float64 |
| train/train_labels.csv | kpx_group_3 | float64 |

## STEP 3

### 컬럼 사전

| Dataset | Column | Type | Null | Null % | 설명(추정) |
| --- | --- | --- | --- | --- | --- |
| sample_submission.csv | forecast_id | str | 0 | 0 | 제출 행을 식별하는 고유 ID |
| sample_submission.csv | forecast_kst_dtm | str | 0 | 0 | 예보 대상 시각 / 발전량 예측 대상 시각(KST) |
| sample_submission.csv | kpx_group_1 | int64 | 0 | 0 | 제출 대상: KPX 그룹 1 예측 발전량(kWh) |
| sample_submission.csv | kpx_group_2 | int64 | 0 | 0 | 제출 대상: KPX 그룹 2 예측 발전량(kWh) |
| sample_submission.csv | kpx_group_3 | int64 | 0 | 0 | 제출 대상: KPX 그룹 3 예측 발전량(kWh) |
| test/gfs_test.csv | forecast_kst_dtm | str | 0 | 0 | 예보 대상 시각 / 발전량 예측 대상 시각(KST) |
| test/gfs_test.csv | data_available_kst_dtm | str | 0 | 0 | 해당 예보 데이터가 사용 가능해진 시각(KST) |
| test/gfs_test.csv | grid_id | int64 | 0 | 0 | 기상 예보 격자 ID |
| test/gfs_test.csv | latitude | float64 | 0 | 0 | 격자 위도 |
| test/gfs_test.csv | longitude | float64 | 0 | 0 | 격자 경도 |
| test/gfs_test.csv | heightAboveGround_10_10u | float64 | 0 | 0 | 지상 10 m U 성분 바람 |
| test/gfs_test.csv | heightAboveGround_10_10v | float64 | 0 | 0 | 지상 10 m V 성분 바람 |
| test/gfs_test.csv | heightAboveGround_80_u | float64 | 0 | 0 | 지상 80 m U 성분 바람 |
| test/gfs_test.csv | heightAboveGround_80_v | float64 | 0 | 0 | 지상 80 m V 성분 바람 |
| test/gfs_test.csv | heightAboveGround_100_100u | float64 | 0 | 0 | 지상 100 m U 성분 바람 |
| test/gfs_test.csv | heightAboveGround_100_100v | float64 | 0 | 0 | 지상 100 m V 성분 바람 |
| test/gfs_test.csv | heightAboveGround_2_2t | float64 | 0 | 0 | 지상 2 m 기온 |
| test/gfs_test.csv | heightAboveGround_2_2d | float64 | 0 | 0 | 지상 2 m 이슬점온도 |
| test/gfs_test.csv | heightAboveGround_2_2r | float64 | 0 | 0 | 지상 2 m 상대습도 |
| test/gfs_test.csv | heightAboveGround_2_2sh | float64 | 0 | 0 | 지상 2 m 비습 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_u | float64 | 0 | 0 | 행성경계층 U 성분 바람 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_v | float64 | 0 | 0 | 행성경계층 V 성분 바람 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_VRATE | float64 | 0 | 0 | 행성경계층 수직 속도 |
| test/gfs_test.csv | surface_0_dswrf | float64 | 0 | 0 | 지표면 하향 단파복사 플럭스 |
| test/gfs_test.csv | surface_0_dlwrf | float64 | 0 | 0 | 지표면 하향 장파복사 플럭스 |
| test/gfs_test.csv | surface_0_prate | float64 | 0 | 0 | 지표면 강수율 |
| test/gfs_test.csv | surface_0_tp | float64 | 0 | 0 | 지표면 총강수량 |
| test/gfs_test.csv | surface_0_sp | float64 | 0 | 0 | 지표면 기압 |
| test/gfs_test.csv | meanSea_0_prmsl | float64 | 0 | 0 | 해면기압 |
| test/gfs_test.csv | surface_0_gust | float64 | 0 | 0 | 지표면 돌풍 |
| test/gfs_test.csv | lowCloudLayer_0_lcc | float64 | 0 | 0 | 하층운량 |
| test/gfs_test.csv | middleCloudLayer_0_mcc | float64 | 0 | 0 | 중층운량 |
| test/gfs_test.csv | highCloudLayer_0_hcc | float64 | 0 | 0 | 상층운량 |
| test/gfs_test.csv | atmosphere_0_tcc | float64 | 0 | 0 | 전운량 |
| test/gfs_test.csv | isobaricInhPa_850_t | float64 | 0 | 0 | 850 hPa 기온 |
| test/gfs_test.csv | isobaricInhPa_850_u | float64 | 0 | 0 | 850 hPa U 성분 바람 |
| test/gfs_test.csv | isobaricInhPa_850_v | float64 | 0 | 0 | 850 hPa V 성분 바람 |
| test/gfs_test.csv | isobaricInhPa_850_r | float64 | 0 | 0 | 850 hPa 상대습도 |
| test/gfs_test.csv | isobaricInhPa_700_t | float64 | 0 | 0 | 700 hPa 기온 |
| test/gfs_test.csv | isobaricInhPa_700_u | float64 | 0 | 0 | 700 hPa U 성분 바람 |
| test/gfs_test.csv | isobaricInhPa_700_v | float64 | 0 | 0 | 700 hPa V 성분 바람 |
| test/gfs_test.csv | isobaricInhPa_500_gh | float64 | 0 | 0 | 500 hPa 지위고도 |
| test/gfs_test.csv | isobaricInhPa_500_t | float64 | 0 | 0 | 500 hPa 기온 |
| test/gfs_test.csv | isobaricInhPa_500_u | float64 | 0 | 0 | 500 hPa U 성분 바람 |
| test/gfs_test.csv | isobaricInhPa_500_v | float64 | 0 | 0 | 500 hPa V 성분 바람 |
| test/ldaps_test.csv | forecast_kst_dtm | str | 0 | 0 | 예보 대상 시각 / 발전량 예측 대상 시각(KST) |
| test/ldaps_test.csv | data_available_kst_dtm | str | 0 | 0 | 해당 예보 데이터가 사용 가능해진 시각(KST) |
| test/ldaps_test.csv | grid_id | int64 | 0 | 0 | 기상 예보 격자 ID |
| test/ldaps_test.csv | latitude | float64 | 0 | 0 | 격자 위도 |
| test/ldaps_test.csv | longitude | float64 | 0 | 0 | 격자 경도 |
| test/ldaps_test.csv | heightAboveGround_10_10u | float64 | 0 | 0 | 지상 10 m U 성분 바람 |
| test/ldaps_test.csv | heightAboveGround_10_10v | float64 | 0 | 0 | 지상 10 m V 성분 바람 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmax | float64 | 48 | 0.034247 | 지상 50 m U 성분 바람 최댓값 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmin | float64 | 48 | 0.034247 | 지상 50 m U 성분 바람 최솟값 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmax | float64 | 48 | 0.034247 | 지상 50 m V 성분 바람 최댓값 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmin | float64 | 48 | 0.034247 | 지상 50 m V 성분 바람 최솟값 |
| test/ldaps_test.csv | heightAboveGround_5_XBLWS | float64 | 0 | 0 | 지상 5 m X 방향 경계층 바람 |
| test/ldaps_test.csv | heightAboveGround_5_YBLWS | float64 | 16 | 0.011416 | 지상 5 m Y 방향 경계층 바람 |
| test/ldaps_test.csv | heightAboveGround_2_t | float64 | 16 | 0.011416 | 지상 2 m 기온 |
| test/ldaps_test.csv | heightAboveGround_2_dpt | float64 | 16 | 0.011416 | 지상 2 m 이슬점온도 |
| test/ldaps_test.csv | heightAboveGround_2_r | float64 | 16 | 0.011416 | 지상 2 m 상대습도 |
| test/ldaps_test.csv | heightAboveGround_2_q | float64 | 16 | 0.011416 | 지상 2 m 비습 |
| test/ldaps_test.csv | surface_0_sp | float64 | 48 | 0.034247 | 지표면 기압 |
| test/ldaps_test.csv | meanSea_0_prmsl | float64 | 48 | 0.034247 | 해면기압 |
| test/ldaps_test.csv | etc_0_blh | float64 | 48 | 0.034247 | 경계층 높이 |
| test/ldaps_test.csv | surface_0_NDNSW | float64 | 0 | 0 | 지표면 순 하향 단파복사 |
| test/ldaps_test.csv | surface_0_NDNLW | float64 | 0 | 0 | 지표면 순 하향 장파복사 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIR | float64 | 0 | 0 | 지상 2 m 직접 단파복사 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIF | float64 | 0 | 0 | 지상 2 m 산란 단파복사 |
| test/ldaps_test.csv | etc_0_hcc | float64 | 48 | 0.034247 | 상층운량 |
| test/ldaps_test.csv | etc_0_mcc | float64 | 48 | 0.034247 | 중층운량 |
| test/ldaps_test.csv | etc_0_lcc | float64 | 48 | 0.034247 | 하층운량 |
| test/ldaps_test.csv | etc_0_VLCDC | float64 | 48 | 0.034247 | 매우 낮은 층 운량 |
| test/ldaps_test.csv | surface_0_avg_lsprate | float64 | 0 | 0 | 지표면 평균 대규모 강수율 |
| test/ldaps_test.csv | surface_0_lssrate | float64 | 0 | 0 | 지표면 대규모 강설률 |
| test/ldaps_test.csv | surface_0_ncpcp | float64 | 0 | 0 | 지표면 비대류성 강수량 |
| test/ldaps_test.csv | surface_0_snol | float64 | 0 | 0 | 지표면 적설 관련 변수 |
| test/ldaps_test.csv | surface_0_SNOM | float64 | 48 | 0.034247 | 지표면 융설량 |
| test/ldaps_test.csv | surface_0_lsm | float64 | 48 | 0.034247 | 육지/해양 마스크 |
| test/ldaps_test.csv | surface_0_h | float64 | 48 | 0.034247 | 지표면 고도 |
| train/gfs_train.csv | forecast_kst_dtm | str | 0 | 0 | 예보 대상 시각 / 발전량 예측 대상 시각(KST) |
| train/gfs_train.csv | data_available_kst_dtm | str | 0 | 0 | 해당 예보 데이터가 사용 가능해진 시각(KST) |
| train/gfs_train.csv | grid_id | int64 | 0 | 0 | 기상 예보 격자 ID |
| train/gfs_train.csv | latitude | float64 | 0 | 0 | 격자 위도 |
| train/gfs_train.csv | longitude | float64 | 0 | 0 | 격자 경도 |
| train/gfs_train.csv | heightAboveGround_10_10u | float64 | 0 | 0 | 지상 10 m U 성분 바람 |
| train/gfs_train.csv | heightAboveGround_10_10v | float64 | 0 | 0 | 지상 10 m V 성분 바람 |
| train/gfs_train.csv | heightAboveGround_80_u | float64 | 0 | 0 | 지상 80 m U 성분 바람 |
| train/gfs_train.csv | heightAboveGround_80_v | float64 | 0 | 0 | 지상 80 m V 성분 바람 |
| train/gfs_train.csv | heightAboveGround_100_100u | float64 | 0 | 0 | 지상 100 m U 성분 바람 |
| train/gfs_train.csv | heightAboveGround_100_100v | float64 | 0 | 0 | 지상 100 m V 성분 바람 |
| train/gfs_train.csv | heightAboveGround_2_2t | float64 | 0 | 0 | 지상 2 m 기온 |
| train/gfs_train.csv | heightAboveGround_2_2d | float64 | 0 | 0 | 지상 2 m 이슬점온도 |
| train/gfs_train.csv | heightAboveGround_2_2r | float64 | 0 | 0 | 지상 2 m 상대습도 |
| train/gfs_train.csv | heightAboveGround_2_2sh | float64 | 0 | 0 | 지상 2 m 비습 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_u | float64 | 0 | 0 | 행성경계층 U 성분 바람 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_v | float64 | 0 | 0 | 행성경계층 V 성분 바람 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_VRATE | float64 | 0 | 0 | 행성경계층 수직 속도 |
| train/gfs_train.csv | surface_0_dswrf | float64 | 0 | 0 | 지표면 하향 단파복사 플럭스 |
| train/gfs_train.csv | surface_0_dlwrf | float64 | 0 | 0 | 지표면 하향 장파복사 플럭스 |
| train/gfs_train.csv | surface_0_prate | float64 | 0 | 0 | 지표면 강수율 |
| train/gfs_train.csv | surface_0_tp | float64 | 0 | 0 | 지표면 총강수량 |
| train/gfs_train.csv | surface_0_sp | float64 | 0 | 0 | 지표면 기압 |
| train/gfs_train.csv | meanSea_0_prmsl | float64 | 0 | 0 | 해면기압 |
| train/gfs_train.csv | surface_0_gust | float64 | 0 | 0 | 지표면 돌풍 |
| train/gfs_train.csv | lowCloudLayer_0_lcc | float64 | 0 | 0 | 하층운량 |
| train/gfs_train.csv | middleCloudLayer_0_mcc | float64 | 0 | 0 | 중층운량 |
| train/gfs_train.csv | highCloudLayer_0_hcc | float64 | 0 | 0 | 상층운량 |
| train/gfs_train.csv | atmosphere_0_tcc | float64 | 0 | 0 | 전운량 |
| train/gfs_train.csv | isobaricInhPa_850_t | float64 | 0 | 0 | 850 hPa 기온 |
| train/gfs_train.csv | isobaricInhPa_850_u | float64 | 0 | 0 | 850 hPa U 성분 바람 |
| train/gfs_train.csv | isobaricInhPa_850_v | float64 | 0 | 0 | 850 hPa V 성분 바람 |
| train/gfs_train.csv | isobaricInhPa_850_r | float64 | 0 | 0 | 850 hPa 상대습도 |
| train/gfs_train.csv | isobaricInhPa_700_t | float64 | 0 | 0 | 700 hPa 기온 |
| train/gfs_train.csv | isobaricInhPa_700_u | float64 | 0 | 0 | 700 hPa U 성분 바람 |
| train/gfs_train.csv | isobaricInhPa_700_v | float64 | 0 | 0 | 700 hPa V 성분 바람 |
| train/gfs_train.csv | isobaricInhPa_500_gh | float64 | 0 | 0 | 500 hPa 지위고도 |
| train/gfs_train.csv | isobaricInhPa_500_t | float64 | 0 | 0 | 500 hPa 기온 |
| train/gfs_train.csv | isobaricInhPa_500_u | float64 | 0 | 0 | 500 hPa U 성분 바람 |
| train/gfs_train.csv | isobaricInhPa_500_v | float64 | 0 | 0 | 500 hPa V 성분 바람 |
| train/ldaps_train.csv | forecast_kst_dtm | str | 0 | 0 | 예보 대상 시각 / 발전량 예측 대상 시각(KST) |
| train/ldaps_train.csv | data_available_kst_dtm | str | 0 | 0 | 해당 예보 데이터가 사용 가능해진 시각(KST) |
| train/ldaps_train.csv | grid_id | int64 | 0 | 0 | 기상 예보 격자 ID |
| train/ldaps_train.csv | latitude | float64 | 0 | 0 | 격자 위도 |
| train/ldaps_train.csv | longitude | float64 | 0 | 0 | 격자 경도 |
| train/ldaps_train.csv | heightAboveGround_10_10u | float64 | 0 | 0 | 지상 10 m U 성분 바람 |
| train/ldaps_train.csv | heightAboveGround_10_10v | float64 | 0 | 0 | 지상 10 m V 성분 바람 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmax | float64 | 0 | 0 | 지상 50 m U 성분 바람 최댓값 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmin | float64 | 0 | 0 | 지상 50 m U 성분 바람 최솟값 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmax | float64 | 0 | 0 | 지상 50 m V 성분 바람 최댓값 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmin | float64 | 0 | 0 | 지상 50 m V 성분 바람 최솟값 |
| train/ldaps_train.csv | heightAboveGround_5_XBLWS | float64 | 0 | 0 | 지상 5 m X 방향 경계층 바람 |
| train/ldaps_train.csv | heightAboveGround_5_YBLWS | float64 | 0 | 0 | 지상 5 m Y 방향 경계층 바람 |
| train/ldaps_train.csv | heightAboveGround_2_t | float64 | 0 | 0 | 지상 2 m 기온 |
| train/ldaps_train.csv | heightAboveGround_2_dpt | float64 | 0 | 0 | 지상 2 m 이슬점온도 |
| train/ldaps_train.csv | heightAboveGround_2_r | float64 | 0 | 0 | 지상 2 m 상대습도 |
| train/ldaps_train.csv | heightAboveGround_2_q | float64 | 0 | 0 | 지상 2 m 비습 |
| train/ldaps_train.csv | surface_0_sp | float64 | 0 | 0 | 지표면 기압 |
| train/ldaps_train.csv | meanSea_0_prmsl | float64 | 0 | 0 | 해면기압 |
| train/ldaps_train.csv | etc_0_blh | float64 | 0 | 0 | 경계층 높이 |
| train/ldaps_train.csv | surface_0_NDNSW | float64 | 0 | 0 | 지표면 순 하향 단파복사 |
| train/ldaps_train.csv | surface_0_NDNLW | float64 | 0 | 0 | 지표면 순 하향 장파복사 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIR | float64 | 0 | 0 | 지상 2 m 직접 단파복사 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIF | float64 | 0 | 0 | 지상 2 m 산란 단파복사 |
| train/ldaps_train.csv | etc_0_hcc | float64 | 0 | 0 | 상층운량 |
| train/ldaps_train.csv | etc_0_mcc | float64 | 0 | 0 | 중층운량 |
| train/ldaps_train.csv | etc_0_lcc | float64 | 0 | 0 | 하층운량 |
| train/ldaps_train.csv | etc_0_VLCDC | float64 | 0 | 0 | 매우 낮은 층 운량 |
| train/ldaps_train.csv | surface_0_avg_lsprate | float64 | 0 | 0 | 지표면 평균 대규모 강수율 |
| train/ldaps_train.csv | surface_0_lssrate | float64 | 0 | 0 | 지표면 대규모 강설률 |
| train/ldaps_train.csv | surface_0_ncpcp | float64 | 0 | 0 | 지표면 비대류성 강수량 |
| train/ldaps_train.csv | surface_0_snol | float64 | 0 | 0 | 지표면 적설 관련 변수 |
| train/ldaps_train.csv | surface_0_SNOM | float64 | 0 | 0 | 지표면 융설량 |
| train/ldaps_train.csv | surface_0_lsm | float64 | 0 | 0 | 육지/해양 마스크 |
| train/ldaps_train.csv | surface_0_h | float64 | 0 | 0 | 지표면 고도 |
| train/scada_unison_train.csv | kst_dtm | str | 0 | 0 | SCADA 계측 시각(KST) |
| train/scada_unison_train.csv | unison_wtg01_power_kw10m | float64 | 208 | 0.197598 | UNISON 1-5호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_unison_train.csv | unison_wtg02_power_kw10m | float64 | 1,362 | 1.29389 | UNISON 1-5호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_unison_train.csv | unison_wtg03_power_kw10m | float64 | 352 | 0.334397 | UNISON 1-5호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_unison_train.csv | unison_wtg04_power_kw10m | float64 | 150 | 0.142499 | UNISON 1-5호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_unison_train.csv | unison_wtg05_power_kw10m | float64 | 142 | 0.134899 | UNISON 1-5호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_unison_train.csv | unison_wtg01_ws | float64 | 1,466 | 1.392689 | UNISON 1-5호기 풍속입니다. |
| train/scada_unison_train.csv | unison_wtg02_ws | float64 | 1,424 | 1.352789 | UNISON 1-5호기 풍속입니다. |
| train/scada_unison_train.csv | unison_wtg03_ws | float64 | 447 | 0.424647 | UNISON 1-5호기 풍속입니다. |
| train/scada_unison_train.csv | unison_wtg04_ws | float64 | 380 | 0.360997 | UNISON 1-5호기 풍속입니다. |
| train/scada_unison_train.csv | unison_wtg05_ws | float64 | 1,379 | 1.31004 | UNISON 1-5호기 풍속입니다. |
| train/scada_unison_train.csv | unison_wtg01_wd | float64 | 208 | 0.197598 | UNISON 1-5호기 풍향입니다. |
| train/scada_unison_train.csv | unison_wtg02_wd | float64 | 1,354 | 1.28629 | UNISON 1-5호기 풍향입니다. |
| train/scada_unison_train.csv | unison_wtg03_wd | float64 | 347 | 0.329647 | UNISON 1-5호기 풍향입니다. |
| train/scada_unison_train.csv | unison_wtg04_wd | float64 | 152 | 0.144399 | UNISON 1-5호기 풍향입니다. |
| train/scada_unison_train.csv | unison_wtg05_wd | float64 | 140 | 0.132999 | UNISON 1-5호기 풍향입니다. |
| train/scada_vestas_train.csv | kst_dtm | str | 0 | 0 | SCADA 계측 시각(KST) |
| train/scada_vestas_train.csv | vestas_wtg01_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg02_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg03_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg04_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg05_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg06_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg07_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg08_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg09_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg10_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg11_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg12_power_kw10m | int64 | 0 | 0 | VESTAS 1-12호기 10분 단위 power 값입니다. 원천 컬럼명 기준 단위는 `kW10m`입니다. |
| train/scada_vestas_train.csv | vestas_wtg01_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg02_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg03_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg04_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg05_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg06_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg07_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg08_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg09_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg10_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg11_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg12_ws | float64 | 0 | 0 | VESTAS 1-12호기 풍속입니다. |
| train/scada_vestas_train.csv | vestas_wtg01_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg02_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg03_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg04_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg05_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg06_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg07_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg08_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg09_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg10_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg11_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/scada_vestas_train.csv | vestas_wtg12_wd | float64 | 0 | 0 | VESTAS 1-12호기 풍향입니다. |
| train/train_labels.csv | kst_dtm | str | 0 | 0 | 실제 발전량 집계 구간 종료 시각(KST) |
| train/train_labels.csv | kpx_group_1 | float64 | 104 | 0.395377 | Target: KPX 그룹 1 실제 발전량(kWh) |
| train/train_labels.csv | kpx_group_2 | float64 | 103 | 0.391575 | Target: KPX 그룹 2 실제 발전량(kWh) |
| train/train_labels.csv | kpx_group_3 | float64 | 8,766 | 33.32573 | Target: KPX 그룹 3 실제 발전량(kWh) |

### info.xlsx Metadata 요약

| Metric | Value |
| --- | --- |
| Rows | 17 |
| Columns | 11 |
| Column: 단계 | non-null 17, unique 2 |
| Column: 명칭 | non-null 17, unique 2 |
| Column: 제작사 | non-null 17, unique 2 |
| Column: 모델명 | non-null 17, unique 2 |
| Column: 호기 | non-null 17, unique 12 |
| Column: 좌표(Google) | non-null 17, unique 17 |
| Column: KPX그룹 | non-null 3, unique 3 |
| Column: Hub Height(m) | non-null 17, unique 1 |
| Column: Rotor Diameter(m) | non-null 17, unique 2 |
| Column: 설비용량(MW) | non-null 17, unique 2 |
| Column: 그룹설비용량(MW) | non-null 3, unique 2 |

## STEP 4

### 결측치 요약

| Dataset | Rows | Columns | Total Missing Cells | Columns With Missing | Max Missing % |
| --- | --- | --- | --- | --- | --- |
| sample_submission.csv | 8,760 | 5 | 0 | 0 | 0 |
| test/gfs_test.csv | 78,840 | 40 | 0 | 0 | 0 |
| test/ldaps_test.csv | 140,160 | 35 | 752 | 19 | 0.034247 |
| train/gfs_train.csv | 236,736 | 40 | 0 | 0 | 0 |
| train/ldaps_train.csv | 420,864 | 35 | 0 | 0 | 0 |
| train/scada_unison_train.csv | 105,264 | 16 | 9,511 | 15 | 1.392689 |
| train/scada_vestas_train.csv | 157,819 | 37 | 0 | 0 | 0 |
| train/train_labels.csv | 26,304 | 4 | 8,973 | 3 | 33.32573 |

![Top Missing Rates](missing_rates_top.svg)

### 컬럼별 결측치

| Dataset | Column | Missing Count | Missing % |
| --- | --- | --- | --- |
| sample_submission.csv | forecast_id | 0 | 0 |
| sample_submission.csv | forecast_kst_dtm | 0 | 0 |
| sample_submission.csv | kpx_group_1 | 0 | 0 |
| sample_submission.csv | kpx_group_2 | 0 | 0 |
| sample_submission.csv | kpx_group_3 | 0 | 0 |
| test/gfs_test.csv | forecast_kst_dtm | 0 | 0 |
| test/gfs_test.csv | data_available_kst_dtm | 0 | 0 |
| test/gfs_test.csv | grid_id | 0 | 0 |
| test/gfs_test.csv | latitude | 0 | 0 |
| test/gfs_test.csv | longitude | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_10_10u | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_10_10v | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_80_u | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_80_v | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_100_100u | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_100_100v | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_2_2t | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_2_2d | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_2_2r | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_2_2sh | 0 | 0 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_u | 0 | 0 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_v | 0 | 0 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_VRATE | 0 | 0 |
| test/gfs_test.csv | surface_0_dswrf | 0 | 0 |
| test/gfs_test.csv | surface_0_dlwrf | 0 | 0 |
| test/gfs_test.csv | surface_0_prate | 0 | 0 |
| test/gfs_test.csv | surface_0_tp | 0 | 0 |
| test/gfs_test.csv | surface_0_sp | 0 | 0 |
| test/gfs_test.csv | meanSea_0_prmsl | 0 | 0 |
| test/gfs_test.csv | surface_0_gust | 0 | 0 |
| test/gfs_test.csv | lowCloudLayer_0_lcc | 0 | 0 |
| test/gfs_test.csv | middleCloudLayer_0_mcc | 0 | 0 |
| test/gfs_test.csv | highCloudLayer_0_hcc | 0 | 0 |
| test/gfs_test.csv | atmosphere_0_tcc | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_850_t | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_850_u | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_850_v | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_850_r | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_700_t | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_700_u | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_700_v | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_500_gh | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_500_t | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_500_u | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_500_v | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmax | 48 | 0.034247 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmin | 48 | 0.034247 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmax | 48 | 0.034247 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmin | 48 | 0.034247 |
| test/ldaps_test.csv | surface_0_sp | 48 | 0.034247 |
| test/ldaps_test.csv | meanSea_0_prmsl | 48 | 0.034247 |
| test/ldaps_test.csv | etc_0_blh | 48 | 0.034247 |
| test/ldaps_test.csv | etc_0_hcc | 48 | 0.034247 |
| test/ldaps_test.csv | etc_0_mcc | 48 | 0.034247 |
| test/ldaps_test.csv | etc_0_lcc | 48 | 0.034247 |
| test/ldaps_test.csv | etc_0_VLCDC | 48 | 0.034247 |
| test/ldaps_test.csv | surface_0_SNOM | 48 | 0.034247 |
| test/ldaps_test.csv | surface_0_lsm | 48 | 0.034247 |
| test/ldaps_test.csv | surface_0_h | 48 | 0.034247 |
| test/ldaps_test.csv | heightAboveGround_5_YBLWS | 16 | 0.011416 |
| test/ldaps_test.csv | heightAboveGround_2_t | 16 | 0.011416 |
| test/ldaps_test.csv | heightAboveGround_2_dpt | 16 | 0.011416 |
| test/ldaps_test.csv | heightAboveGround_2_r | 16 | 0.011416 |
| test/ldaps_test.csv | heightAboveGround_2_q | 16 | 0.011416 |
| test/ldaps_test.csv | forecast_kst_dtm | 0 | 0 |
| test/ldaps_test.csv | data_available_kst_dtm | 0 | 0 |
| test/ldaps_test.csv | grid_id | 0 | 0 |
| test/ldaps_test.csv | latitude | 0 | 0 |
| test/ldaps_test.csv | longitude | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_10_10u | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_10_10v | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_5_XBLWS | 0 | 0 |
| test/ldaps_test.csv | surface_0_NDNSW | 0 | 0 |
| test/ldaps_test.csv | surface_0_NDNLW | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIR | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIF | 0 | 0 |
| test/ldaps_test.csv | surface_0_avg_lsprate | 0 | 0 |
| test/ldaps_test.csv | surface_0_lssrate | 0 | 0 |
| test/ldaps_test.csv | surface_0_ncpcp | 0 | 0 |
| test/ldaps_test.csv | surface_0_snol | 0 | 0 |
| train/gfs_train.csv | forecast_kst_dtm | 0 | 0 |
| train/gfs_train.csv | data_available_kst_dtm | 0 | 0 |
| train/gfs_train.csv | grid_id | 0 | 0 |
| train/gfs_train.csv | latitude | 0 | 0 |
| train/gfs_train.csv | longitude | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_10_10u | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_10_10v | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_80_u | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_80_v | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_100_100u | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_100_100v | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_2_2t | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_2_2d | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_2_2r | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_2_2sh | 0 | 0 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_u | 0 | 0 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_v | 0 | 0 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_VRATE | 0 | 0 |
| train/gfs_train.csv | surface_0_dswrf | 0 | 0 |
| train/gfs_train.csv | surface_0_dlwrf | 0 | 0 |
| train/gfs_train.csv | surface_0_prate | 0 | 0 |
| train/gfs_train.csv | surface_0_tp | 0 | 0 |
| train/gfs_train.csv | surface_0_sp | 0 | 0 |
| train/gfs_train.csv | meanSea_0_prmsl | 0 | 0 |
| train/gfs_train.csv | surface_0_gust | 0 | 0 |
| train/gfs_train.csv | lowCloudLayer_0_lcc | 0 | 0 |
| train/gfs_train.csv | middleCloudLayer_0_mcc | 0 | 0 |
| train/gfs_train.csv | highCloudLayer_0_hcc | 0 | 0 |
| train/gfs_train.csv | atmosphere_0_tcc | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_850_t | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_850_u | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_850_v | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_850_r | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_700_t | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_700_u | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_700_v | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_500_gh | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_500_t | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_500_u | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_500_v | 0 | 0 |
| train/ldaps_train.csv | forecast_kst_dtm | 0 | 0 |
| train/ldaps_train.csv | data_available_kst_dtm | 0 | 0 |
| train/ldaps_train.csv | grid_id | 0 | 0 |
| train/ldaps_train.csv | latitude | 0 | 0 |
| train/ldaps_train.csv | longitude | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_10_10u | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_10_10v | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmax | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmin | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmax | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmin | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_5_XBLWS | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_5_YBLWS | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_t | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_dpt | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_r | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_q | 0 | 0 |
| train/ldaps_train.csv | surface_0_sp | 0 | 0 |
| train/ldaps_train.csv | meanSea_0_prmsl | 0 | 0 |
| train/ldaps_train.csv | etc_0_blh | 0 | 0 |
| train/ldaps_train.csv | surface_0_NDNSW | 0 | 0 |
| train/ldaps_train.csv | surface_0_NDNLW | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIR | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIF | 0 | 0 |
| train/ldaps_train.csv | etc_0_hcc | 0 | 0 |
| train/ldaps_train.csv | etc_0_mcc | 0 | 0 |
| train/ldaps_train.csv | etc_0_lcc | 0 | 0 |
| train/ldaps_train.csv | etc_0_VLCDC | 0 | 0 |
| train/ldaps_train.csv | surface_0_avg_lsprate | 0 | 0 |
| train/ldaps_train.csv | surface_0_lssrate | 0 | 0 |
| train/ldaps_train.csv | surface_0_ncpcp | 0 | 0 |
| train/ldaps_train.csv | surface_0_snol | 0 | 0 |
| train/ldaps_train.csv | surface_0_SNOM | 0 | 0 |
| train/ldaps_train.csv | surface_0_lsm | 0 | 0 |
| train/ldaps_train.csv | surface_0_h | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg01_ws | 1,466 | 1.392689 |
| train/scada_unison_train.csv | unison_wtg02_ws | 1,424 | 1.352789 |
| train/scada_unison_train.csv | unison_wtg05_ws | 1,379 | 1.31004 |
| train/scada_unison_train.csv | unison_wtg02_power_kw10m | 1,362 | 1.29389 |
| train/scada_unison_train.csv | unison_wtg02_wd | 1,354 | 1.28629 |
| train/scada_unison_train.csv | unison_wtg03_ws | 447 | 0.424647 |
| train/scada_unison_train.csv | unison_wtg04_ws | 380 | 0.360997 |
| train/scada_unison_train.csv | unison_wtg03_power_kw10m | 352 | 0.334397 |
| train/scada_unison_train.csv | unison_wtg03_wd | 347 | 0.329647 |
| train/scada_unison_train.csv | unison_wtg01_power_kw10m | 208 | 0.197598 |
| train/scada_unison_train.csv | unison_wtg01_wd | 208 | 0.197598 |
| train/scada_unison_train.csv | unison_wtg04_wd | 152 | 0.144399 |
| train/scada_unison_train.csv | unison_wtg04_power_kw10m | 150 | 0.142499 |
| train/scada_unison_train.csv | unison_wtg05_power_kw10m | 142 | 0.134899 |
| train/scada_unison_train.csv | unison_wtg05_wd | 140 | 0.132999 |
| train/scada_unison_train.csv | kst_dtm | 0 | 0 |
| train/scada_vestas_train.csv | kst_dtm | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg01_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg02_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg03_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg04_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg05_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg06_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg07_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg08_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg09_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg10_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg11_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg12_power_kw10m | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg01_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg02_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg03_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg04_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg05_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg06_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg07_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg08_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg09_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg10_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg11_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg12_ws | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg01_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg02_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg03_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg04_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg05_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg06_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg07_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg08_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg09_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg10_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg11_wd | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg12_wd | 0 | 0 |
| train/train_labels.csv | kpx_group_3 | 8,766 | 33.32573 |
| train/train_labels.csv | kpx_group_1 | 104 | 0.395377 |
| train/train_labels.csv | kpx_group_2 | 103 | 0.391575 |
| train/train_labels.csv | kst_dtm | 0 | 0 |

### 결측률 10% 이상 컬럼

| Dataset | Column | Missing Count | Missing % |
| --- | --- | --- | --- |
| train/train_labels.csv | kpx_group_3 | 8,766 | 33.32573 |

## STEP 5

### 데이터 타입 검사

| Dataset | Column | Current Dtype | Inspection | Datetime Parse % | Numeric Parse % | Suggested Action |
| --- | --- | --- | --- | --- | --- | --- |
| sample_submission.csv | forecast_id | str | 정상 |  |  | 변환 필요 없음 |
| sample_submission.csv | forecast_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| sample_submission.csv | kpx_group_1 | int64 | 숫자형 ID/범주 후보 |  |  | 연산 피처가 아니라 key/category로 취급 검토 |
| sample_submission.csv | kpx_group_2 | int64 | 숫자형 ID/범주 후보 |  |  | 연산 피처가 아니라 key/category로 취급 검토 |
| sample_submission.csv | kpx_group_3 | int64 | 숫자형 ID/범주 후보 |  |  | 연산 피처가 아니라 key/category로 취급 검토 |
| test/gfs_test.csv | forecast_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | data_available_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | grid_id | int64 | 숫자형 ID/범주 후보 |  |  | 연산 피처가 아니라 key/category로 취급 검토 |
| test/gfs_test.csv | latitude | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | longitude | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_10_10u | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_10_10v | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_80_u | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_80_v | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_100_100u | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_100_100v | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_2_2t | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_2_2d | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_2_2r | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | heightAboveGround_2_2sh | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_u | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_v | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_VRATE | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | surface_0_dswrf | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | surface_0_dlwrf | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | surface_0_prate | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | surface_0_tp | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | surface_0_sp | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | meanSea_0_prmsl | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | surface_0_gust | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | lowCloudLayer_0_lcc | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | middleCloudLayer_0_mcc | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | highCloudLayer_0_hcc | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | atmosphere_0_tcc | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_850_t | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_850_u | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_850_v | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_850_r | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_700_t | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_700_u | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_700_v | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_500_gh | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_500_t | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_500_u | float64 | 정상 |  |  | 변환 필요 없음 |
| test/gfs_test.csv | isobaricInhPa_500_v | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | forecast_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | data_available_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | grid_id | int64 | 숫자형 ID/범주 후보 |  |  | 연산 피처가 아니라 key/category로 취급 검토 |
| test/ldaps_test.csv | latitude | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | longitude | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_10_10u | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_10_10v | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmax | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmin | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmax | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmin | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_5_XBLWS | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_5_YBLWS | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_2_t | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_2_dpt | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_2_r | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_2_q | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_sp | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | meanSea_0_prmsl | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | etc_0_blh | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_NDNSW | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_NDNLW | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIR | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIF | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | etc_0_hcc | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | etc_0_mcc | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | etc_0_lcc | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | etc_0_VLCDC | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_avg_lsprate | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_lssrate | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_ncpcp | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_snol | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_SNOM | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_lsm | float64 | 정상 |  |  | 변환 필요 없음 |
| test/ldaps_test.csv | surface_0_h | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | forecast_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | data_available_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | grid_id | int64 | 숫자형 ID/범주 후보 |  |  | 연산 피처가 아니라 key/category로 취급 검토 |
| train/gfs_train.csv | latitude | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | longitude | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_10_10u | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_10_10v | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_80_u | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_80_v | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_100_100u | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_100_100v | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_2_2t | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_2_2d | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_2_2r | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | heightAboveGround_2_2sh | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_u | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_v | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_VRATE | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | surface_0_dswrf | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | surface_0_dlwrf | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | surface_0_prate | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | surface_0_tp | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | surface_0_sp | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | meanSea_0_prmsl | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | surface_0_gust | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | lowCloudLayer_0_lcc | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | middleCloudLayer_0_mcc | float64 | 숫자형 ID/범주 후보 |  |  | 연산 피처가 아니라 key/category로 취급 검토 |
| train/gfs_train.csv | highCloudLayer_0_hcc | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | atmosphere_0_tcc | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_850_t | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_850_u | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_850_v | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_850_r | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_700_t | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_700_u | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_700_v | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_500_gh | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_500_t | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_500_u | float64 | 정상 |  |  | 변환 필요 없음 |
| train/gfs_train.csv | isobaricInhPa_500_v | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | forecast_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | data_available_kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | grid_id | int64 | 숫자형 ID/범주 후보 |  |  | 연산 피처가 아니라 key/category로 취급 검토 |
| train/ldaps_train.csv | latitude | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | longitude | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_10_10u | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_10_10v | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmax | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmin | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmax | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmin | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_5_XBLWS | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_5_YBLWS | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_2_t | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_2_dpt | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_2_r | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_2_q | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_sp | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | meanSea_0_prmsl | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | etc_0_blh | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_NDNSW | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_NDNLW | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIR | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIF | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | etc_0_hcc | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | etc_0_mcc | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | etc_0_lcc | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | etc_0_VLCDC | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_avg_lsprate | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_lssrate | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_ncpcp | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_snol | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_SNOM | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_lsm | float64 | 정상 |  |  | 변환 필요 없음 |
| train/ldaps_train.csv | surface_0_h | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg01_power_kw10m | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg02_power_kw10m | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg03_power_kw10m | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg04_power_kw10m | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg05_power_kw10m | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg01_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg02_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg03_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg04_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg05_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg01_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg02_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg03_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg04_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_unison_train.csv | unison_wtg05_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg01_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg02_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg03_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg04_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg05_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg06_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg07_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg08_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg09_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg10_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg11_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg12_power_kw10m | int64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg01_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg02_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg03_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg04_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg05_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg06_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg07_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg08_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg09_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg10_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg11_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg12_ws | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg01_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg02_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg03_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg04_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg05_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg06_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg07_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg08_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg09_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg10_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg11_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/scada_vestas_train.csv | vestas_wtg12_wd | float64 | 정상 |  |  | 변환 필요 없음 |
| train/train_labels.csv | kst_dtm | str | 정상 |  |  | 변환 필요 없음 |
| train/train_labels.csv | kpx_group_1 | float64 | 정상 |  |  | 변환 필요 없음 |
| train/train_labels.csv | kpx_group_2 | float64 | 정상 |  |  | 변환 필요 없음 |
| train/train_labels.csv | kpx_group_3 | float64 | 정상 |  |  | 변환 필요 없음 |

## STEP 6

### 시간 데이터 분석

| Dataset | Time Column | Parsed % | Start | End | Unique Times | Mode Interval | Interval Distribution Top | Raw Duplicate Timestamps | Missing Intervals | Timezone In Raw String | Parsed Timezone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sample_submission.csv | forecast_kst_dtm | 100 | 2025-01-01 01:00:00 | 2026-01-01 00:00:00 | 8,760 | 0 days 01:00:00 | 0 days 01:00:00: 8,759 | 0 | 0 | 없음 | 없음(KST naive) |
| test/gfs_test.csv | forecast_kst_dtm | 100 | 2025-01-01 01:00:00 | 2026-01-01 00:00:00 | 8,760 | 0 days 01:00:00 | 0 days 01:00:00: 8,759 | 70,080 | 0 | 없음 | 없음(KST naive) |
| test/gfs_test.csv | data_available_kst_dtm | 100 | 2024-12-31 13:00:00 | 2025-12-30 13:00:00 | 365 | 1 days 00:00:00 | 1 days 00:00:00: 364 | 78,475 | 0 | 없음 | 없음(KST naive) |
| test/ldaps_test.csv | forecast_kst_dtm | 100 | 2025-01-01 01:00:00 | 2026-01-01 00:00:00 | 8,760 | 0 days 01:00:00 | 0 days 01:00:00: 8,759 | 131,400 | 0 | 없음 | 없음(KST naive) |
| test/ldaps_test.csv | data_available_kst_dtm | 100 | 2024-12-31 13:00:00 | 2025-12-30 13:00:00 | 365 | 1 days 00:00:00 | 1 days 00:00:00: 364 | 139,795 | 0 | 없음 | 없음(KST naive) |
| train/gfs_train.csv | forecast_kst_dtm | 100 | 2022-01-01 01:00:00 | 2025-01-01 00:00:00 | 26,304 | 0 days 01:00:00 | 0 days 01:00:00: 26,303 | 210,432 | 0 | 없음 | 없음(KST naive) |
| train/gfs_train.csv | data_available_kst_dtm | 100 | 2021-12-31 13:00:00 | 2024-12-30 13:00:00 | 1,096 | 1 days 00:00:00 | 1 days 00:00:00: 1,095 | 235,640 | 0 | 없음 | 없음(KST naive) |
| train/ldaps_train.csv | forecast_kst_dtm | 100 | 2022-01-01 01:00:00 | 2025-01-01 00:00:00 | 26,304 | 0 days 01:00:00 | 0 days 01:00:00: 26,303 | 394,560 | 0 | 없음 | 없음(KST naive) |
| train/ldaps_train.csv | data_available_kst_dtm | 100 | 2021-12-31 13:00:00 | 2024-12-30 13:00:00 | 1,096 | 1 days 00:00:00 | 1 days 00:00:00: 1,095 | 419,768 | 0 | 없음 | 없음(KST naive) |
| train/scada_unison_train.csv | kst_dtm | 100 | 2023-01-01 00:10:00 | 2025-01-01 00:00:00 | 105,264 | 0 days 00:10:00 | 0 days 00:10:00: 105,263 | 0 | 0 | 없음 | 없음(KST naive) |
| train/scada_vestas_train.csv | kst_dtm | 100 | 2022-01-01 01:00:00 | 2025-01-01 00:00:00 | 157,819 | 0 days 00:10:00 | 0 days 00:10:00: 157,818 | 0 | 0 | 없음 | 없음(KST naive) |
| train/train_labels.csv | kst_dtm | 100 | 2022-01-01 01:00:00 | 2025-01-01 00:00:00 | 26,304 | 0 days 01:00:00 | 0 days 01:00:00: 26,303 | 0 | 0 | 없음 | 없음(KST naive) |

## STEP 7

### Target 분석

| Target | Missing | Min | Max | Mean | Median | Std | Zero Count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kpx_group_1 | 104 | 0 | 21,275.305 | 6,621.981 | 4,252.168 | 6,582.443 | 3,001 |
| kpx_group_2 | 103 | 0 | 21,362.084 | 7,076.843 | 4,382.337 | 7,001.146 | 2,992 |
| kpx_group_3 | 8,766 | 0 | 21,130.674 | 5,563.82 | 2,719.074 | 6,294.583 | 2,846 |

### Target 설비용량 기준 점검

| Target | Capacity kWh/h | Below 0 Count | Above Capacity Count | Max / Capacity |
| --- | --- | --- | --- | --- |
| kpx_group_1 | 21,600 | 0 | 0 | 0.984968 |
| kpx_group_2 | 21,600 | 0 | 0 | 0.988985 |
| kpx_group_3 | 21,000 | 0 | 38 | 1.006223 |

![Target Histograms](target_histograms.svg)

## STEP 8

### 수치형 변수 분석

| Dataset | Column | Count | Mean | Std | Min | 25% | Median | 75% | Max | Skew | Kurtosis | IQR Outliers | Outlier % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sample_submission.csv | kpx_group_1 | 8,760 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sample_submission.csv | kpx_group_2 | 8,760 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sample_submission.csv | kpx_group_3 | 8,760 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| test/gfs_test.csv | atmosphere_0_tcc | 78,840 | 56.523262 | 43.57413 | 0 | 4.1 | 73.1 | 100 | 100 | -0.249982 | -1.749364 | 0 | 0 |
| test/gfs_test.csv | grid_id | 78,840 | 5 | 2.582005 | 1 | 3 | 5 | 7 | 9 | 0 | -1.230002 | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_100_100u | 78,840 | 2.523777 | 3.762073 | -13.797676 | 0.053231 | 2.224679 | 4.305187 | 27.09684 | 0.75783 | 1.68271 | 3,232 | 4.099442 |
| test/gfs_test.csv | heightAboveGround_100_100v | 78,840 | 0.35142 | 2.310266 | -17.248701 | -0.869572 | 0.473655 | 1.541031 | 16.416443 | -0.046931 | 3.456552 | 3,668 | 4.652461 |
| test/gfs_test.csv | heightAboveGround_10_10u | 78,840 | 1.529077 | 2.386495 | -11.45808 | -0.041829 | 1.518143 | 2.832349 | 20.35683 | 0.404161 | 1.48365 | 2,023 | 2.565956 |
| test/gfs_test.csv | heightAboveGround_10_10v | 78,840 | 0.277444 | 1.626097 | -14.282737 | -0.599963 | 0.41764 | 1.134816 | 12.810869 | -0.414162 | 4.984203 | 3,298 | 4.183156 |
| test/gfs_test.csv | heightAboveGround_2_2d | 78,840 | 277.708485 | 12.054525 | 244.29988 | 268.76391 | 278.27055 | 288.606443 | 298.3039 | -0.323446 | -0.919114 | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_2_2r | 78,840 | 70.384098 | 21.166629 | 12.4 | 53.7 | 73.4 | 89.4 | 100 | -0.406407 | -0.932139 | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_2_2sh | 78,840 | 0.007276 | 0.005093 | 0.000382 | 0.002887 | 0.005747 | 0.011569 | 0.020987 | 0.50806 | -1.083729 | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_2_2t | 78,840 | 283.584483 | 10.891838 | 254.37704 | 274.7669 | 284.4236 | 292.58612 | 309.39804 | -0.167141 | -0.851794 | 0 | 0 |
| test/gfs_test.csv | heightAboveGround_80_u | 78,840 | 2.399277 | 3.585652 | -13.479356 | 0.055854 | 2.145956 | 4.106033 | 26.485977 | 0.72932 | 1.67543 | 3,213 | 4.075342 |
| test/gfs_test.csv | heightAboveGround_80_v | 78,840 | 0.343528 | 2.228637 | -17.039068 | -0.842317 | 0.47272 | 1.498981 | 16.00849 | -0.081935 | 3.531447 | 3,564 | 4.520548 |
| test/gfs_test.csv | highCloudLayer_0_hcc | 78,840 | 37.789451 | 43.965047 | 0 | 0 | 5 | 96.7 | 100 | 0.497628 | -1.598384 | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_500_gh | 78,840 | 5,653.418 | 181.390531 | 5,126.276 | 5,518.128 | 5,660.056 | 5,822.333 | 5,940.275 | -0.359935 | -0.754259 | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_500_t | 78,840 | 257.00906 | 9.941452 | 233.13205 | 248.46933 | 256.41743 | 267.010063 | 274.05 | -0.111414 | -1.239932 | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_500_u | 78,840 | 18.141011 | 11.288539 | -16.636639 | 10.245079 | 17.327181 | 25.801369 | 60.581413 | 0.242285 | -0.064895 | 405 | 0.513699 |
| test/gfs_test.csv | isobaricInhPa_500_v | 78,840 | -0.678042 | 8.210741 | -36.321423 | -5.429166 | -0.668149 | 4.333039 | 48.900127 | -0.080254 | 1.12969 | 2,173 | 2.756215 |
| test/gfs_test.csv | isobaricInhPa_700_t | 78,840 | 271.855455 | 10.003106 | 242.21121 | 264.019643 | 272.026505 | 281.0066 | 289.10056 | -0.335166 | -0.924949 | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_700_u | 78,840 | 10.107408 | 7.892896 | -16.867195 | 4.556086 | 9.095457 | 14.979474 | 41.755642 | 0.480556 | 0.078766 | 870 | 1.103501 |
| test/gfs_test.csv | isobaricInhPa_700_v | 78,840 | -1.390391 | 6.426107 | -23.90256 | -5.362219 | -1.224518 | 2.330461 | 38.12293 | 0.221599 | 1.068953 | 1,665 | 2.111872 |
| test/gfs_test.csv | isobaricInhPa_850_r | 78,840 | 61.471518 | 27.225647 | 2.1 | 39.5 | 63.4 | 85.8 | 100 | -0.247217 | -1.105131 | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_850_t | 78,840 | 279.005738 | 10.747561 | 249.67082 | 270.031625 | 279.6026 | 288.693083 | 299.31308 | -0.236063 | -1.029593 | 0 | 0 |
| test/gfs_test.csv | isobaricInhPa_850_u | 78,840 | 6.099331 | 7.326401 | -22.395147 | 1.069753 | 5.292018 | 10.988507 | 37.307537 | 0.318281 | 0.054916 | 546 | 0.692542 |
| test/gfs_test.csv | isobaricInhPa_850_v | 78,840 | -0.401994 | 4.665089 | -20.690973 | -3.116453 | -0.283422 | 2.163917 | 29.321352 | 0.209285 | 1.371485 | 2,874 | 3.645358 |
| test/gfs_test.csv | latitude | 78,840 | 37.25 | 0.204125 | 37 | 37 | 37.25 | 37.5 | 37.5 | 0 | -1.500019 | 0 | 0 |
| test/gfs_test.csv | longitude | 78,840 | 129 | 0.204125 | 128.75 | 128.75 | 129 | 129.25 | 129.25 | 0 | -1.500019 | 0 | 0 |
| test/gfs_test.csv | lowCloudLayer_0_lcc | 78,840 | 26.479291 | 37.6853 | 0 | 0 | 2.3 | 50.9 | 100 | 1.082752 | -0.527814 | 0 | 0 |
| test/gfs_test.csv | meanSea_0_prmsl | 78,840 | 101,572.39 | 793.251698 | 99,139.05 | 100,998.247 | 101,544.15 | 102,216.747 | 103,296.336 | -0.131034 | -0.627902 | 2 | 0.002537 |
| test/gfs_test.csv | middleCloudLayer_0_mcc | 78,840 | 26.271554 | 39.770683 | 0 | 0 | 0 | 55.5 | 100 | 1.077671 | -0.651517 | 0 | 0 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_VRATE | 78,840 | 4,002.092 | 7,367.975 | 0 | 0 | 1,000 | 4,500 | 92,000 | 3.218874 | 14.266087 | 8,960 | 11.364789 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_u | 78,840 | 3.19224 | 5.284796 | -18.947662 | 0.080906 | 1.81646 | 4.771294 | 33.08091 | 1.451655 | 3.020389 | 6,987 | 8.862253 |
| test/gfs_test.csv | planetaryBoundaryLayer_0_v | 78,840 | 0.172532 | 2.772817 | -17.536785 | -0.993932 | 0.318463 | 1.298969 | 23.833246 | 0.33436 | 5.917212 | 7,103 | 9.009386 |
| test/gfs_test.csv | surface_0_dlwrf | 78,840 | 304.022036 | 74.423553 | 143.02937 | 241.18829 | 307.1 | 372.63623 | 453.86545 | -0.146302 | -1.197227 | 0 | 0 |
| test/gfs_test.csv | surface_0_dswrf | 78,840 | 180.689651 | 246.112114 | 0 | 0 | 43.174 | 317.7 | 932.72 | 1.286702 | 0.47247 | 2,292 | 2.907154 |
| test/gfs_test.csv | surface_0_gust | 78,840 | 4.735787 | 4.179852 | 0.200164 | 1.72203 | 3.213524 | 6.213302 | 27.201847 | 1.571983 | 2.139483 | 5,117 | 6.49036 |
| test/gfs_test.csv | surface_0_prate | 78,840 | 0.000034 | 0.000163 | 0 | 0 | 0 | 0.000002 | 0.010547 | 12.375907 | 344.268181 | 16,309 | 20.6862 |
| test/gfs_test.csv | surface_0_sp | 78,840 | 95,381.735 | 2,744.179 | 90,586.336 | 93,154.145 | 94,852.015 | 96,817.035 | 103,071.56 | 0.916314 | 0.08061 | 879 | 1.114916 |
| test/gfs_test.csv | surface_0_tp | 78,840 | 1.846932 | 6.474035 | 0 | 0 | 0 | 0.5 | 98.375 | 6.292831 | 50.836022 | 14,004 | 17.762557 |
| test/ldaps_test.csv | etc_0_VLCDC | 140,112 | 0.165461 | 0.314875 | 0 | 0 | 0 | 0.132996 | 1 | 1.770819 | 1.60126 | 27,165 | 19.388061 |
| test/ldaps_test.csv | etc_0_blh | 140,112 | 357.742367 | 300.0966 | 11.858371 | 160.05241 | 247.936405 | 457.536125 | 3,183.56 | 2.320578 | 7.856266 | 8,559 | 6.108684 |
| test/ldaps_test.csv | etc_0_hcc | 140,112 | 0.257367 | 0.359633 | 0 | 0 | 0 | 0.483246 | 1.000006 | 1.084417 | -0.40039 | 0 | 0 |
| test/ldaps_test.csv | etc_0_lcc | 140,112 | 0.294846 | 0.381948 | 0 | 0 | 0.024841 | 0.629303 | 1 | 0.863233 | -0.927558 | 0 | 0 |
| test/ldaps_test.csv | etc_0_mcc | 140,112 | 0.171981 | 0.323913 | 0 | 0 | 0 | 0.145264 | 1 | 1.718484 | 1.3751 | 26,946 | 19.231757 |
| test/ldaps_test.csv | grid_id | 140,160 | 8.5 | 4.609789 | 1 | 4.75 | 8.5 | 12.25 | 16 | 0 | -1.209412 | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_10_10u | 140,160 | 3.273872 | 4.287097 | -11.614317 | 0.131222 | 3.833808 | 6.413698 | 16.215715 | -0.333362 | -0.541296 | 148 | 0.105594 |
| test/ldaps_test.csv | heightAboveGround_10_10v | 140,160 | 0.495076 | 1.84576 | -9.490688 | -0.550017 | 0.419773 | 1.582559 | 11.067608 | 0.156646 | 1.833494 | 4,283 | 3.055793 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIF | 140,160 | 60.058311 | 83.534915 | 0 | 0 | 6.525391 | 101.66211 | 526.9885 | 1.631055 | 2.619144 | 5,774 | 4.119578 |
| test/ldaps_test.csv | heightAboveGround_2_SWDIR | 140,160 | 126.068405 | 221.702445 | 0 | 0 | 0 | 165.164065 | 949.90625 | 1.78151 | 2.080771 | 19,132 | 13.650114 |
| test/ldaps_test.csv | heightAboveGround_2_dpt | 140,144 | 276.395511 | 12.517853 | 242.87035 | 267.336345 | 277.11472 | 287.6777 | 296.6564 | -0.366284 | -0.902124 | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_2_q | 140,144 | 0.007159 | 0.005127 | 0.000244 | 0.002686 | 0.005615 | 0.011475 | 0.019961 | 0.495697 | -1.1062 | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_2_r | 140,144 | 75.490345 | 20.364468 | 18.229977 | 60.700312 | 79.582335 | 93.351495 | 113.077354 | -0.590949 | -0.697987 | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_2_t | 140,144 | 281.15914 | 11.120384 | 253.04515 | 271.934818 | 282.187055 | 290.82764 | 303.52997 | -0.252175 | -0.987289 | 0 | 0 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmax | 140,112 | 5.533797 | 6.509342 | -16.755417 | 0.962915 | 6.188187 | 10.31969 | 25.433338 | -0.270885 | -0.520328 | 197 | 0.140602 |
| test/ldaps_test.csv | heightAboveGround_50_50MUmin | 140,112 | 4.442302 | 6.530852 | -17.76794 | -0.5854 | 5.194755 | 9.309641 | 23.169157 | -0.269039 | -0.593882 | 84 | 0.059952 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmax | 140,112 | 1.280096 | 2.895416 | -12.326637 | -0.333548 | 1.07952 | 2.846886 | 18.977125 | 0.424155 | 2.320483 | 5,521 | 3.940419 |
| test/ldaps_test.csv | heightAboveGround_50_50MVmin | 140,112 | 0.288788 | 2.817138 | -15.162205 | -1.181016 | 0.249223 | 1.853455 | 16.067867 | -0.009679 | 2.126055 | 6,481 | 4.625585 |
| test/ldaps_test.csv | heightAboveGround_5_XBLWS | 140,160 | 0.028034 | 0.08707 | -0.778204 | -0.004867 | 0.010944 | 0.047501 | 0.713279 | 0.529299 | 13.524834 | 17,230 | 12.293094 |
| test/ldaps_test.csv | heightAboveGround_5_YBLWS | 140,144 | 0.066317 | 0.283381 | -1.900361 | -0.048477 | 0.025819 | 0.15656 | 3.163315 | 1.436508 | 10.546548 | 14,718 | 10.502055 |
| test/ldaps_test.csv | latitude | 140,160 | 37.281931 | 0.013849 | 37.2607 | 37.274375 | 37.2819 | 37.289525 | 37.3032 | 0.003191 | -1.063963 | 0 | 0 |
| test/ldaps_test.csv | longitude | 140,160 | 128.960719 | 0.021274 | 128.9257 | 128.943525 | 128.9607 | 128.97795 | 128.9958 | 0.000316 | -1.000388 | 0 | 0 |
| test/ldaps_test.csv | meanSea_0_prmsl | 140,112 | 101,398.866 | 783.233991 | 98,824.47 | 100,848.78 | 101,381.953 | 102,013.852 | 103,203.39 | -0.192733 | -0.4088 | 309 | 0.220538 |
| test/ldaps_test.csv | surface_0_NDNLW | 140,160 | -66.336849 | 40.210029 | -163.02718 | -98.707989 | -72.541365 | -28.916741 | 11.947685 | 0.165398 | -1.154658 | 0 | 0 |
| test/ldaps_test.csv | surface_0_NDNSW | 140,160 | 156.664769 | 235.084103 | 0 | 0 | 6.006627 | 261.107593 | 916.18195 | 1.45271 | 0.947331 | 9,175 | 6.54609 |
| test/ldaps_test.csv | surface_0_SNOM | 140,112 | 0.016844 | 0.159543 | -0 | 0 | 0 | 0 | 4.614136 | 14.461339 | 245.91278 | 0 | 0 |
| test/ldaps_test.csv | surface_0_avg_lsprate | 140,160 | 0.00003 | 0.000192 | 0 | 0 | 0 | 0 | 0.008273 | 12.161352 | 229.583977 | 0 | 0 |
| test/ldaps_test.csv | surface_0_h | 140,112 | 943.527344 | 43.368749 | 868.8125 | 918.9375 | 946.59375 | 974.0625 | 1,001.25 | -0.324283 | -1.041729 | 0 | 0 |
| test/ldaps_test.csv | surface_0_lsm | 140,112 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| test/ldaps_test.csv | surface_0_lssrate | 140,160 | 0.000008 | 0.000067 | 0 | 0 | 0 | 0 | 0.00154 | 12.699127 | 192.047713 | 0 | 0 |
| test/ldaps_test.csv | surface_0_ncpcp | 140,160 | 0.10609 | 0.692077 | 0 | 0 | 0 | 0 | 29.779297 | 12.163177 | 229.630853 | 0 | 0 |
| test/ldaps_test.csv | surface_0_snol | 140,160 | 0.029026 | 0.240044 | 0 | 0 | 0 | 0 | 5.543701 | 12.707436 | 192.210941 | 0 | 0 |
| test/ldaps_test.csv | surface_0_sp | 140,112 | 90,614.37 | 741.783367 | 87,766.59 | 90,132.285 | 90,621.232 | 91,118.06 | 92,739.15 | -0.17116 | 0.077102 | 1,153 | 0.822913 |
| train/gfs_train.csv | atmosphere_0_tcc | 236,736 | 55.904014 | 43.478858 | 0 | 4.2 | 70.1 | 100 | 100 | -0.221756 | -1.756136 | 0 | 0 |
| train/gfs_train.csv | grid_id | 236,736 | 5 | 2.581994 | 1 | 3 | 5 | 7 | 9 | 0 | -1.230001 | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_100_100u | 236,736 | 2.025617 | 3.597086 | -22.420181 | -0.436756 | 1.761622 | 3.76838 | 27.14945 | 0.822203 | 2.207535 | 8,277 | 3.4963 |
| train/gfs_train.csv | heightAboveGround_100_100v | 236,736 | 0.228532 | 2.449771 | -31.509785 | -0.959666 | 0.356141 | 1.402044 | 20.112705 | -0.290671 | 5.359604 | 14,522 | 6.134259 |
| train/gfs_train.csv | heightAboveGround_10_10u | 236,736 | 1.237709 | 2.312744 | -17.183594 | -0.380477 | 1.246916 | 2.567676 | 17.827602 | 0.403297 | 1.449858 | 4,575 | 1.932532 |
| train/gfs_train.csv | heightAboveGround_10_10v | 236,736 | 0.177562 | 1.732229 | -24.243887 | -0.698129 | 0.315629 | 1.064908 | 15.46408 | -0.681125 | 6.768189 | 11,461 | 4.841258 |
| train/gfs_train.csv | heightAboveGround_2_2d | 236,736 | 277.653883 | 11.748487 | 243.31473 | 268.84185 | 278.521955 | 287.888575 | 298.7771 | -0.292433 | -0.839289 | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_2_2r | 236,736 | 70.328309 | 21.529326 | 11.4 | 53.6 | 73 | 90 | 100 | -0.410261 | -0.923561 | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_2_2sh | 236,736 | 0.007176 | 0.005044 | 0.000341 | 0.002903 | 0.005864 | 0.011029 | 0.020929 | 0.628974 | -0.861481 | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_2_2t | 236,736 | 283.562452 | 10.391815 | 251.10165 | 275.275425 | 284.39356 | 292.304062 | 308.4 | -0.23889 | -0.816362 | 0 | 0 |
| train/gfs_train.csv | heightAboveGround_80_u | 236,736 | 1.928002 | 3.430303 | -21.81385 | -0.428749 | 1.71023 | 3.616421 | 25.659668 | 0.782726 | 2.142316 | 7,951 | 3.358594 |
| train/gfs_train.csv | heightAboveGround_80_v | 236,736 | 0.222579 | 2.362594 | -30.727304 | -0.932746 | 0.354571 | 1.36578 | 19.62365 | -0.329337 | 5.394538 | 14,079 | 5.947131 |
| train/gfs_train.csv | highCloudLayer_0_hcc | 236,736 | 38.629378 | 44.074616 | 0 | 0 | 5.5 | 98.2 | 100 | 0.467873 | -1.624169 | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_500_gh | 236,736 | 5,662.886 | 159.127128 | 5,048.893 | 5,543.992 | 5,680.816 | 5,799.023 | 5,973.196 | -0.428005 | -0.492931 | 389 | 0.164318 |
| train/gfs_train.csv | isobaricInhPa_500_t | 236,736 | 257.251983 | 9.000056 | 229.76521 | 249.731317 | 257.19757 | 265.241725 | 275.67087 | -0.09382 | -1.033833 | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_500_u | 236,736 | 17.260607 | 11.266291 | -23.023571 | 9.12588 | 16.244457 | 24.518635 | 71.96049 | 0.432108 | 0.129158 | 1,946 | 0.822013 |
| train/gfs_train.csv | isobaricInhPa_500_v | 236,736 | -0.888516 | 8.421184 | -40.966904 | -5.642402 | -0.722854 | 4.156798 | 39.756546 | -0.16379 | 1.115776 | 7,275 | 3.073043 |
| train/gfs_train.csv | isobaricInhPa_700_t | 236,736 | 272.142148 | 9.185209 | 242.83926 | 264.754678 | 272.741535 | 280.266518 | 290.17392 | -0.280208 | -0.870828 | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_700_u | 236,736 | 9.160163 | 7.887912 | -27.79229 | 3.747101 | 8.229054 | 13.870282 | 44.007008 | 0.493046 | 0.324697 | 3,605 | 1.522793 |
| train/gfs_train.csv | isobaricInhPa_700_v | 236,736 | -1.256216 | 6.631066 | -29.96846 | -5.327192 | -1.345652 | 2.584509 | 39.108986 | 0.244219 | 0.924555 | 6,240 | 2.635848 |
| train/gfs_train.csv | isobaricInhPa_850_r | 236,736 | 60.351485 | 28.427944 | 1.5 | 35.8 | 62.7 | 86.7 | 100 | -0.204992 | -1.232889 | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_850_t | 236,736 | 279.121712 | 10.177393 | 247.10553 | 270.464252 | 280.13284 | 288.307385 | 297.82675 | -0.296899 | -0.988086 | 0 | 0 |
| train/gfs_train.csv | isobaricInhPa_850_u | 236,736 | 5.229534 | 7.133122 | -29.702671 | 0.419542 | 4.086511 | 9.66566 | 46.64678 | 0.451253 | 0.375913 | 3,035 | 1.282019 |
| train/gfs_train.csv | isobaricInhPa_850_v | 236,736 | -0.420039 | 4.708323 | -40.439484 | -3.015574 | -0.480737 | 1.771457 | 35.66771 | 0.424163 | 3.025863 | 12,992 | 5.48797 |
| train/gfs_train.csv | latitude | 236,736 | 37.25 | 0.204125 | 37 | 37 | 37.25 | 37.5 | 37.5 | 0 | -1.500006 | 0 | 0 |
| train/gfs_train.csv | longitude | 236,736 | 129 | 0.204125 | 128.75 | 128.75 | 129 | 129.25 | 129.25 | 0 | -1.500006 | 0 | 0 |
| train/gfs_train.csv | lowCloudLayer_0_lcc | 236,736 | 26.590305 | 37.834491 | 0 | 0 | 2.1 | 52.1 | 100 | 1.070197 | -0.56293 | 0 | 0 |
| train/gfs_train.csv | meanSea_0_prmsl | 236,736 | 101,635.378 | 785.004268 | 98,440.04 | 101,018.016 | 101,659.535 | 102,234.133 | 103,858.49 | -0.066475 | -0.642752 | 189 | 0.079836 |
| train/gfs_train.csv | middleCloudLayer_0_mcc | 236,736 | 26.962361 | 39.878374 | 0 | 0 | 0 | 59.2 | 100 | 1.03624 | -0.731159 | 0 | 0 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_VRATE | 236,736 | 3,497.9 | 6,531.402 | 0 | 0 | 1,000 | 4,000 | 80,000 | 3.089852 | 12.021607 | 25,698 | 10.85513 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_u | 236,736 | 2.562335 | 4.974871 | -28.42416 | -0.291621 | 1.419858 | 3.72194 | 40.64356 | 1.571963 | 4.144644 | 23,938 | 10.111686 |
| train/gfs_train.csv | planetaryBoundaryLayer_0_v | 236,736 | 0.10943 | 2.992191 | -35.50895 | -1.036442 | 0.216194 | 1.165519 | 29.517832 | 0.127776 | 9.355025 | 25,320 | 10.695458 |
| train/gfs_train.csv | surface_0_dlwrf | 236,736 | 303.381958 | 71.797258 | 128.26337 | 245.36545 | 303.9 | 364.399207 | 447.8611 | -0.069454 | -1.048962 | 0 | 0 |
| train/gfs_train.csv | surface_0_dswrf | 236,736 | 179.505842 | 245.137763 | 0 | 0 | 41 | 313.545 | 938.32 | 1.29556 | 0.512246 | 7,528 | 3.179913 |
| train/gfs_train.csv | surface_0_gust | 236,736 | 4.373325 | 4.031051 | 0.01821 | 1.603751 | 2.907227 | 5.612366 | 30.510489 | 1.753243 | 3.041326 | 18,044 | 7.621992 |
| train/gfs_train.csv | surface_0_prate | 236,736 | 0.000041 | 0.000211 | 0 | 0 | 0 | 0.000002 | 0.009126 | 13.011417 | 259.132701 | 49,897 | 21.077065 |
| train/gfs_train.csv | surface_0_sp | 236,736 | 95,444.077 | 2,745.634 | 90,569.836 | 93,198.124 | 94,948.46 | 96,866.451 | 103,344.33 | 0.92543 | 0.080145 | 2,597 | 1.097003 |
| train/gfs_train.csv | surface_0_tp | 236,736 | 2.326166 | 8.970587 | 0 | 0 | 0 | 0.5625 | 228.625 | 8.789215 | 113.517774 | 44,519 | 18.805336 |
| train/ldaps_train.csv | etc_0_VLCDC | 420,864 | 0.167564 | 0.316205 | 0 | 0 | 0 | 0.142365 | 1 | 1.7419 | 1.493974 | 80,856 | 19.211907 |
| train/ldaps_train.csv | etc_0_blh | 420,864 | 340.230303 | 292.904972 | 11.922593 | 159.40993 | 219.85582 | 428.931245 | 3,850.206 | 2.424788 | 8.40312 | 29,032 | 6.89819 |
| train/ldaps_train.csv | etc_0_hcc | 420,864 | 0.274823 | 0.367792 | 0 | 0 | 0.007965 | 0.542725 | 1.000007 | 0.974111 | -0.652883 | 0 | 0 |
| train/ldaps_train.csv | etc_0_lcc | 420,864 | 0.296137 | 0.383111 | 0 | 0 | 0.020111 | 0.639862 | 1.000003 | 0.848673 | -0.959547 | 0 | 0 |
| train/ldaps_train.csv | etc_0_mcc | 420,864 | 0.181567 | 0.323329 | 0 | 0 | 0 | 0.21875 | 1.000006 | 1.621206 | 1.098512 | 67,884 | 16.129676 |
| train/ldaps_train.csv | grid_id | 420,864 | 8.5 | 4.609778 | 1 | 4.75 | 8.5 | 12.25 | 16 | 0 | -1.209412 | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_10_10u | 420,864 | 2.738978 | 4.332892 | -11.825531 | -1.140903 | 3.284855 | 5.853243 | 18.085985 | -0.086063 | -0.697085 | 57 | 0.013544 |
| train/ldaps_train.csv | heightAboveGround_10_10v | 420,864 | 0.425384 | 1.938003 | -17.344872 | -0.623062 | 0.3505 | 1.452382 | 12.71147 | 0.16705 | 3.350444 | 18,773 | 4.460586 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIF | 420,864 | 60.209888 | 84.062173 | 0 | 0 | 6.487305 | 101.098778 | 541.08984 | 1.620378 | 2.464594 | 18,255 | 4.337506 |
| train/ldaps_train.csv | heightAboveGround_2_SWDIR | 420,864 | 120.160059 | 215.979082 | 0 | 0 | 0 | 145.5625 | 946.0156 | 1.863887 | 2.454049 | 62,978 | 14.963979 |
| train/ldaps_train.csv | heightAboveGround_2_dpt | 420,864 | 276.366933 | 12.000972 | 242.41481 | 267.408322 | 277.67883 | 286.894847 | 297.35178 | -0.320557 | -0.853468 | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_q | 420,864 | 0.007019 | 0.00501 | 0.000244 | 0.002686 | 0.005859 | 0.010904 | 0.021249 | 0.628414 | -0.836914 | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_r | 420,864 | 75.469012 | 20.667001 | 11.018637 | 60.52639 | 79.858127 | 93.691743 | 110.38448 | -0.628311 | -0.619152 | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_2_t | 420,864 | 281.169282 | 10.638699 | 249.69829 | 272.132043 | 282.30503 | 290.511465 | 302.91513 | -0.300274 | -0.923263 | 0 | 0 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmax | 420,864 | 4.696355 | 6.560151 | -17.205416 | -0.714551 | 5.166576 | 9.427945 | 29.133512 | -0.004846 | -0.618924 | 112 | 0.026612 |
| train/ldaps_train.csv | heightAboveGround_50_50MUmin | 420,864 | 3.605434 | 6.554589 | -19.550144 | -2.081963 | 4.165522 | 8.41421 | 27.475353 | -0.015836 | -0.688668 | 124 | 0.029463 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmax | 420,864 | 1.145152 | 3.049756 | -24.694263 | -0.447014 | 0.929294 | 2.536415 | 20.772963 | 0.514455 | 3.872019 | 25,952 | 6.166363 |
| train/ldaps_train.csv | heightAboveGround_50_50MVmin | 420,864 | 0.156378 | 2.954496 | -27.77414 | -1.286951 | 0.140192 | 1.602886 | 18.794529 | -0.029328 | 4.058497 | 26,414 | 6.276137 |
| train/ldaps_train.csv | heightAboveGround_5_XBLWS | 420,864 | 0.024902 | 0.080477 | -0.535396 | -0.006596 | 0.007798 | 0.042192 | 0.957414 | 1.929478 | 12.590248 | 54,190 | 12.875893 |
| train/ldaps_train.csv | heightAboveGround_5_YBLWS | 420,864 | 0.060284 | 0.308396 | -6.486269 | -0.050532 | 0.017298 | 0.127826 | 3.71174 | 0.679074 | 26.227168 | 53,746 | 12.770396 |
| train/ldaps_train.csv | latitude | 420,864 | 37.281931 | 0.013849 | 37.2607 | 37.274375 | 37.2819 | 37.289525 | 37.3032 | 0.003191 | -1.063966 | 0 | 0 |
| train/ldaps_train.csv | longitude | 420,864 | 128.960719 | 0.021274 | 128.9257 | 128.943525 | 128.9607 | 128.97795 | 128.9958 | 0.000316 | -1.000393 | 0 | 0 |
| train/ldaps_train.csv | meanSea_0_prmsl | 420,864 | 101,454.27 | 760.834431 | 98,038.98 | 100,869.555 | 101,514.315 | 102,026.914 | 103,395.07 | -0.17314 | -0.532223 | 550 | 0.130684 |
| train/ldaps_train.csv | surface_0_NDNLW | 420,864 | -65.3811 | 40.768507 | -179.58722 | -97.11307 | -71.69842 | -26.885847 | 18.440361 | 0.06154 | -1.084875 | 0 | 0 |
| train/ldaps_train.csv | surface_0_NDNSW | 420,864 | 151.796905 | 231.127728 | 0 | 0 | 5.863281 | 245.177535 | 948.9419 | 1.525169 | 1.229416 | 31,211 | 7.415935 |
| train/ldaps_train.csv | surface_0_SNOM | 420,864 | 0.013421 | 0.132004 | -0 | 0 | 0 | 0 | 6.606934 | 17.670094 | 409.598865 | 0 | 0 |
| train/ldaps_train.csv | surface_0_avg_lsprate | 420,864 | 0.000044 | 0.000349 | 0 | 0 | 0 | 0 | 0.024531 | 19.494577 | 650.493621 | 0 | 0 |
| train/ldaps_train.csv | surface_0_h | 420,864 | 943.527344 | 43.368646 | 868.8125 | 918.9375 | 946.59375 | 974.0625 | 1,001.25 | -0.32428 | -1.041733 | 0 | 0 |
| train/ldaps_train.csv | surface_0_lsm | 420,864 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| train/ldaps_train.csv | surface_0_lssrate | 420,864 | 0.000007 | 0.000051 | 0 | 0 | 0 | 0 | 0.001586 | 12.428972 | 200.117788 | 0 | 0 |
| train/ldaps_train.csv | surface_0_ncpcp | 420,864 | 0.156966 | 1.255183 | 0 | 0 | 0 | 0 | 88.31055 | 19.501857 | 650.84256 | 0 | 0 |
| train/ldaps_train.csv | surface_0_snol | 420,864 | 0.023242 | 0.181884 | 0 | 0 | 0 | 0 | 5.710938 | 12.457568 | 200.851902 | 0 | 0 |
| train/ldaps_train.csv | surface_0_sp | 420,864 | 90,673.492 | 706.504962 | 87,462.81 | 90,188.234 | 90,662.075 | 91,152.99 | 93,083.13 | 0.009453 | -0.14401 | 1,881 | 0.446938 |
| train/scada_unison_train.csv | unison_wtg01_power_kw10m | 105,056 | 162.753741 | 213.965741 | 0 | 0 | 67 | 289 | 800 | 1.216101 | 0.194 | 19 | 0.018086 |
| train/scada_unison_train.csv | unison_wtg01_wd | 105,056 | -35.304626 | 88.493916 | -179.998004 | -91.519067 | -75.503094 | 51.742465 | 179.99237 | 0.895903 | -0.477455 | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg01_ws | 103,798 | 5.509658 | 3.208078 | 0 | 2.81 | 4.89 | 7.62 | 22.16 | 0.734291 | -0.094678 | 479 | 0.461473 |
| train/scada_unison_train.csv | unison_wtg02_power_kw10m | 103,902 | 145.411022 | 209.503968 | 0 | 0 | 34.5 | 200 | 1,000 | 1.465415 | 0.90107 | 10,682 | 10.280842 |
| train/scada_unison_train.csv | unison_wtg02_wd | 103,910 | -29.873037 | 91.322197 | -179.990774 | -87.437162 | -69.956673 | 62.122249 | 179.991454 | 0.77891 | -0.738812 | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg02_ws | 103,840 | 5.183158 | 3.599933 | 0.15 | 2.5 | 4.1 | 6.87 | 26.52 | 1.313689 | 1.498756 | 4,065 | 3.914676 |
| train/scada_unison_train.csv | unison_wtg03_power_kw10m | 104,912 | 201.070268 | 241.747608 | 0 | 0 | 100 | 395 | 900 | 0.936807 | -0.592543 | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg03_wd | 104,917 | -59.313485 | 100.878594 | -179.984887 | -129.055615 | -118.905479 | 44.249837 | 179.979319 | 0.902252 | -0.79097 | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg03_ws | 104,817 | 5.996033 | 3.896123 | 0.11 | 2.73 | 5.07 | 8.45 | 25.04 | 0.878431 | 0.191627 | 834 | 0.795672 |
| train/scada_unison_train.csv | unison_wtg04_power_kw10m | 105,114 | 196.390233 | 239.218988 | 0 | 0 | 100 | 362.75 | 800 | 0.970619 | -0.500705 | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg04_wd | 105,112 | -38.778134 | 89.279695 | -179.999337 | -96.918874 | -84.511003 | 52.789004 | 179.996811 | 0.850052 | -0.720513 | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg04_ws | 104,884 | 6.049325 | 3.927545 | 0 | 2.77 | 5.19 | 8.45 | 27.98 | 0.946406 | 0.550841 | 1,216 | 1.159376 |
| train/scada_unison_train.csv | unison_wtg05_power_kw10m | 105,122 | 221.543216 | 262.719079 | 0 | 0 | 100 | 416 | 800 | 0.829051 | -0.902068 | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg05_wd | 105,124 | -64.02381 | 104.627197 | -179.997511 | -136.498899 | -126.60257 | 43.444649 | 179.994027 | 0.934929 | -0.773644 | 0 | 0 |
| train/scada_unison_train.csv | unison_wtg05_ws | 103,885 | 6.428533 | 4.172445 | 0 | 2.91 | 5.44 | 9.15 | 32.05 | 0.876073 | 0.199636 | 772 | 0.743129 |
| train/scada_vestas_train.csv | vestas_wtg01_power_kw10m | 157,819 | 195.472066 | 712,805.87 | -42,512,957 | 5 | 102 | 371 | 42,512,957 | -0.000797 | 2,653.118 | 74 | 0.046889 |
| train/scada_vestas_train.csv | vestas_wtg01_wd | 157,819 | 208.283989 | 94.983134 | 0 | 127.069 | 250.753 | 266.448 | 359 | -0.816256 | -0.66019 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg01_ws | 157,819 | 7.047924 | 3.734498 | 0 | 4.234 | 6.5 | 9.559 | 22.8 | 0.578614 | -0.110986 | 950 | 0.601955 |
| train/scada_vestas_train.csv | vestas_wtg02_power_kw10m | 157,819 | 201.289148 | 691,914.947 | -41,959,813 | 9 | 107 | 389 | 41,959,813 | -0.000867 | 2,857.279 | 70 | 0.044355 |
| train/scada_vestas_train.csv | vestas_wtg02_wd | 157,819 | 203.823949 | 87.819822 | 0 | 122.7 | 252.04 | 262.4 | 359 | -0.952544 | -0.622593 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg02_ws | 157,819 | 7.038639 | 3.858768 | 0 | 4.1 | 6.367 | 9.527 | 27.125 | 0.70104 | 0.081101 | 1,288 | 0.816125 |
| train/scada_vestas_train.csv | vestas_wtg03_power_kw10m | 157,819 | 217.457809 | 786,801.149 | -46,559,445 | 12 | 126 | 431 | 46,559,445 | -0.000816 | 2,284.503 | 88 | 0.05576 |
| train/scada_vestas_train.csv | vestas_wtg03_wd | 157,819 | 216.44397 | 87.891724 | 0 | 144.6 | 263.958 | 273.554 | 359 | -0.999448 | -0.490368 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg03_ws | 157,819 | 7.290738 | 3.969916 | 0 | 4.25 | 6.637 | 9.855 | 27.605 | 0.696305 | 0.097466 | 1,379 | 0.873786 |
| train/scada_vestas_train.csv | vestas_wtg04_power_kw10m | 157,819 | 186.633777 | 480,318.381 | -40,642,699 | 2 | 97 | 345 | 40,642,699 | -0.001149 | 4,727.054 | 44 | 0.02788 |
| train/scada_vestas_train.csv | vestas_wtg04_wd | 157,819 | 227.020691 | 95.060312 | 0 | 157.5955 | 277.443 | 290.983 | 359 | -0.9995 | -0.424692 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg04_ws | 157,819 | 6.817297 | 3.564228 | 0 | 4.2 | 6.4 | 9.1 | 26.336 | 0.562808 | 0.168426 | 1,500 | 0.950456 |
| train/scada_vestas_train.csv | vestas_wtg05_power_kw10m | 157,819 | 153.188786 | 456,684.664 | -33,717,814 | 0 | 58 | 268 | 33,717,814 | -0.001023 | 3,277.89 | 72 | 0.045622 |
| train/scada_vestas_train.csv | vestas_wtg05_wd | 157,819 | 194.169266 | 97.067244 | 0 | 98.729 | 245.913 | 266.616 | 359 | -0.741354 | -0.88441 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg05_ws | 157,819 | 6.101548 | 3.463623 | 0 | 3.688 | 5.59 | 8.496 | 22.3 | 0.410242 | -0.234337 | 592 | 0.375113 |
| train/scada_vestas_train.csv | vestas_wtg06_power_kw10m | 157,819 | 158.188127 | 478,422.427 | -34,184,409 | 3 | 72 | 274 | 34,184,409 | -0.001018 | 3,289.108 | 60 | 0.038018 |
| train/scada_vestas_train.csv | vestas_wtg06_wd | 157,819 | 210.295446 | 91.337659 | 0 | 142.722 | 258.279 | 271.092 | 359 | -0.91053 | -0.67404 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg06_ws | 157,819 | 6.400856 | 3.354055 | 0 | 4 | 5.8 | 8.445 | 23.98 | 0.702952 | 0.230765 | 2,026 | 1.283749 |
| train/scada_vestas_train.csv | vestas_wtg07_power_kw10m | 157,819 | 138.37761 | 418,071.326 | -29,770,834 | 0 | 52 | 233 | 29,770,834 | -0.001045 | 3,122.977 | 2,769 | 1.754542 |
| train/scada_vestas_train.csv | vestas_wtg07_wd | 157,819 | 201.246555 | 89.427818 | 0 | 145.757 | 244.71 | 260.545 | 359 | -0.922955 | -0.613116 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg07_ws | 157,819 | 5.977015 | 3.085296 | 0 | 3.727 | 5.363 | 8 | 21.586 | 0.68253 | 0.185357 | 1,413 | 0.895329 |
| train/scada_vestas_train.csv | vestas_wtg08_power_kw10m | 157,819 | 185.373447 | 802,538.179 | -42,301,001 | 5 | 95 | 350 | 42,300,996 | -0.002898 | 1,856.732 | 102 | 0.064631 |
| train/scada_vestas_train.csv | vestas_wtg08_wd | 157,819 | 207.359186 | 87.726355 | 0 | 148.149 | 251.369 | 264.238 | 359 | -0.958909 | -0.525022 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg08_ws | 157,819 | 6.902167 | 3.784046 | 0 | 4.035 | 6.2 | 9.3535 | 27.293 | 0.695399 | 0.070582 | 1,244 | 0.788245 |
| train/scada_vestas_train.csv | vestas_wtg09_power_kw10m | 157,819 | 199.256205 | 580,428.741 | -43,556,999 | 5 | 102 | 385 | 43,556,994 | -0.001096 | 3,720.474 | 52 | 0.032949 |
| train/scada_vestas_train.csv | vestas_wtg09_wd | 157,819 | 215.962082 | 89.559162 | 0 | 146.289 | 258.782 | 276.3 | 359 | -0.955929 | -0.494062 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg09_ws | 157,819 | 7.151594 | 3.895377 | 0 | 4.3 | 6.309 | 9.516 | 26.344 | 0.762086 | 0.117178 | 1,802 | 1.141814 |
| train/scada_vestas_train.csv | vestas_wtg10_power_kw10m | 157,819 | 239.206572 | 842,549.633 | -51,376,454 | 14 | 149 | 499 | 51,376,454 | -0.000821 | 2,810.789 | 68 | 0.043087 |
| train/scada_vestas_train.csv | vestas_wtg10_wd | 157,819 | 205.156555 | 89.121549 | 0 | 137.308 | 244.598 | 265.553 | 359 | -0.920322 | -0.45733 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg10_ws | 157,819 | 7.98552 | 4.531049 | 0 | 4.4 | 7.098 | 11 | 30.75 | 0.669812 | -0.237139 | 558 | 0.35357 |
| train/scada_vestas_train.csv | vestas_wtg11_power_kw10m | 157,819 | 222.979724 | 996,905.723 | -51,770,425 | 9 | 144 | 424 | 51,770,425 | -0.000674 | 1,942.883 | 98 | 0.062096 |
| train/scada_vestas_train.csv | vestas_wtg11_wd | 157,819 | 212.307634 | 91.295913 | 0 | 134.9165 | 258.251 | 274.981 | 359 | -0.930136 | -0.61139 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg11_ws | 157,819 | 7.998195 | 4.625901 | 0 | 4.336 | 7.07 | 11.145 | 31.117 | 0.67411 | -0.216774 | 611 | 0.387152 |
| train/scada_vestas_train.csv | vestas_wtg12_power_kw10m | 157,819 | 198.804162 | 627,046.591 | -41,447,795 | 5 | 94 | 397 | 41,447,795 | -0.000903 | 2,826.454 | 72 | 0.045622 |
| train/scada_vestas_train.csv | vestas_wtg12_wd | 157,819 | 183.331037 | 94.527524 | 0 | 84.5 | 238.22 | 260.2 | 359 | -0.486803 | -1.36727 | 0 | 0 |
| train/scada_vestas_train.csv | vestas_wtg12_ws | 157,819 | 7.203512 | 4.144355 | 0 | 4.1 | 6.227 | 9.891 | 27.504 | 0.751478 | -0.003773 | 1,155 | 0.731851 |
| train/train_labels.csv | kpx_group_1 | 26,200 | 6,621.981 | 6,582.443 | 0 | 549.6 | 4,252.168 | 12,206.905 | 21,275.305 | 0.668287 | -0.930449 | 0 | 0 |
| train/train_labels.csv | kpx_group_2 | 26,201 | 7,076.843 | 7,001.146 | 0 | 549.6 | 4,382.337 | 13,508.589 | 21,362.084 | 0.581333 | -1.165847 | 0 | 0 |
| train/train_labels.csv | kpx_group_3 | 17,538 | 5,563.82 | 6,294.583 | 0 | 159.095 | 2,719.074 | 9,979.579 | 21,130.674 | 0.939719 | -0.438292 | 0 | 0 |

## STEP 9

### 범주형 변수 분석

| Dataset | Column | Reason | Unique Count | Top Values |
| --- | --- | --- | --- | --- |
| test/gfs_test.csv | grid_id | low-cardinality numeric | 9 | 1: 8,760; 2: 8,760; 3: 8,760; 4: 8,760; 5: 8,760; 6: 8,760; 7: 8,760; 8: 8,760; 9: 8,760 |
| test/gfs_test.csv | latitude | low-cardinality numeric | 3 | 37.5: 26,280; 37.25: 26,280; 37.0: 26,280 |
| test/gfs_test.csv | longitude | low-cardinality numeric | 3 | 128.75: 26,280; 129.0: 26,280; 129.25: 26,280 |
| test/ldaps_test.csv | grid_id | low-cardinality numeric | 16 | 1: 8,760; 2: 8,760; 3: 8,760; 4: 8,760; 5: 8,760; 6: 8,760; 7: 8,760; 8: 8,760; 9: 8,760; 10: 8,760 |
| test/ldaps_test.csv | latitude | low-cardinality numeric | 16 | 37.3032: 8,760; 37.3027: 8,760; 37.3022: 8,760; 37.2899: 8,760; 37.2894: 8,760; 37.2888: 8,760; 37.2883: 8,760; 37.2878: 8,760; 37.276: 8,760; 37.2755: 8,760 |
| test/ldaps_test.csv | longitude | low-cardinality numeric | 16 | 128.9443: 8,760; 128.9617: 8,760; 128.979: 8,760; 128.9263: 8,760; 128.9437: 8,760; 128.961: 8,760; 128.9784: 8,760; 128.9958: 8,760; 128.9257: 8,760; 128.943: 8,760 |
| test/ldaps_test.csv | surface_0_lsm | low-cardinality numeric | 1 | 1.0: 140,112; <NA>: 48 |
| test/ldaps_test.csv | surface_0_h | low-cardinality numeric | 16 | 992.625: 8,757; 936.5625: 8,757; 868.8125: 8,757; 926.5: 8,757; 997.625: 8,757; 1001.25: 8,757; 934.4375: 8,757; 869.4375: 8,757; 889.1875: 8,757; 966.6875: 8,757 |
| train/gfs_train.csv | grid_id | low-cardinality numeric | 9 | 1: 26,304; 2: 26,304; 3: 26,304; 4: 26,304; 5: 26,304; 6: 26,304; 7: 26,304; 8: 26,304; 9: 26,304 |
| train/gfs_train.csv | latitude | low-cardinality numeric | 3 | 37.5: 78,912; 37.25: 78,912; 37.0: 78,912 |
| train/gfs_train.csv | longitude | low-cardinality numeric | 3 | 128.75: 78,912; 129.0: 78,912; 129.25: 78,912 |
| train/ldaps_train.csv | grid_id | low-cardinality numeric | 16 | 1: 26,304; 2: 26,304; 3: 26,304; 4: 26,304; 5: 26,304; 6: 26,304; 7: 26,304; 8: 26,304; 9: 26,304; 10: 26,304 |
| train/ldaps_train.csv | latitude | low-cardinality numeric | 16 | 37.3032: 26,304; 37.3027: 26,304; 37.3022: 26,304; 37.2899: 26,304; 37.2894: 26,304; 37.2888: 26,304; 37.2883: 26,304; 37.2878: 26,304; 37.276: 26,304; 37.2755: 26,304 |
| train/ldaps_train.csv | longitude | low-cardinality numeric | 16 | 128.9443: 26,304; 128.9617: 26,304; 128.979: 26,304; 128.9263: 26,304; 128.9437: 26,304; 128.961: 26,304; 128.9784: 26,304; 128.9958: 26,304; 128.9257: 26,304; 128.943: 26,304 |
| train/ldaps_train.csv | surface_0_lsm | low-cardinality numeric | 1 | 1.0: 420,864 |
| train/ldaps_train.csv | surface_0_h | low-cardinality numeric | 16 | 992.625: 26,304; 936.5625: 26,304; 868.8125: 26,304; 926.5: 26,304; 997.625: 26,304; 1001.25: 26,304; 934.4375: 26,304; 869.4375: 26,304; 889.1875: 26,304; 966.6875: 26,304 |

## STEP 10

### Correlation Matrix

- 전체 상관행렬 CSV: `combined_correlation_matrix.csv`

![Correlation Heatmap](correlation_heatmap.svg)

### Target별 상관관계 Top 30

| Target | Feature | Source | Correlation | Abs Correlation |
| --- | --- | --- | --- | --- |
| kpx_group_1 | scada_vestas_vestas_wtg11_ws_max | SCADA(누수 주의) | 0.893887 | 0.893887 |
| kpx_group_1 | scada_vestas_vestas_wtg11_ws_mean | SCADA(누수 주의) | 0.892736 | 0.892736 |
| kpx_group_1 | scada_vestas_vestas_wtg10_ws_max | SCADA(누수 주의) | 0.886951 | 0.886951 |
| kpx_group_1 | scada_vestas_vestas_wtg10_ws_mean | SCADA(누수 주의) | 0.885488 | 0.885488 |
| kpx_group_1 | scada_vestas_vestas_wtg11_ws_min | SCADA(누수 주의) | 0.878146 | 0.878146 |
| kpx_group_1 | scada_vestas_vestas_wtg03_ws_mean | SCADA(누수 주의) | 0.875439 | 0.875439 |
| kpx_group_1 | scada_vestas_vestas_wtg12_ws_max | SCADA(누수 주의) | 0.875186 | 0.875186 |
| kpx_group_1 | scada_vestas_vestas_wtg12_ws_mean | SCADA(누수 주의) | 0.874064 | 0.874064 |
| kpx_group_1 | scada_vestas_vestas_wtg10_ws_min | SCADA(누수 주의) | 0.872972 | 0.872972 |
| kpx_group_1 | scada_vestas_vestas_wtg03_ws_max | SCADA(누수 주의) | 0.870515 | 0.870515 |
| kpx_group_1 | scada_vestas_vestas_wtg02_ws_mean | SCADA(누수 주의) | 0.869549 | 0.869549 |
| kpx_group_1 | scada_vestas_vestas_wtg03_ws_min | SCADA(누수 주의) | 0.86935 | 0.86935 |
| kpx_group_1 | scada_vestas_vestas_wtg08_ws_max | SCADA(누수 주의) | 0.868469 | 0.868469 |
| kpx_group_1 | scada_vestas_vestas_wtg08_ws_mean | SCADA(누수 주의) | 0.866987 | 0.866987 |
| kpx_group_1 | scada_vestas_vestas_wtg01_ws_mean | SCADA(누수 주의) | 0.866308 | 0.866308 |
| kpx_group_1 | scada_unison_unison_wtg05_ws_mean | SCADA(누수 주의) | 0.865202 | 0.865202 |
| kpx_group_1 | scada_unison_unison_wtg05_ws_max | SCADA(누수 주의) | 0.864682 | 0.864682 |
| kpx_group_1 | scada_vestas_vestas_wtg02_ws_max | SCADA(누수 주의) | 0.863597 | 0.863597 |
| kpx_group_1 | scada_vestas_vestas_wtg02_ws_min | SCADA(누수 주의) | 0.863138 | 0.863138 |
| kpx_group_1 | scada_vestas_vestas_wtg01_ws_max | SCADA(누수 주의) | 0.862949 | 0.862949 |
| kpx_group_1 | scada_unison_unison_wtg03_ws_max | SCADA(누수 주의) | 0.862096 | 0.862096 |
| kpx_group_1 | scada_vestas_vestas_wtg12_ws_min | SCADA(누수 주의) | 0.860315 | 0.860315 |
| kpx_group_1 | scada_unison_unison_wtg03_ws_mean | SCADA(누수 주의) | 0.85899 | 0.85899 |
| kpx_group_1 | scada_vestas_vestas_wtg01_ws_min | SCADA(누수 주의) | 0.854964 | 0.854964 |
| kpx_group_1 | scada_unison_unison_wtg05_ws_min | SCADA(누수 주의) | 0.853098 | 0.853098 |
| kpx_group_1 | scada_unison_unison_wtg04_ws_max | SCADA(누수 주의) | 0.850044 | 0.850044 |
| kpx_group_1 | scada_vestas_vestas_wtg08_ws_min | SCADA(누수 주의) | 0.849341 | 0.849341 |
| kpx_group_1 | scada_unison_unison_wtg04_ws_mean | SCADA(누수 주의) | 0.849264 | 0.849264 |
| kpx_group_1 | scada_unison_unison_wtg01_ws_mean | SCADA(누수 주의) | 0.847866 | 0.847866 |
| kpx_group_1 | scada_unison_unison_wtg01_ws_max | SCADA(누수 주의) | 0.846 | 0.846 |
| kpx_group_2 | scada_vestas_vestas_wtg11_ws_mean | SCADA(누수 주의) | 0.911152 | 0.911152 |
| kpx_group_2 | scada_vestas_vestas_wtg11_ws_max | SCADA(누수 주의) | 0.911049 | 0.911049 |
| kpx_group_2 | scada_vestas_vestas_wtg10_ws_max | SCADA(누수 주의) | 0.910831 | 0.910831 |
| kpx_group_2 | scada_vestas_vestas_wtg10_ws_mean | SCADA(누수 주의) | 0.910227 | 0.910227 |
| kpx_group_2 | scada_vestas_vestas_wtg10_ws_min | SCADA(누수 주의) | 0.898044 | 0.898044 |
| kpx_group_2 | scada_vestas_vestas_wtg11_ws_min | SCADA(누수 주의) | 0.897418 | 0.897418 |
| kpx_group_2 | scada_vestas_vestas_wtg12_ws_max | SCADA(누수 주의) | 0.89521 | 0.89521 |
| kpx_group_2 | scada_vestas_vestas_wtg12_ws_mean | SCADA(누수 주의) | 0.894807 | 0.894807 |
| kpx_group_2 | scada_vestas_vestas_wtg08_ws_mean | SCADA(누수 주의) | 0.889371 | 0.889371 |
| kpx_group_2 | scada_vestas_vestas_wtg08_ws_max | SCADA(누수 주의) | 0.888914 | 0.888914 |
| kpx_group_2 | scada_vestas_vestas_wtg12_ws_min | SCADA(누수 주의) | 0.881613 | 0.881613 |
| kpx_group_2 | scada_unison_unison_wtg03_ws_max | SCADA(누수 주의) | 0.880221 | 0.880221 |
| kpx_group_2 | scada_vestas_vestas_wtg09_ws_mean | SCADA(누수 주의) | 0.879701 | 0.879701 |
| kpx_group_2 | scada_unison_unison_wtg03_ws_mean | SCADA(누수 주의) | 0.878972 | 0.878972 |
| kpx_group_2 | scada_vestas_vestas_wtg09_ws_max | SCADA(누수 주의) | 0.877957 | 0.877957 |
| kpx_group_2 | scada_unison_unison_wtg05_ws_mean | SCADA(누수 주의) | 0.875222 | 0.875222 |
| kpx_group_2 | scada_unison_unison_wtg01_ws_mean | SCADA(누수 주의) | 0.8751 | 0.8751 |
| kpx_group_2 | scada_unison_unison_wtg05_ws_max | SCADA(누수 주의) | 0.874468 | 0.874468 |
| kpx_group_2 | scada_vestas_vestas_wtg08_ws_min | SCADA(누수 주의) | 0.873689 | 0.873689 |
| kpx_group_2 | scada_unison_unison_wtg01_ws_max | SCADA(누수 주의) | 0.870339 | 0.870339 |
| kpx_group_2 | scada_vestas_vestas_wtg09_ws_min | SCADA(누수 주의) | 0.869901 | 0.869901 |
| kpx_group_2 | scada_vestas_vestas_wtg03_ws_mean | SCADA(누수 주의) | 0.867778 | 0.867778 |
| kpx_group_2 | scada_unison_unison_wtg04_ws_mean | SCADA(누수 주의) | 0.866773 | 0.866773 |
| kpx_group_2 | scada_unison_unison_wtg04_ws_max | SCADA(누수 주의) | 0.866454 | 0.866454 |
| kpx_group_2 | scada_unison_unison_wtg03_power_kw10m_max | SCADA(누수 주의) | 0.866366 | 0.866366 |
| kpx_group_2 | scada_vestas_vestas_wtg03_ws_max | SCADA(누수 주의) | 0.864717 | 0.864717 |
| kpx_group_2 | scada_unison_unison_wtg05_ws_min | SCADA(누수 주의) | 0.863743 | 0.863743 |
| kpx_group_2 | scada_unison_unison_wtg03_ws_min | SCADA(누수 주의) | 0.863297 | 0.863297 |
| kpx_group_2 | scada_unison_unison_wtg01_ws_min | SCADA(누수 주의) | 0.861391 | 0.861391 |
| kpx_group_2 | scada_vestas_vestas_wtg03_ws_min | SCADA(누수 주의) | 0.859329 | 0.859329 |
| kpx_group_3 | scada_unison_unison_wtg03_power_kw10m_mean | SCADA(누수 주의) | 0.902154 | 0.902154 |
| kpx_group_3 | scada_unison_unison_wtg05_power_kw10m_mean | SCADA(누수 주의) | 0.900511 | 0.900511 |
| kpx_group_3 | scada_unison_unison_wtg04_power_kw10m_mean | SCADA(누수 주의) | 0.898517 | 0.898517 |
| kpx_group_3 | scada_unison_unison_wtg03_power_kw10m_max | SCADA(누수 주의) | 0.897451 | 0.897451 |
| kpx_group_3 | scada_unison_unison_wtg04_power_kw10m_max | SCADA(누수 주의) | 0.887442 | 0.887442 |
| kpx_group_3 | scada_unison_unison_wtg05_power_kw10m_max | SCADA(누수 주의) | 0.886103 | 0.886103 |
| kpx_group_3 | scada_unison_unison_wtg05_ws_mean | SCADA(누수 주의) | 0.883922 | 0.883922 |
| kpx_group_3 | scada_unison_unison_wtg05_ws_max | SCADA(누수 주의) | 0.880217 | 0.880217 |
| kpx_group_3 | scada_unison_unison_wtg03_ws_mean | SCADA(누수 주의) | 0.877417 | 0.877417 |
| kpx_group_3 | scada_unison_unison_wtg05_power_kw10m_min | SCADA(누수 주의) | 0.875624 | 0.875624 |
| kpx_group_3 | scada_unison_unison_wtg05_ws_min | SCADA(누수 주의) | 0.875515 | 0.875515 |
| kpx_group_3 | scada_unison_unison_wtg03_ws_max | SCADA(누수 주의) | 0.875304 | 0.875304 |
| kpx_group_3 | scada_unison_unison_wtg04_ws_mean | SCADA(누수 주의) | 0.872969 | 0.872969 |
| kpx_group_3 | scada_vestas_vestas_wtg12_ws_mean | SCADA(누수 주의) | 0.870912 | 0.870912 |
| kpx_group_3 | scada_vestas_vestas_wtg11_ws_mean | SCADA(누수 주의) | 0.870438 | 0.870438 |
| kpx_group_3 | scada_vestas_vestas_wtg12_ws_max | SCADA(누수 주의) | 0.870281 | 0.870281 |
| kpx_group_3 | scada_vestas_vestas_wtg11_ws_max | SCADA(누수 주의) | 0.869971 | 0.869971 |
| kpx_group_3 | scada_unison_unison_wtg04_ws_max | SCADA(누수 주의) | 0.869931 | 0.869931 |
| kpx_group_3 | scada_vestas_vestas_wtg10_ws_mean | SCADA(누수 주의) | 0.867308 | 0.867308 |
| kpx_group_3 | scada_vestas_vestas_wtg10_ws_max | SCADA(누수 주의) | 0.866444 | 0.866444 |
| kpx_group_3 | scada_unison_unison_wtg03_ws_min | SCADA(누수 주의) | 0.865785 | 0.865785 |
| kpx_group_3 | scada_unison_unison_wtg02_power_kw10m_max | SCADA(누수 주의) | 0.862229 | 0.862229 |
| kpx_group_3 | scada_unison_unison_wtg04_ws_min | SCADA(누수 주의) | 0.860596 | 0.860596 |
| kpx_group_3 | scada_vestas_vestas_wtg12_ws_min | SCADA(누수 주의) | 0.858548 | 0.858548 |
| kpx_group_3 | scada_vestas_vestas_wtg11_ws_min | SCADA(누수 주의) | 0.857289 | 0.857289 |
| kpx_group_3 | scada_vestas_vestas_wtg10_ws_min | SCADA(누수 주의) | 0.856367 | 0.856367 |
| kpx_group_3 | scada_vestas_vestas_wtg08_ws_mean | SCADA(누수 주의) | 0.855358 | 0.855358 |
| kpx_group_3 | scada_vestas_vestas_wtg08_ws_max | SCADA(누수 주의) | 0.854257 | 0.854257 |
| kpx_group_3 | scada_unison_unison_wtg04_power_kw10m_min | SCADA(누수 주의) | 0.854228 | 0.854228 |
| kpx_group_3 | scada_unison_unison_wtg02_power_kw10m_mean | SCADA(누수 주의) | 0.851394 | 0.851394 |

> 주의: SCADA 기반 상관은 데이터 이해용입니다. test에 SCADA 실측이 없으므로 제출용 feature로 직접 사용하면 데이터 누수 가능성이 큽니다.

## STEP 11

### 데이터 연결 구조 분석

| Left Dataset | Right Dataset | Recommended Key | Right Duplicate Key Rows | Expected Grid Count | Times With Missing/Extra Grids | Left Times Missing In Right | Right Times Missing In Left | Merge Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sample_submission.forecast_kst_dtm | test/gfs_test.csv | sample_submission.forecast_kst_dtm = test/gfs_test.csv.forecast_kst_dtm; raw detail key = forecast_kst_dtm + grid_id | 0 | 9 | 0 | 0 | 0 | raw weather는 시간당 격자 여러 행이므로 label에 바로 merge하면 행이 증폭됨. 시간별 격자 집계 또는 grid별 wide 변환 필요. |
| sample_submission.forecast_kst_dtm | test/ldaps_test.csv | sample_submission.forecast_kst_dtm = test/ldaps_test.csv.forecast_kst_dtm; raw detail key = forecast_kst_dtm + grid_id | 0 | 16 | 0 | 0 | 0 | raw weather는 시간당 격자 여러 행이므로 label에 바로 merge하면 행이 증폭됨. 시간별 격자 집계 또는 grid별 wide 변환 필요. |
| train_labels.kst_dtm | train/gfs_train.csv | train_labels.kst_dtm = train/gfs_train.csv.forecast_kst_dtm; raw detail key = forecast_kst_dtm + grid_id | 0 | 9 | 0 | 0 | 0 | raw weather는 시간당 격자 여러 행이므로 label에 바로 merge하면 행이 증폭됨. 시간별 격자 집계 또는 grid별 wide 변환 필요. |
| train_labels.kst_dtm | train/ldaps_train.csv | train_labels.kst_dtm = train/ldaps_train.csv.forecast_kst_dtm; raw detail key = forecast_kst_dtm + grid_id | 0 | 16 | 0 | 0 | 0 | raw weather는 시간당 격자 여러 행이므로 label에 바로 merge하면 행이 증폭됨. 시간별 격자 집계 또는 grid별 wide 변환 필요. |
| train_labels.kst_dtm | train/scada_vestas_train.csv | SCADA kst_dtm를 시간 단위로 집계 후 train_labels.kst_dtm와 결합 | 0 |  |  | 0 | 0 | 10분 SCADA 실측은 test에 제공되지 않으므로 미래 실측 사용은 누수. lag/history 용도만 검토. |
| train_labels.kst_dtm | train/scada_unison_train.csv | SCADA kst_dtm를 시간 단위로 집계 후 train_labels.kst_dtm와 결합 | 0 |  |  | 8,759 | 0 | 10분 SCADA 실측은 test에 제공되지 않으므로 미래 실측 사용은 누수. lag/history 용도만 검토. |
| info.xlsx | SCADA / KPX group | 제작사 + 호기 -> SCADA turbine column; KPX그룹 -> kpx_group_n |  |  |  |  |  | 좌표(Google)는 기상 grid와 직접 키가 없으므로 위경도 기반 nearest grid/거리 feature로 연결하는 것이 자연스러움. |

### 권장 Merge Key 정리

| From | To | Key | Cardinality |
| --- | --- | --- | --- |
| train_labels | ldaps_train/gfs_train | train_labels.kst_dtm = weather.forecast_kst_dtm | 1 시간 : N grids |
| sample_submission | ldaps_test/gfs_test | sample.forecast_kst_dtm = weather.forecast_kst_dtm | 1 시간 : N grids |
| weather raw | weather raw | forecast_kst_dtm + grid_id | unique row 후보 |
| SCADA | train_labels | SCADA kst_dtm를 hourly aggregation 후 kst_dtm | 6개 10분 row -> 1시간 |
| info.xlsx | SCADA/weather | 제작사/호기, KPX그룹, 좌표 기반 nearest grid | metadata -> turbine/grid |

## STEP 12

### Feature Engineering 후보

| Category | Candidate Features | 주의점 |
| --- | --- | --- |
| 시간 Feature | hour, dayofweek, weekend, month, season, dayofyear, weekofyear, holiday 여부, sunrise/sunset 근사, forecast horizon(data_available -> forecast 차이) | 시간은 KST naive로 제공. train/test 동일 규칙으로 생성. |
| Cyclic Encoding | sin/cos(hour), sin/cos(month), sin/cos(dayofyear), sin/cos(wind direction) | 풍향/시각처럼 원형 구조인 변수에 적합. |
| Lag Feature | target lag 1/2/3/6/12/24/48/72/168h, weather lag, SCADA lag, previous-day same-hour | 평가 시점에 실제로 관측 가능한 과거 값만 사용. 미래 target/SCADA 금지. |
| Rolling Mean | target/weather/SCADA rolling mean 3/6/12/24/48/168h | rolling window는 반드시 과거 방향으로 shift 후 계산. |
| Rolling Std | 풍속 변동성, 발전량 변동성, 기온 변동성 rolling std/range/IQR | 급변/불안정한 바람 상태를 표현 가능. |
| 풍속 관련 Feature | sqrt(u^2+v^2), 풍속^2, 풍속^3, cut-in/cut-out threshold flag, hub-height 보정 풍속, gust factor | 발전량은 풍속의 세제곱과 비선형 관계. turbine hub height 고려. |
| 풍향 Encoding | atan2(v,u) 풍향, sin/cos(direction), prevailing wind sector, turbine별 풍향 차이 | 0도와 360도는 가까운 값이므로 직접 수치 사용 주의. |
| 기온 관련 Feature | 기온, 이슬점, 상대습도, 비습, 체감/공기밀도 근사, temperature gradient(850/700/500hPa) | 공기 밀도와 출력 효율에 간접 영향 가능. |
| 기압/대기 안정도 Feature | surface pressure, mean sea pressure, boundary layer height, vertical rate, geopotential height | 풍황 변화와 기상 패턴 설명 변수 후보. |
| 복사/구름/강수 Feature | cloud cover total/low/mid/high, radiation, precipitation, snow flags | 직접 영향보다 기상 상태 proxy로 활용 가능. |
| Grid Aggregation | grid별 mean/std/min/max, nearest grid, distance-weighted average, upwind grid aggregation | raw weather merge 시 행 증폭 방지. info.xlsx 좌표와 결합 가능. |
| Interaction Feature | wind_speed × direction sector, wind_speed × air_density, gust × boundary_layer_height, humidity × temperature | 물리적 의미가 있는 조합부터 우선 검토. |
| 누적 발전량 | daily cumulative generation, 24h cumulative, weekly cumulative, capacity factor cumulative | 동일 일자 미래 시간 누적을 쓰면 누수 가능. 현재 시점 이전 누적만 사용. |
| Moving Average | EWMA, expanding mean by month/hour, same-hour historical moving average | train/test 경계에서 미래 정보가 섞이지 않도록 시계열 split 기준 유지. |
| SCADA Derived | turbine별 평균/합계 power, wind speed, wind direction dispersion, turbine availability proxy, group별 SCADA aggregation | test SCADA 미제공. 실시간 운영 데이터가 별도로 없는 공모전 제출에는 누수 위험이 큼. |
| Capacity / Normalization | target / capacity, group capacity factor, turbine count, installed capacity, hub height, rotor diameter | group별 설비용량이 다르므로 정규화 타깃/피처 분석에 유용. |

## STEP 13

### Data Quality Report

| Area | Severity | Evidence | Recommendation |
| --- | --- | --- | --- |
| 결측 문제 | High | 전체 결측 셀 19,236개, 결측률 10% 이상 컬럼 1개 | 타깃 결측은 학습 제외/기간 분리, weather 결측은 시간·grid 기준 원인 확인 후 보간/indicator 검토. |
| 시간 문제 | Low | 주요 시간 컬럼은 설명서 기준 기간/간격과 대체로 일치하며 timezone 문자열은 없음(KST naive) | 모든 datetime 변환 후 KST 기준을 명시하고, DST 없는 한국 시간으로 feature를 생성. |
| Merge 문제 | High | weather raw 데이터는 forecast_kst_dtm당 grid_id 여러 행이 존재하여 label 시간 1개가 여러 weather row와 매칭됨 | label과 merge 전 grid 집계 또는 wide pivot을 수행. 원본 그대로 merge하면 행 수가 증가. |
| 타깃 범위 | High | 설비용량(kWh/h)을 초과한 target 값 존재 | 단위/집계 기준 확인. 제출 후처리 시 capacity clipping 검토 대상이나 현재 단계에서는 원인 분석만 수행. |
| 데이터 누수 가능성 | High | SCADA 실측은 train에만 제공되고 test에는 제공되지 않음. 평가 기간 실제 발전량/SCADA/사후 보정자료 사용 금지. | 실제 제출용 feature는 예측 시점에 사용 가능한 weather, calendar, 과거 lag만 남기는 검증 규칙 필요. |
| 시간 가용성 | High | weather에는 data_available_kst_dtm가 존재하며 forecast_kst_dtm보다 앞선 예보 가용 시점이 명시됨 | feature 생성 시 forecast 대상 시점이 아니라 data_available 기준으로 사용 가능 여부를 판단. |
| 이상치 문제 | Medium | IQR 기준 outlier는 풍속/강수/발전량 변수에서 자연적으로 다수 발생 가능 | 무조건 제거하지 말고 물리 한계(음수 풍속, capacity 초과, 불가능 습도 등)와 구분. |

### 최종 주의사항

- 예측 대상인 2025년 test 기간에는 실제 발전량 label과 SCADA 실측이 제공되지 않습니다.
- weather는 `data_available_kst_dtm` 기준으로 사용 가능성이 정해지므로, 미래 예보/사후 정보를 섞지 않도록 해야 합니다.
- raw weather는 시간당 여러 grid 행을 갖기 때문에 label과 직접 merge하면 row explosion이 발생합니다.
- `kpx_group_3`는 설명서상 2022년 구간 label이 비어 있을 수 있으므로 기간별 결측 처리가 필요합니다.
- 풍속/강수/발전량 이상치는 실제 기상 급변일 수 있으므로 IQR 기준만으로 제거하면 안 됩니다.
