---
title: "CAREL Modbus从站与数据表示"
source_files: ["0210_Modbus从站配置.md", "0209_Modbus主站配置.md", "0211_Modbus功能码与异常码.md"]
source_type: "manual"
controller_model: ["c.pCO"]
software_version: ["c.design 4.3.x / Manual 1.1"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL Modbus从站与数据表示

## 本文解决的问题

发布从站寄存器，辨认 Index、Size 与在线超时，而不是只确认端口能连通。

## 操作与条件

创建 Modbus Slave 线路，双击进入配置；添加寄存器或线圈，关联 Variable，设置 Index 和 Size。在 Setting 核对 pCO Address、Timeout、Online error 及 Unit Conversion Zone。[0210_Modbus从站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0210_Modbus%E4%BB%8E%E7%AB%99%E9%85%8D%E7%BD%AE.md)

## 关键参数

- 从站帮助要求 REAL 或 32 位整数保持默认 Size=2；改为 1 时按 1tool 模拟量格式转换。
- Hysteresis 表示最小变化量，较小的变化被忽略。
- Timeout 字段单位为 ms，原页默认值表述为 3 秒；超过该时间没有请求，关联 Online error 变量置 1。原字段叫 Online error，描述实际是离线错误：0 为有请求，1 为超时无请求。
- 可导出 .2cf，供 CAREL 上位监控系统使用。

## 数据核对方法

同时确认数据对象、Index 起始约定、寄存器数量、符号、缩放、浮点表示与字序。主站帮助的乘10说明与从站 Size=2 的 REAL 默认规则不能合并成通用编码。功能码支持表按对应平台帮助查阅。[0209_Modbus主站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0209_Modbus%E4%B8%BB%E7%AB%99%E9%85%8D%E7%BD%AE.md)；[0211_Modbus功能码与异常码.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0211_Modbus%E5%8A%9F%E8%83%BD%E7%A0%81%E4%B8%8E%E5%BC%82%E5%B8%B8%E7%A0%81.md)

## 常见错误与待核实

将网络可达当作寄存器正确；把 40001 显示号直接当作线上的起始偏移；只读取一个寄存器就解析 32 位值。具体地址与编码需目标工程、运行时和对端寄存器表共同确认。

## 来源及定位

- [0210_Modbus从站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0210_Modbus%E4%BB%8E%E7%AB%99%E9%85%8D%E7%BD%AE.md)
- [0209_Modbus主站配置.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0209_Modbus%E4%B8%BB%E7%AB%99%E9%85%8D%E7%BD%AE.md)
- [0211_Modbus功能码与异常码.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0211_Modbus%E5%8A%9F%E8%83%BD%E7%A0%81%E4%B8%8E%E5%BC%82%E5%B8%B8%E7%A0%81.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
