---
title: "CAREL 旧pCO拓扑与扩展卡图解"
source_files: ["0407_旧版pCO系统通用手册_官方中文原版.pdf"]
source_type: "manual"
controller_model: ["旧pCO1", "旧pCO3", "旧pCOxs"]
software_version: ["旧版pCO系统通用手册；不用于推定c.pCO配置"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL 旧pCO拓扑与扩展卡图解

## 本文解决的问题

将旧pCO手册三个图像页的网络角色变为可检索入口，查卡件时回到对应型号图。

## 型号图的可读信息

| PDF文件页序 | 图中对象和连接角色 | 原图 |
|---|---|---|
| 72 | pCO1；上方pLAN连接终端、控制器、EEV驱动器等；下方将Field-Bus和BMS分区 | [0407_旧版pCO系统通用手册_官方中文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF12_0407_%E6%97%A7%E7%89%88pCO%E7%B3%BB%E7%BB%9F%E9%80%9A%E7%94%A8%E6%89%8B%E5%86%8C_%E5%AE%98%E6%96%B9%E4%B8%AD%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC72%E9%A1%B5) |
| 73 | pCO3；同样区分pLAN、Field-Bus和BMS，另画Synoptic及pCO I/O RS485扩展 | [0407_旧版pCO系统通用手册_官方中文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF12_0407_%E6%97%A7%E7%89%88pCO%E7%B3%BB%E7%BB%9F%E9%80%9A%E7%94%A8%E6%89%8B%E5%86%8C_%E5%AE%98%E6%96%B9%E4%B8%AD%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC73%E9%A1%B5) |
| 74 | pCOxs；pLAN、tLAN、MP-BUS与BMS分别绘出；MP-BUS标注仅PCO1MP0*X0 | [0407_旧版pCO系统通用手册_官方中文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF12_0407_%E6%97%A7%E7%89%88pCO%E7%B3%BB%E7%BB%9F%E9%80%9A%E7%94%A8%E6%89%8B%E5%86%8C_%E5%AE%98%E6%96%B9%E4%B8%AD%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC74%E9%A1%B5) |

第72–73页Field-Bus区域列PCO100FD10（RS485 Modbus/CAREL主站）、PCOS00HBF0（CANbus）、PCO100TLN0（tLAN）；BMS区域列PCOS004850（RS485）、PCO1000BA0（BACnet RS485）、PCO1000WB0（pCOWeb Ethernet/BACnet）、PCO10000F0（LON）等。这是旧图的卡件标注，不代表每块板同时安装这些卡。

## 重要图注

第72–74页tLAN图注均指出pCO I/O tLAN扩展与PLD终端不能同时连接在同一tLAN。第74页有WARNING标识；具体端子、电气限制和可用选件继续查完整料号手册。

## 查阅步骤与常见错误

先确定pCO1/pCO3/pCOxs及完整料号 → 选对应图 → 区分pLAN/Field-Bus/BMS等角色 → 核对实际卡件标签 → 查该卡专用接线和通信配置。不要将BMS的RS485卡视作Field-Bus主站卡，也不要把这些旧产品代码套到c.pCO。

## 尚未核实

本机没有提供三种旧控制器的铭牌和实物卡件；图中未清晰给出的电气参数、最大节点数和通信速率保持未知。


## 来源及定位

- [0407_旧版pCO系统通用手册_官方中文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF12_0407_%E6%97%A7%E7%89%88pCO%E7%B3%BB%E7%BB%9F%E9%80%9A%E7%94%A8%E6%89%8B%E5%86%8C_%E5%AE%98%E6%96%B9%E4%B8%AD%E6%96%87%E5%8E%9F%E7%89%88.pdf.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
