---
title: "CAREL 变量声明与发布"
source_files: ["0202_创建变量与快速声明.md", "0201_从基础应用开始创建工程.md"]
source_type: "manual"
controller_model: []
software_version: ["c.strategy 帮助 4.3.x / Manual 1.4", "本机 c.suite 4.4.22"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL 变量声明与发布

## 本文解决的问题

区分“变量已声明”与“变量已发布到 I/O、协议或界面”。

## 操作与示例

在程序语言编辑器打开 Variable Selector，选相应页签，Add 后填写名称与类型。Quick Declaration 使用 Ctrl+Q，可批量设置 Name、DataType、Flags、Min/Max、Comment、Unit Of Measure。

变量表的快速输入示例：

```st
test : BOOL
testArray : INT [0..10]
```

第二条声明有 11 个元素，索引 0 至 10。这是变量表快速声明语法，不能直接把它作为 MCP 的可执行 source 正文。[0202_创建变量与快速声明.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0202_%E5%88%9B%E5%BB%BA%E5%8F%98%E9%87%8F%E4%B8%8E%E5%BF%AB%E9%80%9F%E5%A3%B0%E6%98%8E.md)

在 Published Variables Selector 按用途勾选 Chip I/O、Protocol、User Interface 等列，供 c.design、c.mask 等使用。[0201_从基础应用开始创建工程.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0201_%E4%BB%8E%E5%9F%BA%E7%A1%80%E5%BA%94%E7%94%A8%E5%BC%80%E5%A7%8B%E5%88%9B%E5%BB%BA%E5%B7%A5%E7%A8%8B.md)

## 常见错误与排查

变量能在策略里看到但不能在协议/I/O 选择器中出现：先检查发布标志和该编辑器允许的类型，再检查变量所属资源。数据类型和单位必须同时核对，显示小数位不等于改变通信编码。

## 待核实

每个具体变量是否 Retain、初值、工程作用域和映射地址要读实际工程，不从变量名猜测。

## 来源及定位

- [0202_创建变量与快速声明.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0202_%E5%88%9B%E5%BB%BA%E5%8F%98%E9%87%8F%E4%B8%8E%E5%BF%AB%E9%80%9F%E5%A3%B0%E6%98%8E.md)
- [0201_从基础应用开始创建工程.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0201_%E4%BB%8E%E5%9F%BA%E7%A1%80%E5%BA%94%E7%94%A8%E5%BC%80%E5%A7%8B%E5%88%9B%E5%BB%BA%E5%B7%A5%E7%A8%8B.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
