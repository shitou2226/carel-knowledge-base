---
title: "CAREL c.pCO端口与硬件查表"
source_files: ["0401_c.pCO系统用户手册_外文原版.pdf", "0402_c.pCOmini安装说明_外文原版.pdf", "0403_c.pCOe扩展模块说明_外文原版.pdf"]
source_type: "manual"
controller_model: ["c.pCO Small–ExtraLarge", "c.pCO mini", "c.pCOe"]
software_version: ["c.pCO 手册 rel.1.8", "c.pCOmini 安装说明 rel.1.7", "c.pCOe 安装说明 rel.1.6"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL c.pCO端口与硬件查表

## 本文解决的问题

根据实际型号找到端口、接线及电气条件的原页，不凭软件截图判断硬件。

## 端口区别

| 对象 | 手册明确列出的例子 | 来源 |
|---|---|---|
| c.pCO Small–ExtraLarge | pLAN J10/J11；内置 BMS2 J25；FieldBus2 J26；BMS1/FBus1 通过相应扩展卡 | PDF 第14页 |
| c.pCO mini | 终端 J3；J6 BMS 仅 Enhanced；J4 FBus 对应 Enhanced、Smart、High End | PDF 第14页 |
| 以太网 | Small–ExtraLarge 为一个或两个端口；mini High End 有一个端口 | PDF 第15页 |

[0401_c.pCO系统用户手册_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF06_0401_c.pCO%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC14%E9%A1%B5)；[0401_c.pCO系统用户手册_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF06_0401_c.pCO%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC15%E9%A1%B5)。上表是该手册列举范围，最终仍以完整产品代码核对。

## 查阅步骤

1. 第 7–9 页确认产品与 OS 分支。
2. 第 14–15 页确认通信接口及 J26 配置条件。
3. 第 29–40 页查看 I/O 接线；第 52 页起核对技术规格。
4. mini 单独查安装说明，c.pCOe 单独查扩展模块说明，保留原图和电源警告。[0402_c.pCOmini安装说明_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF07_0402_c.pCOmini%E5%AE%89%E8%A3%85%E8%AF%B4%E6%98%8E_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC1%E9%A1%B5)；[0403_c.pCOe扩展模块说明_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF08_0403_c.pCOe%E6%89%A9%E5%B1%95%E6%A8%A1%E5%9D%97%E8%AF%B4%E6%98%8E_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC1%E9%A1%B5)

## 常见错误与待核实

Large/ExtraLarge 的 J23 与 J26 在应用管理上属于同一串口线路，但电气端口独立，不能把它们当作两个完全独立的协议线路。该细节见 PDF 第14页。实际供电方式、隔离选项、传感器接法需完整料号后再确定。

## 来源及定位

- [0401_c.pCO系统用户手册_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF06_0401_c.pCO%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md)
- [0402_c.pCOmini安装说明_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF07_0402_c.pCOmini%E5%AE%89%E8%A3%85%E8%AF%B4%E6%98%8E_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md)
- [0403_c.pCOe扩展模块说明_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF08_0403_c.pCOe%E6%89%A9%E5%B1%95%E6%A8%A1%E5%9D%97%E8%AF%B4%E6%98%8E_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
