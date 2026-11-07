"""命令行入口。"""

from __future__ import annotations

import argparse

from .collector import collect
from .config import settings
from .selector import rank


def main() -> None:
    parser = argparse.ArgumentParser(description="TK选品 - TikTok Shop 选品助手")
    parser.add_argument("--region", default=settings.region, help="目标市场区域")
    parser.add_argument("--top", type=int, default=20, help="输出 Top N 商品")
    args = parser.parse_args()

    settings.region = args.region
    products = collect(settings)
    ranked = rank(products, top_k=args.top, settings=settings)

    if not ranked:
        print("暂无数据。请先在 collector.py 接入真实数据源。")
        return

    for i, (p, s) in enumerate(ranked, 1):
        print(f"{i:>3}. [{s:>6}] {p.title}  (${p.price})")


if __name__ == "__main__":
    main()
