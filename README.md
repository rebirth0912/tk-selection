# tk选品 (TikTok Shop 选品助手)

从 TikTok / 抖音等平台发现、分析并筛选有潜力的商品，辅助选品决策。

## 功能规划

- **数据采集 (collector)**：拉取商品 / 视频 / 达人数据
- **数据分析 (analyzer)**：计算增长、互动、转化等核心指标
- **选品评分 (selector)**：多维度打分与排序，输出潜力榜单
- **配置 (config)**：区域、品类、API Key 等可配置项

## 目录结构

```
tk-selection/
├── src/
│   ├── config.py        # 配置与参数
│   ├── collector.py     # 数据采集
│   ├── analyzer.py      # 指标分析
│   ├── selector.py      # 选品评分排序
│   └── main.py          # 命令行入口
├── data/                # 原始数据 / 中间结果
├── tests/               # 单元测试
├── requirements.txt
└── .gitignore
```

## 快速开始

```bash
pip install -r requirements.txt
python -m src.main --help
```

## 状态

脚手架已初始化，各模块为可运行的占位实现，待按实际数据源（TikTok API / 爬虫 / 第三方数据服务）填充。
