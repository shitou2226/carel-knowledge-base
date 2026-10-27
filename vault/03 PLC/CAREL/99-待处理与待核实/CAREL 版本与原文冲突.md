---
title: "CAREL 版本与原文冲突"
source_files: []
source_type: "other"
controller_model: []
software_version: []
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL 版本与原文冲突

## c.suite 与 STone

c.pCO 手册第8–9页覆盖两种开发体系且说明 OS 不兼容；现有 MCP 连接 c.suite 4.4.22。保留新硬件手册，但软件步骤以目标系统分支为准。[0401_c.pCO系统用户手册_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF06_0401_c.pCO%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC9%E9%A1%B5)

## I/O 脚注

Config_U_IO.htm 第461行的脚注与同页固定方向类型表存在适用条件不完整问题。当前编号译文第78行已明确指出矛盾，旧 0703 复核建议属于历史记录，不能再写成“当前译文仍增加通过变量设置的结论”。本轮对照了源文件，实际界面行为仍待测。[0212_I_O通道配置与错误码.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0212_I_O%E9%80%9A%E9%81%93%E9%85%8D%E7%BD%AE%E4%B8%8E%E9%94%99%E8%AF%AF%E7%A0%81.md)

## 函数能否调用 FB

Functions_definition 明确限制函数调用 FB；Function_Blocks_definition 的“任何 POU”较宽泛。保留两者来源，函数场景按专门说明，不擅自把宽泛表述当作兼容性保证。[0203_函数的定义与调用规则.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0203_%E5%87%BD%E6%95%B0%E7%9A%84%E5%AE%9A%E4%B9%89%E4%B8%8E%E8%B0%83%E7%94%A8%E8%A7%84%E5%88%99.md)；[0204_功能块的定义与实例.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0204_%E5%8A%9F%E8%83%BD%E5%9D%97%E7%9A%84%E5%AE%9A%E4%B9%89%E4%B8%8E%E5%AE%9E%E4%BE%8B.md)

## 旧 ST 课件第56、85页

原 PPT 第56页把 REPEAT 的继续/退出真假条件写成与现有译本不同的规则，第85页 Debug 优化开关的执行时间说明也存在疑点。已保留原 PPT 直接读取、截图和中文 PDF。不要根据这两页编写新控制器循环或给出性能结论，先查对应版本语言手册或测试工程。[Course_ST_EN_ver_2_05.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT04_Course_ST_EN_ver_2_05.pptx.md#%E5%B9%BB%E7%81%AF%E7%89%8756)；[Course_ST_EN_ver_2_05.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT04_Course_ST_EN_ver_2_05.pptx.md#%E5%B9%BB%E7%81%AF%E7%89%8785)；[0101_ST结构化文本课程_2.05_中文版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF02_0101_ST%E7%BB%93%E6%9E%84%E5%8C%96%E6%96%87%E6%9C%AC%E8%AF%BE%E7%A8%8B_2.05_%E4%B8%AD%E6%96%87%E7%89%88.pdf.md#pdf%E7%AC%AC56%E9%A1%B5)

## Modbus 编码与算术笔误

主站帮助的实数乘10说明和从站 Size=2 默认表示保留各自适用条件，不合成统一规则。异常合成示例中的 0xFF 与 256 不一致，已明确标记算术核对及有符号解释。[0209_Modbus主站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0209_Modbus%E4%B8%BB%E7%AB%99%E9%85%8D%E7%BD%AE.md)；[0210_Modbus从站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0210_Modbus%E4%BB%8E%E7%AB%99%E9%85%8D%E7%BD%AE.md)

## PID 引脚名

PID_Adv_2 原文段落有 LimLow/LowLim、LimHigh/HighLim 写法差异。连线时查实际库接口；旧 PID_Adv 已标 Deprecated。[PID_Adv_2](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%85%A8%E6%96%87/CAREL%20%E5%AE%98%E6%96%B9%E5%B8%AE%E5%8A%A9%20c.strategy%20%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2.md#h0530)；[PID_Adv](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%85%A8%E6%96%87/CAREL%20%E5%AE%98%E6%96%B9%E5%B8%AE%E5%8A%A9%20c.strategy%20%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2.md#h0497)
