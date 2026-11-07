"""配置与参数。"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Settings:
    # 目标市场区域，如 US / UK / ID / PH
    region: str = "US"
    # 关注的商品类目
    categories: List[str] = field(default_factory=lambda: ["beauty", "home", "fashion"])
    # 单个类目采集商品数量上限
    top_n: int = 200
    # 数据输出目录
    data_dir: str = "data"

    # 选品评分权重（各项相加应为 1.0）
    weights: dict = field(
        default_factory=lambda: {
            "growth": 0.35,      # 增长趋势
            "engagement": 0.25,  # 互动率
            "conversion": 0.25,  # 转化潜力
            "competition": 0.15, # 竞争度（越低越好）
        }
    )


settings = Settings()
