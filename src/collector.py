"""数据采集模块（占位实现）。

实际接入时可替换为：
- TikTok Shop 官方 API
- 第三方数据服务（如第三方选品平台）
- 合规的爬虫脚本
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .config import Settings, settings


@dataclass
class Product:
    product_id: str
    title: str
    category: str
    price: float
    # 近 30 天指标（占位字段，接入真实数据后填充）
    views_30d: int = 0
    sales_30d: int = 0
    likes: int = 0
    comments: int = 0
    shops_count: int = 0  # 同类目在售店铺数，用于竞争度估算


def collect(settings: Settings = settings) -> List[Product]:
    """采集目标区域 / 类目的商品数据。

    当前为占位实现，返回空列表，待接入真实数据源。
    """
    # TODO: 接入真实数据源，返回 Product 列表
    return []
