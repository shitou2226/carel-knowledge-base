---
title: "CAREL pGD1的NO LINK排查"
source_files: ["0405_pGD1图形显示终端_官方中英原版.pdf", "0406_pGDe图形显示终端_官方中英原版.pdf"]
source_type: "manual"
controller_model: ["PGD1000F*0 / PGD1000W*0"]
software_version: ["+05C001050 rel.1.2 / 2008-10-13"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL pGD1的NO LINK排查

## 本文解决的问题

区分 pGD1 提示 NO LINK 与 I/O board fault 的含义，并找到终端地址设置原图。

## 资料记载

原厂 pGD1 PDF 第1页“故障信号”区分：

- 终端检测到所连接 pCO 主板掉线，显示 I/O 板 xx fault。
- 终端未收到网络信号，显示 NO LINK。[0405_pGD1图形显示终端_官方中英原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF10_0405_pGD1%E5%9B%BE%E5%BD%A2%E6%98%BE%E7%A4%BA%E7%BB%88%E7%AB%AF_%E5%AE%98%E6%96%B9%E4%B8%AD%E8%8B%B1%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC1%E9%A1%B5)

同页有地址配置、专用/共享终端说明；第2页有网络状态、固件版本、技术参数。

## 建议排查顺序

先记录提示原文和终端型号，核查供电与线缆，再核查终端地址、关联主板及专用/共享分配。按原 PDF 图示辨认组合按键和确认步骤，避免通过纯文本抽取的符号操作。

这是基于资料的排查顺序；本轮没有实际故障设备或修复结果。

## 常见错误与待核实

不能将 pGD1 按键组合直接套到 pGDe；不能把 NO LINK 直接判成 PLC 程序丢失。现场线缆、地址和主板运行状态仍需读取。

## 来源及定位

- [0405_pGD1图形显示终端_官方中英原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF10_0405_pGD1%E5%9B%BE%E5%BD%A2%E6%98%BE%E7%A4%BA%E7%BB%88%E7%AB%AF_%E5%AE%98%E6%96%B9%E4%B8%AD%E8%8B%B1%E5%8E%9F%E7%89%88.pdf.md)
- [0406_pGDe图形显示终端_官方中英原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF11_0406_pGDe%E5%9B%BE%E5%BD%A2%E6%98%BE%E7%A4%BA%E7%BB%88%E7%AB%AF_%E5%AE%98%E6%96%B9%E4%B8%AD%E8%8B%B1%E5%8E%9F%E7%89%88.pdf.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
