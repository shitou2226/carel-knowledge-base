---
title: "CAREL 报警类型与保护逻辑"
source_files: ["0207_报警编辑器与复位方式.md", "报警管理一：概述与项目模板", "报警管理二：导入Chiller控制逻辑", "报警管理三：功能实现"]
source_type: "manual"
controller_model: []
software_version: ["c.strategy 4.3.x / Manual 1.4"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL 报警类型与保护逻辑

## 本文解决的问题

区分报警触发、报警运行时状态和设备输出联锁。

## 报警编辑器

Alarms 添加报警时创建同名全局 ALM 结构变量。Edge 决定 FALSE→TRUE 或 TRUE→FALSE 激活。最多可随报警采样两个变量，Unit Conversion Zone 会影响保存值。[0207_报警编辑器与复位方式.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0207_%E6%8A%A5%E8%AD%A6%E7%BC%96%E8%BE%91%E5%99%A8%E4%B8%8E%E5%A4%8D%E4%BD%8D%E6%96%B9%E5%BC%8F.md)

| 复位类型 | 行为 |
|---|---|
| Manual Reset | 用户复位 |
| Auto Reset | 触发条件改变后自动复位 |
| Auto Reset until Counter | 移动时间窗口内自动复位；触发次数超过 CounterMax 后不再自动复位 |

原页提到 ALARM_RESET_ALL 用于复位全部报警状态。该调用不等于排除报警原因或许可设备重启。

## 实际配置与示例

KALE 的 Alarm_Management/AlarmList.txt 中 NewAlarm_3 设 CounterMax=3、TimeValue=600。这里只保留原数值，时间单位需按相应导入格式/帮助核对，不能默认当作秒。

## 保护链条

根据设备需求分别检查：触发条件 → ALM/日志/界面 → 复位条件 → 输出许可。温控示例中报警置位是否同时阻断输出，要读代码判断，不能只看报警变量名。

## 尚未核实

报警示例工程运行、复位及设备保护均未在本轮实测。视频为机器字幕来源，按对应时间段回看录屏。

## 来源及定位

- [0207_报警编辑器与复位方式.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0207_%E6%8A%A5%E8%AD%A6%E7%BC%96%E8%BE%91%E5%99%A8%E4%B8%8E%E5%A4%8D%E4%BD%8D%E6%96%B9%E5%BC%8F.md)
- [报警管理一：概述与项目模板](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0316_%E6%8A%A5%E8%AD%A6%E7%AE%A1%E7%90%86%E4%B8%80%EF%BC%9A%E6%A6%82%E8%BF%B0%E4%B8%8E%E9%A1%B9%E7%9B%AE%E6%A8%A1%E6%9D%BF.md)
- [报警管理二：导入Chiller控制逻辑](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0317_%E6%8A%A5%E8%AD%A6%E7%AE%A1%E7%90%86%E4%BA%8C%EF%BC%9A%E5%AF%BC%E5%85%A5Chiller%E6%8E%A7%E5%88%B6%E9%80%BB%E8%BE%91.md)
- [报警管理三：功能实现](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0318_%E6%8A%A5%E8%AD%A6%E7%AE%A1%E7%90%86%E4%B8%89%EF%BC%9A%E5%8A%9F%E8%83%BD%E5%AE%9E%E7%8E%B0.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
