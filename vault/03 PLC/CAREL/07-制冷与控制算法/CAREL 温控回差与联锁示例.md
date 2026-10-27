---
title: "CAREL 温控回差与联锁示例"
source_files: ["PRG_TemperatureFan源码快照", "0204_功能块的定义与实例.md"]
source_type: "manual"
controller_model: []
software_version: ["本机 c.suite 4.4.22 / bridge 0.2.0"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL 温控回差与联锁示例

## 本文解决的问题

用本轮 MCP 实际读取的 PRG_TemperatureFan 解释回差、参数检查、故障许可与状态优先级。

## 源码的执行链条

1. 第2–7行：首次执行将 Setpoint=25.0、Deadband=2.0、HighLimit=35.0，之后 InitDone=TRUE。
2. 第10–11行：Deadband<=0 或 HighLimit<=Setpoint+Deadband 判参数错误；传感器与参数有效时判断高温报警。
3. 第14–22行：未允许、传感器故障或参数故障时清除 FanDemand；否则温度达到上阈值置 TRUE，降到 Setpoint 置 FALSE，回差区间保持之前状态。
4. 第25行：FanRunCmd 由 Enable、SensorFault、ParamFault 和 FanDemand 共同决定。
5. 第28–40行：状态优先级为传感器故障、参数故障、高温、未允许、运行、空闲。[PRG_TemperatureFan源码快照](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B7%A5%E7%A8%8B%E6%BA%90%E7%A0%81/CAREL%20PRG_TemperatureFan%E6%BA%90%E7%A0%81%E5%BF%AB%E7%85%A7.md#%E6%BA%90%E7%A0%81)

## 关键含义

默认启动阈值 27°C、停止阈值25°C 是从已读源码常量与表达式计算出的示例值。高温报警35°C没有直接加入 FanRunCmd 的禁止条件，因此不能把该例说成“高温后停风机”。

该高温行为是否合理取决于控制目标。这里解释现有代码，不擅自增加保护或改变联锁。

## 变量与验证范围

12个局部变量、类型和注释见源码记录。控制器型号、真实传感器、输出接线、扫描时间均未确认。当前完成的是源码读取与逻辑分析，本轮未编译、仿真或连接实物。

## 来源及定位

- [PRG_TemperatureFan源码快照](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B7%A5%E7%A8%8B%E6%BA%90%E7%A0%81/CAREL%20PRG_TemperatureFan%E6%BA%90%E7%A0%81%E5%BF%AB%E7%85%A7.md)
- [0204_功能块的定义与实例.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0204_%E5%8A%9F%E8%83%BD%E5%9D%97%E7%9A%84%E5%AE%9A%E4%B9%89%E4%B8%8E%E5%AE%9E%E4%BE%8B.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
