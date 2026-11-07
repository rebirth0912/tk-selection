"""指标分析模块。"""

from __future__ import annotations

from typing import Dict

from .collector import Product


def compute_metrics(product: Product) -> Dict[str, float]:
    """计算单个商品的核心指标（0~1 归一化前的原始分）。"""
    engagement = (
        (product.likes + product.comments) / product.views_30d
        if product.views_30d > 0
        else 0.0
    )
    conversion = (
        product.sales_30d / product.views_30d
        if product.views_30d > 0
        else 0.0
    )
    return {
        "engagement": engagement,
        "conversion": conversion,
    }
