"""
functions 模块初始化文件

此模块包含项目中使用的通用函数和全局变量。
"""

# 导入全局变量
from .global_variables import *

__version__ = "0.1.0"

# 定义 __all__ 来控制 from functions import * 的行为
# 只导出我们定义的变量，不导出 os、Path 等导入的模块
# __all__ = [

# ]
