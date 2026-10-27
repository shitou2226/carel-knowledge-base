---
title: "CAREL DEV默认值与参数导入导出"
source_files: ["0213_DEV默认参数编辑器.md", "0216_参数导入导出官方示例.md"]
source_type: "manual"
controller_model: ["c.pCO 系列"]
software_version: ["DEV 帮助 4.3.x / Manual 1.1", "导入导出示例要求 c.suite >=4.0.36、OS >=3.0.001"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL DEV默认值与参数导入导出

## 本文解决的问题

区分策略初值、DEV 的 User value 和导出文件，解释参数导出时为什么缺少变量。

## 关键条件与操作

DEV 编辑器只显示在 c.strategy 勾选 Dev 的变量。Initial value 与策略的初值列相同，只读；User value 为 RETAIN 变量默认值。导入 TXT 按变量名称匹配。[0213_DEV默认参数编辑器.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0213_DEV%E9%BB%98%E8%AE%A4%E5%8F%82%E6%95%B0%E7%BC%96%E8%BE%91%E5%99%A8.md)

官方 IMPORT_PARAMS / EXPORT_PARAMS 示例只处理具有 User value 的 DEV 变量；示例在 USB 或内部 Flash 的 EXPORT_xx.txt 文件间导入导出。Path 可为空；填入时必须与实际路径一致。[0216_参数导入导出官方示例.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0216_%E5%8F%82%E6%95%B0%E5%AF%BC%E5%85%A5%E5%AF%BC%E5%87%BA%E5%AE%98%E6%96%B9%E7%A4%BA%E4%BE%8B.md)

## 数据类型与版本

EXPORT_PARAMS 将 BYTE、WORD、DWORD 对应输出为 USINT、UINT、UDINT。源页 UDINTS 的笔误保留勘误说明，不创建不存在的数据类型。从 4.3.x 起可设置 STRING 的 DEV 值。

## 排查顺序

先查变量是否具备 Dev、RETAIN、User value 条件，再查变量名称、文件路径及返回 ERR_xxx。具体错误码需检索所用功能块帮助；不要用任意 TXT 覆盖设备参数。

## 尚未核实

本轮未导入参数、改写工程或设备配置；现有 ImpExpParameters 文件保持原样。

## 来源及定位

- [0213_DEV默认参数编辑器.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0213_DEV%E9%BB%98%E8%AE%A4%E5%8F%82%E6%95%B0%E7%BC%96%E8%BE%91%E5%99%A8.md)
- [0216_参数导入导出官方示例.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0216_%E5%8F%82%E6%95%B0%E5%AF%BC%E5%85%A5%E5%AF%BC%E5%87%BA%E5%AE%98%E6%96%B9%E7%A4%BA%E4%BE%8B.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
