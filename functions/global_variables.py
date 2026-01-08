"""
全局变量配置文件

存储项目中使用的永久性变量，包括路径、配置参数等。
使用相对路径管理，确保项目可移植性。
"""

import os
from pathlib import Path

# ==================== 项目根目录 ====================
# 获取项目根目录（functions 文件夹的父目录）
PROJECT_ROOT = Path(__file__).parent.parent

# ==================== 数据路径 ====================
DATA_DIR = PROJECT_ROOT / "data"
DATA_OUTPUT_DIR = PROJECT_ROOT / "data_output"
FIGURE_DIR = PROJECT_ROOT / "figure"

# ==================== 常用数据文件路径 ====================
# Shapefile 数据
US_COUNTY_SHP = DATA_DIR / "cb_2018_us_county_500k.shp"
US_STATE_SHP = DATA_DIR / "cb_2018_us_state_500k.shp"
FREQ_POINT_SHP = DATA_DIR / "merge._freq-point.shp"

# 表格数据
DAYU_EXCEL = DATA_DIR / "dayu.xlsx"
DF_WEIGHT_CSV = DATA_DIR / "df_weight.csv"

# ==================== 输出文件路径 ====================
WORLD_SHP_AGG = DATA_OUTPUT_DIR / "world_shp_agg.shp"
WORLD_SHP_AGG_1973_2024 = DATA_OUTPUT_DIR / "world_shp_agg_1973_2024.shp"
WORLD_SHP_AGG_ALL_CSV = DATA_OUTPUT_DIR / "world_shp_agg_all.csv"

# ==================== 配置参数 ====================
# 空间参考系统
DEFAULT_CRS = "EPSG:4326"  # WGS84 地理坐标系

# 图表配置
FIGURE_DPI = 300  # 图表分辨率
FIGURE_FORMAT = "png"  # 默认图表格式
