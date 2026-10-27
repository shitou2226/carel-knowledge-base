---
title: "CAREL LOG记录与导出"
source_files: ["0214_LOG日志编辑器.md", "0217_日志导出官方示例.md"]
source_type: "manual"
controller_model: []
software_version: ["c.design 帮助 4.3.x / Manual 1.1"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL LOG记录与导出

## 本文解决的问题

按采样或事件建立日志，区分日志定义与实际导出的数据。

## 配置与关键字段

LOG 编辑器 New 创建定义，Enabled 控制启用，Type 选择周期或事件。周期日志的 Parameter Settings 配置采样持续时间、频率和停止/重启事件；动态采样与固定采样有互斥条件。事件日志可按变化或报警事件记录。Log Variable Settings 选择记录变量。[0214_LOG日志编辑器.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0214_LOG%E6%97%A5%E5%BF%97%E7%BC%96%E8%BE%91%E5%99%A8.md)

Unit Conversion Zone 影响记录的单位换算。Export 导出日志定义，Import 向已有列表添加定义；这两个操作不等同于导出运行时数据。实际数据导出的官方示例见 [0217_日志导出官方示例.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0217_%E6%97%A5%E5%BF%97%E5%AF%BC%E5%87%BA%E5%AE%98%E6%96%B9%E7%A4%BA%E4%BE%8B.md)。

## 常见错误

没有启用定义、未选变量、动态采样未设置记录数量、把导出定义当成已有历史数据。先检查配置和触发条件，再检查目标介质和导出功能块返回值。

## 尚未核实

具体日志容量、写入周期对介质的影响、设备端导出结果，本轮未进行设备验证。

## 来源及定位

- [0214_LOG日志编辑器.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0214_LOG%E6%97%A5%E5%BF%97%E7%BC%96%E8%BE%91%E5%99%A8.md)
- [0217_日志导出官方示例.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0217_%E6%97%A5%E5%BF%97%E5%AF%BC%E5%87%BA%E5%AE%98%E6%96%B9%E7%A4%BA%E4%BE%8B.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
