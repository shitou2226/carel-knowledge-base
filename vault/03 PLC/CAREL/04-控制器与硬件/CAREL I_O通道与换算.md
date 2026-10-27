---
title: "CAREL I_O通道与换算"
source_files: ["0212_I_O通道配置与错误码.md", "0401_c.pCO系统用户手册_外文原版.pdf"]
source_type: "manual"
controller_model: ["c.pCO 系列，按通道能力核对"]
software_version: ["c.design 帮助 4.3.x / Manual 1.1", "本机 c.suite 4.4.22"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL I_O通道与换算

## 本文解决的问题

找到输入方向、探头类型、量程及错误变量，避免采到错误值后只改程序。

## 配置步骤

1. 在 c.strategy 发布变量的 Chip I/O。
2. 在 c.design 双击 U1、U2 等通道，关联 Variable。
3. 按实际接线选择 Channel Direction、Channel Type，核对通道支持能力。
4. 有源探头需要按资料定义比例换算 Min、Max；4…20 mA、0…10 V 等不可仅凭同为模拟量就互换。
5. 关联 Error Variable，再检查通道值与错误状态。[0212_I_O通道配置与错误码.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0212_I_O%E9%80%9A%E9%81%93%E9%85%8D%E7%BD%AE%E4%B8%8E%E9%94%99%E8%AF%AF%E7%A0%81.md)

## 关键错误码

| 值 | 本页含义 |
|---|---|
| 10 | 无错误 |
| 0 | 探头未使用 |
| -1 / -2 | 无源探头未连接 / 短路 |
| -3 / -4 | 有源探头高于上限 / 低于下限 |
| -5 | 通道配置错误 |
| -6 | 通道已占用 |
| -8 | 比例换算系数不正确；包括需要 Min/Max 却未配置的情况 |
| -9 | 当前通道不支持该配置 |

不要把 0 当成此页的“正常”状态。

## 原文差异与待核实

Config_U_IO.htm 脚注称 Channel Direction 必须为 Link to variable 才能设置 Channel Type，但同页固定方向表又列出可选类型。当前编号译文已把这个矛盾标出；历史复核建议不等于当前译文仍漏改。固定方向的真实 UI 行为留待对应版本实测。具体传感器工程量范围、通道能力与精度按实际型号和探头数据表核对。

## 来源及定位

- [0212_I_O通道配置与错误码.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0212_I_O%E9%80%9A%E9%81%93%E9%85%8D%E7%BD%AE%E4%B8%8E%E9%94%99%E8%AF%AF%E7%A0%81.md)
- [0401_c.pCO系统用户手册_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF06_0401_c.pCO%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
