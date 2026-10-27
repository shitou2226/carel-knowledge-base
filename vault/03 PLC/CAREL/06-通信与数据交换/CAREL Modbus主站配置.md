---
title: "CAREL Modbus主站配置"
source_files: ["0209_Modbus主站配置.md", "0215_Modbus主从通信官方示例.md", "Modbus主站协议配置"]
source_type: "manual"
controller_model: ["c.pCO 系列；具体端口按型号"]
software_version: ["c.design 4.3.x / Manual 1.1", "官方主从示例要求 c.suite >=4.2.9、OS >=4.3.000"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL Modbus主站配置

## 本文解决的问题

在 c.design 配置主站设备、变量映射与轮询，区分线路参数与设备参数。

## 操作步骤

1. 建立对应端口的协议线路，双击线路。
2. 在 Network 用 ADD 添加从站，设置设备地址或以太网主机名/IP；使用主机名需要网络名称解析。
3. 在 Variables 选择 Holding Register、Input Register、Coil 或 Discrete Input，配置 Index、Size、关联 Variable 和 Access。
4. 在 Device Setting 设置 Timeout、Detection Timeout、Command Delay，按目标设备数据表核对。
5. 在 Line Properties 设置 Retries、Detection Interval、Polling Delay；关联设备状态和轮询统计以便诊断。[0209_Modbus主站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0209_Modbus%E4%B8%BB%E7%AB%99%E9%85%8D%E7%BD%AE.md)

## 数据与写入模式

Size=1 占 16 位寄存器，Size=2 占两个连续寄存器。当前帮助的模拟量说明包含实数乘 10 的传输方式，不能把它推广成所有 REAL 都是 IEEE754 或所有设备都乘 10。

Access 的 WriteOnline 模式会在设备恢复在线时用应用值写入从站；选用前先明确谁持有有效参数。只读采集优先选择相符的 NoWrite 模式，具体设计以需求为准。

## 排查与来源条件

先看 Device Error，再看 ErrorCode、Polls ID 和 Errors ID。官方主从示例用以太网，通过从站取反布尔量检查通信有效性；迁到 RS485 需要可用端口及对应配置。[0215_Modbus主从通信官方示例.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0215_Modbus%E4%B8%BB%E4%BB%8E%E9%80%9A%E4%BF%A1%E5%AE%98%E6%96%B9%E7%A4%BA%E4%BE%8B.md)

## 待核实

实际从站寄存器表、字/字节顺序、波特率、站号、网络地址与运行时版本均需读目标配置，不用教程数值填默认值。

## 来源及定位

- [0209_Modbus主站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0209_Modbus%E4%B8%BB%E7%AB%99%E9%85%8D%E7%BD%AE.md)
- [0215_Modbus主从通信官方示例.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0215_Modbus%E4%B8%BB%E4%BB%8E%E9%80%9A%E4%BF%A1%E5%AE%98%E6%96%B9%E7%A4%BA%E4%BE%8B.md)
- [Modbus主站协议配置](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0320_Modbus%E4%B8%BB%E7%AB%99%E5%8D%8F%E8%AE%AE%E9%85%8D%E7%BD%AE.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
