---
title: "CAREL 工程创建与保存"
source_files: ["0201_从基础应用开始创建工程.md", "c.suite 4.4.22 安装步骤.docx", "c.suite 4.2.9 安装步骤.docx"]
source_type: "manual"
controller_model: []
software_version: ["本机 c.suite 4.4.22", "c.strategy 帮助 4.3.x / Manual 1.4"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL 工程创建与保存

## 本文解决的问题

从空模板创建工程，知道程序、变量、构建信息和保存文件在哪里。本文是官方步骤整理，未在本轮新建工程。

## 操作步骤与预期结果

1. 启动 c.strategy，选择 File → New → Project。
2. 选择 CAREL 模板，填写工程名、保存位置、解决方案名，按需要勾选 Create directory for new solution。
3. 在 Solution Explorer 展开设备和资源；添加所需语言的 PROGRAM，设置名称。
4. 在程序编辑器添加功能块、变量及连线；需要给其他编辑器使用的变量，在相应发布列勾选。
5. Build Solution 后检查 Output 与 Error List。生成完成和诊断无误是编译检查，尚不是运行验证。[0201_从基础应用开始创建工程.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0201_%E4%BB%8E%E5%9F%BA%E7%A1%80%E5%BA%94%E7%94%A8%E5%BC%80%E5%A7%8B%E5%88%9B%E5%BB%BA%E5%B7%A5%E7%A8%8B.md)

## 文件与参数

现有工程有 .otsln 解决方案、.acfproj 工程及内部资源/POU 文件。保存后通过实际路径、修改时间和重新读取检查内容，不能只看窗口标题。

MCP 创建 ST 时 source 放可执行语句，变量通过 variables 参数单独声明；修改已有工程按本知识库 AGENTS 先展示差异并取得确认。

## 常见错误

未选 CAREL 模板、混淆工程与解决方案、变量未发布、只检查上次错误列表。安装步骤 DOCX 已保留段落和截图定位，安装本身本轮未重跑。

## 尚未核实

具体目标板和固件、所选库版本、工程迁移兼容性。

## 来源及定位

- [0201_从基础应用开始创建工程.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0201_%E4%BB%8E%E5%9F%BA%E7%A1%80%E5%BA%94%E7%94%A8%E5%BC%80%E5%A7%8B%E5%88%9B%E5%BB%BA%E5%B7%A5%E7%A8%8B.md)
- [c.suite 4.4.22 安装步骤.docx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%AE%89%E8%A3%85%E6%96%87%E6%A1%A3/DOC01_c.suite%204.4.22%20%E5%AE%89%E8%A3%85%E6%AD%A5%E9%AA%A4.docx.md)
- [c.suite 4.2.9 安装步骤.docx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%AE%89%E8%A3%85%E6%96%87%E6%A1%A3/DOC02_c.suite%204.2.9%20%E5%AE%89%E8%A3%85%E6%AD%A5%E9%AA%A4.docx.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
