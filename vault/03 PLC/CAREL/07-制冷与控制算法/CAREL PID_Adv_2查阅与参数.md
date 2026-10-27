---
title: "CAREL PID_Adv_2查阅与参数"
source_files: ["PID_Adv_2", "PID_Adv_2 flags table", "PID_Adv"]
source_type: "manual"
controller_model: ["c.pCO family"]
software_version: ["帮助产品信息 c.suite 4.3.x / User manual 1.9.0", "功能要求 c.suite >=2.5.x、OS >=2.1.000"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL PID_Adv_2查阅与参数

## 本文解决的问题

找到本机真实存在的 PID 功能块及参数含义，避免把旧库名或通用整定值当作当前工程配置。

## 官方原文确认

PID_Adv_2 是功能块，计算为达到设定值所需的容量请求。原页 Technical features 的条件为 c.suite ≥2.5.x、c.pCO family、OS ≥2.1.000。原 PID_Adv 页标明已由 PID_Adv_2 取代。[PID_Adv_2](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%85%A8%E6%96%87/CAREL%20%E5%AE%98%E6%96%B9%E5%B8%AE%E5%8A%A9%20c.strategy%20%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2.md#h0530)；[PID_Adv](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%85%A8%E6%96%87/CAREL%20%E5%AE%98%E6%96%B9%E5%B8%AE%E5%8A%A9%20c.strategy%20%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2.md#h0497)

## 关键参数与行为

| 项目 | 原页说明 |
|---|---|
| Ti / Td | 设为 0 分别禁用积分 / 微分 |
| Cycle | 算法执行间隔，单位 ms；小于500ms时行为可能强依赖应用循环时间 |
| En_AntiBump | 启用无扰切换；默认禁用 |
| DeadBand | >0启用；范围为 Setpoint ± DeadBand/2；区间内积分误差冻结 |
| 输出上下限 | 在功能块输入限制输出，避免只在块外截断而丢失相应抗积分饱和处理 |

这些是功能块文档的行为说明，不是现场推荐设定。源页部分段落混用 LimLow/LowLim、LimHigh/HighLim，接线时须以已装库的真实引脚名为准。

## 操作顺序与常见错误

核对工程库版本 → 打开本机 PID_Adv_2 原页 Technical features / Cycle time / Antiwind-up → 核对实际引脚及单位 → 在批准的测试工程验证。不要直接把回差风机示例的 Deadband 与 PID 的中心死区规则互换。

## 尚未核实

当前工程是否使用该块、具体引脚声明、采样周期与闭环整定效果。未给出无依据的 Kp/Ti/Td 生产参数。

## 来源及定位

- [PID_Adv_2](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%85%A8%E6%96%87/CAREL%20%E5%AE%98%E6%96%B9%E5%B8%AE%E5%8A%A9%20c.strategy%20%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2.md#h0530)
- [PID_Adv_2 flags table](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%85%A8%E6%96%87/CAREL%20%E5%AE%98%E6%96%B9%E5%B8%AE%E5%8A%A9%20c.strategy%20%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2.md#h0531)
- [PID_Adv](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%85%A8%E6%96%87/CAREL%20%E5%AE%98%E6%96%B9%E5%B8%AE%E5%8A%A9%20c.strategy%20%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2.md#h0497)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
