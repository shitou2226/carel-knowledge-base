---
title: "CAREL Modbus故障定位"
source_files: ["0209_Modbus主站配置.md", "0211_Modbus功能码与异常码.md", "0210_Modbus从站配置.md"]
source_type: "manual"
controller_model: []
software_version: ["c.design 4.3.x / Manual 1.1"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL Modbus故障定位

## 本文解决的问题

按主站实际状态区分未查询、无应答、坏报文与协议异常，避免一直改同一个 Timeout。

## 先读 Device Error

| 值 | 官方含义 | 下一步建议 |
|---|---|---|
| 0 | 正常应答 | 再核对数据值、编码和映射 |
| 1 | 无应答，离线 | 检查端口/网络、站号、对端运行状态、超时与重试 |
| 2 | 应答报文无效 | 对照协议、帧及串口配置检查 |
| 3 | 对端返回异常 | 读取 Device ErrorCode，解析功能码及异常码 |
| 4 | 尚未查询 | 检查线路、设备和数据点是否启用及轮询是否执行 |

状态定义来自原帮助，最后一列是据状态归纳的排查建议。[0209_Modbus主站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0209_Modbus%E4%B8%BB%E7%AB%99%E9%85%8D%E7%BD%AE.md)

## 超时与恢复链条

请求 → 无应答 → 按 Retries 重试，每次等 Timeout → 仍失败标离线 → 每隔 Detection Interval 再探测。不要将 Polling Delay、Command Delay 与 Detection Timeout 当成同一参数。

## 异常码及原文笔误

从站页列出 1 非法功能、2 非法地址、3 非法值。主站页的组合值按 exception_function × 256 + exception_error 解释。例如 0x81 和 2 组成 0x8102，即无符号 33026，按有符号16位解释为 -32510。

原页把十六进制乘数写为 0xFF，同时十进制用了 256；两者不一致。保留原文，计算采用 0x100=256，并明确有符号转换。这是算术核对，不是声称原手册已经修订。[0211_Modbus功能码与异常码.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0211_Modbus%E5%8A%9F%E8%83%BD%E7%A0%81%E4%B8%8E%E5%BC%82%E5%B8%B8%E7%A0%81.md)

## 尚未确认

本轮未抓包或连接现场设备；任何具体波特率、设备站号和超时数值需目标配置。

## 来源及定位

- [0209_Modbus主站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0209_Modbus%E4%B8%BB%E7%AB%99%E9%85%8D%E7%BD%AE.md)
- [0211_Modbus功能码与异常码.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0211_Modbus%E5%8A%9F%E8%83%BD%E7%A0%81%E4%B8%8E%E5%BC%82%E5%B8%B8%E7%A0%81.md)
- [0210_Modbus从站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0210_Modbus%E4%BB%8E%E7%AB%99%E9%85%8D%E7%BD%AE.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
