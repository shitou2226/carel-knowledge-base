---
title: "CAREL MCP只读工程分析案例"
source_files: ["PRG_TemperatureFan源码快照", "TemperatureFanDemo"]
source_type: "manual"
controller_model: []
software_version: ["c.suite 4.4.22 / bridge 0.2.0"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL MCP只读工程分析案例

## 问题与环境

验证现有 MCP 能否读取真实工程，而不改写程序。第一阶段读取的是 McpSimProbe；本轮重新查询时当前 IDE 已打开 TemperatureFanDemo，使用本轮返回的 pid 和 full_name。

## 实际排查



## 实际修改与结果

工程修改：无。仿真启动/写入：无。只读查询成功，源码与变量快照已保存在本知识库。源码哈希 ea0cef08c53217752d6286e494cd0210e662118859f983d54131a542a4764444。[PRG_TemperatureFan源码快照](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B7%A5%E7%A8%8B%E6%BA%90%E7%A0%81/CAREL%20PRG_TemperatureFan%E6%BA%90%E7%A0%81%E5%BF%AB%E7%85%A7.md)

## 适用范围与恢复路径

这是本地 IDE 工程的只读读取验证，不是程序功能或设备运行验收。原工程保持在 <本地路径>；完整工具能力及确认流程见知识库首页中的 MCP 说明。

## 未核实

其他未打开工程的程序体、图形编辑、物理下载及现场行为。

## 来源及定位

- [PRG_TemperatureFan源码快照](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B7%A5%E7%A8%8B%E6%BA%90%E7%A0%81/CAREL%20PRG_TemperatureFan%E6%BA%90%E7%A0%81%E5%BF%AB%E7%85%A7.md)
- [TemperatureFanDemo](../05-%E7%BC%96%E7%A8%8B%E4%B8%8E%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/PROJECT06_TemperatureFanDemo%E5%B7%A5%E7%A8%8B%E7%BB%93%E6%9E%84.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
