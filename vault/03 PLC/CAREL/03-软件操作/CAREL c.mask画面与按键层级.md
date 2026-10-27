---
title: "CAREL c.mask画面与按键层级"
source_files: ["csuite_Course_2_8.pptx", "0102_c.suite培训课程_2.8_中文版.pptx", "c.mask 基础与单画面", "画面循环与按键绑定", "终端、画面、类与自定义类"]
source_type: "manual"
controller_model: ["课件范围 pGD1"]
software_version: ["c.suite 培训课件2.8；本机4.4.22界面行为待逐项复验"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL c.mask画面与按键层级

## 本文解决的问题

根据已有课件建立变量画面、绑定按键，并解释 Terminal、Mask、Class 的优先关系。这里记录课件版本的功能范围，不把旧课件限制认定为所有后续版本限制。

## 操作步骤

1. 在策略变量表勾选 UI，才可在 c.mask 的 Variable 对象中选择。
2. 拖放 Text 或 Variable 到画面；文本通过 Text 属性或双击编辑，变量选择对应对象后编辑 Format、上下限和 Class。
3. ST-Code 页面创建按键函数；Key Binding Editor 依次选 Terminal/Mask/Class 层级、按键和函数。
4. 需要用户类时复制标准 Class，修改 Name、Format 等，再在 Variable 的 Class 属性中选用。[0102_c.suite培训课程_2.8_中文版.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT02_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pptx.md#%E5%B9%BB%E7%81%AF%E7%89%8767)；[0102_c.suite培训课程_2.8_中文版.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT02_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pptx.md#%E5%B9%BB%E7%81%AF%E7%89%8769)；[0102_c.suite培训课程_2.8_中文版.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT02_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pptx.md#%E5%B9%BB%E7%81%AF%E7%89%8773)

## 关键规则与示例

- 类的按键/属性优先级高于画面，画面高于终端。[0102_c.suite培训课程_2.8_中文版.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT02_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pptx.md#%E5%B9%BB%E7%81%AF%E7%89%8771)
- 对象上的 Format 属性会覆盖 Class 定义格式。[0102_c.suite培训课程_2.8_中文版.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT02_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pptx.md#%E5%B9%BB%E7%81%AF%E7%89%8768)
- 课件中 REAL 的 CL_REAL_0/1/2/3 分别对应0/1/2/3位小数；示例增减步长为1、0.1、0.01、0.001。[0102_c.suite培训课程_2.8_中文版.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT02_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pptx.md#%E5%B9%BB%E7%81%AF%E7%89%8772)
- Loop 是画面集合；课件把 GotoLoop() 与进入该循环第一个画面作对应说明。参数签名应查实际库，不凭课件标题补造调用代码。

## 常见错误与待核实

变量未发布UI；低层级绑定被高层级覆盖；显示格式变化被误当作协议缩放；把 c.mask 简化 ST 与 c.strategy 的 ST 当作同一编辑器。课件第74页记录的语言限制只代表该资料版本，当前4.4.22逐项兼容性尚未实测。

## 来源及定位

- [csuite_Course_2_8.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT01_csuite_Course_2_8.pptx.md)
- [0102_c.suite培训课程_2.8_中文版.pptx](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PPT%E9%80%90%E9%A1%B5/PPT02_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pptx.md)
- [c.mask 基础与单画面](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0311_c.mask%20%E5%9F%BA%E7%A1%80%E4%B8%8E%E5%8D%95%E7%94%BB%E9%9D%A2.md)
- [画面循环与按键绑定](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0312_%E7%94%BB%E9%9D%A2%E5%BE%AA%E7%8E%AF%E4%B8%8E%E6%8C%89%E9%94%AE%E7%BB%91%E5%AE%9A.md)
- [终端、画面、类与自定义类](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0314_%E7%BB%88%E7%AB%AF%E3%80%81%E7%94%BB%E9%9D%A2%E3%80%81%E7%B1%BB%E4%B8%8E%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B1%BB.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
