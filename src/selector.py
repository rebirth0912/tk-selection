"""选品评分与排序模块。"""

from __future__ import annotations

from typing import List

from .analyzer import compute_metrics
from .collector import Product
from .config import Settings, settings


def score(product: Product, settings: Settings = settings) -> float:
    """对单个商品计算综合潜力评分（0~100）。"""
    m = compute_metrics(product)
    growth = min(product.sales_30d / 1000.0, 1.0)  # 简化：销量越高增长分越高
    competition = 1.0 / (1.0 + product.shops_count)  # 在售店铺越少竞争越低

    raw = (
        settings.weights["growth"] * growth
        + settings.weights["engagement"] * min(m["engagement"] * 10, 1.0)
        + settings.weights["conversion"] * min(m["conversion"] * 10, 1.0)
        + settings.weights["competition"] * competition
    )
    return round(raw * 100, 2)


def rank(products: List[Product], top_k: int | None = None, settings: Settings = settings) -> List[tuple[Product, float]]:
    """按综合评分降序排序，返回 (商品, 评分) 列表。"""
    scored = [(p, score(p, settings)) for p in products]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k] if top_k else scored
