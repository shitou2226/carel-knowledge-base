---
title: "CAREL 型号与开发平台"
source_files: ["0401_c.pCO系统用户手册_外文原版.pdf", "0407_旧版pCO系统通用手册_官方中文原版.pdf", "Course_ST_EN_ver_2_05.pptx"]
source_type: "manual"
controller_model: ["c.pCO", "c.pCO mini", "旧 pCO"]
software_version: ["c.pCO 手册 rel.1.8 / 2025-12-15", "本机 c.suite 4.4.22"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL 型号与开发平台

## 本文解决的问题

选软件前先确认控制器完整料号、运行系统和工程来源。品牌相同不等于工程或 OS 通用。

## 已由资料确认

- c.pCO 系列用于 HVAC/R 可编程控制；c.pCO mini 与 Small、Medium、Large、ExtraLarge 的 I/O 和端口按型号区分。[0401_c.pCO系统用户手册_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF06_0401_c.pCO%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC7%E9%A1%B5)
- 手册第 8–9 页分别介绍 STone 与 c.suite，且明确两套操作系统不兼容，需要匹配开发工具选用对应控制器。[0401_c.pCO系统用户手册_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF06_0401_c.pCO%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md#pdf%E7%AC%AC9%E9%A1%B5)
- 旧 pCO 系统手册和 ST 2.05 课件另存为旧平台参考，查具体指令时不能直接替代 c.strategy 帮助。

## 判断步骤

1. 记录铭牌完整料号与 OS 信息。
2. 记录工程扩展名、创建软件及库版本；当前 MCP 的已确认目标为 c.suite 4.4.22 的 c.strategy。
3. 按对应手册查硬件接口，再查该版本软件操作。
4. 不清楚目标 OS 时，先做文档和工程静态分析，保留 Unknown。

## 常见错误与未确认事项

“mini 有以太网”“都是 RS485 所以同一协议”等判断均缺少型号条件。具体控制器料号、固件、端口配置仍需设备信息；这里没有把通用示例参数写成设备默认值。

## 来源及定位

- [0401_c.pCO系统用户手册_外文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF06_0401_c.pCO%E7%B3%BB%E7%BB%9F%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C_%E5%A4%96%E6%96%87%E5%8E%9F%E7%89%88.pdf.md)
- [0407_旧版pCO系统通用手册_官方中文原版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF12_0407_%E6%97%A7%E7%89%88pCO%E7%B3%BB%E7%BB%9F%E9%80%9A%E7%94%A8%E6%89%8B%E5%86%8C_%E5%AE%98%E6%96%B9%E4%B8%AD%E6%96%87%E5%8E%9F%E7%89%88.pdf.md)
- [Course_ST_EN_ver_2_05.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT04_Course_ST_EN_ver_2_05.pptx.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
