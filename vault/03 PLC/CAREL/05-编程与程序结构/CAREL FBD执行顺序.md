---
title: "CAREL FBD执行顺序"
source_files: ["0208_FBD 程序的执行顺序.md", "0102_c.suite培训课程_2.8_中文版.pdf"]
source_type: "manual"
controller_model: []
software_version: ["c.strategy 帮助 4.3.x / Manual 1.4"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL FBD执行顺序

## 本文解决的问题

解释图形位置与数据依赖如何影响 FBD 顺序，避免按接线图外观推断程序。

## 官方规则

1. 网络按从左到右、从上到下执行。
2. 一个块的全部输入先求出，才能执行该块；多个块的输入同时就绪时，按块左上角位置从左到右、从上到下排列。
3. 输出相关块按原页描述递归执行。
4. Ctrl+W 显示执行顺序标签；问号 ? 表示无法确定执行顺序。[0208_FBD 程序的执行顺序.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0208_FBD%20%E7%A8%8B%E5%BA%8F%E7%9A%84%E6%89%A7%E8%A1%8C%E9%A1%BA%E5%BA%8F.md)

## 操作与排查

打开目标 FBD，显示编号，对照数据依赖核查读入、计算和赋值。遇到 ? 时先定位相关网络及输入依赖，再结合构建诊断分析。不要因为界面上一个块画在上方就忽略其输入依赖。

## 尚未核实

Chiller 的 FBD 图形程序体未通过 IDE 打开读取；工程结构索引中的 POU 名称不证明其执行顺序。

## 温控图的可读连接

已看原始PDF第31页：W_InTemp进入Conv_REAL.In，SetP_Temp进入In0；SetP_Temp与PB_Temp相加后进入In100。Conv_REAL输出分别接入四个HysterAdv_REAL实例的In。四个实例SetP依次25.0、50.0、75.0、100.0，DiffLeft均25.0、DiffRight均0.0、Reverse均FALSE，Out分别接Comp1–Comp4。[0102_c.suite培训课程_2.8_中文版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF03_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pdf.md#pdf%E7%AC%AC31%E9%A1%B5)

这些数字处于转换后的控制域；不能直接把四个SetP解释为现场温度摄氏值。课件写“替代方案PID_Adv”，当前PID帮助另说明旧块已由PID_Adv_2替代，跨版本选块需查实际库。


## 来源及定位

- [0208_FBD 程序的执行顺序.md](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/%E5%B8%AE%E5%8A%A9%E8%AF%91%E6%96%87/0208_FBD%20%E7%A8%8B%E5%BA%8F%E7%9A%84%E6%89%A7%E8%A1%8C%E9%A1%BA%E5%BA%8F.md)
- [0102_c.suite培训课程_2.8_中文版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF03_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pdf.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
