---
title: "CAREL Web套件页面与日志图解"
source_files: ["0102_c.suite培训课程_2.8_中文版.pdf", "Web服务器"]
source_type: "manual"
controller_model: ["课程c.pCO示例"]
software_version: ["c.suite培训课程2.8；Web录屏版本未知"]
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL Web套件页面与日志图解

## 本文解决的问题

根据原图识别Web kit的远程终端、变量表和日志趋势，区分浏览、导出及写值。

## 图中确认的功能

PDF第134页顶部将页面分为header、logo、topmenu、container、menu、title、menu_cat、maintext、bottommenu。Web pGD示例说明可与其他pLAN终端并行、动态更新；活动区394×198像素，按键区域可点击并跟踪按压时间。这是该示例布局的尺寸。[0102_c.suite培训课程_2.8_中文版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF03_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pdf.md#pdf%E7%AC%AC134%E9%A1%B5)

| 页面 | 可读功能 | 核对要点 |
|---|---|---|
| Variables table | 自动列出public变量；名称/描述来自c.strategy/c.design；AJAX后台刷新 | 外框蓝色表示c.pCO正常，红色表示未响应 |
| Variable write | enable write、输入文本、set或set all selected variables | 会写变量；执行前确认目标和原值 |
| Logger Charts | 按c.design日志配置自动填充列表；选择开始/结束时间并从c.pCO加载 | 先核对时间范围、日志名和单位 |
| 导出及图表 | 保存CSV、保存PNG、缩放/平移/选择/点值；序列显隐、主/副轴和颜色 | 轴的分配影响读数，不能只比较线高 |

## 操作顺序

1. 确认网页包与控制器版本、连接对象和网络状态。
2. 先查看远程终端、public变量和日志时间范围。
3. 对趋势核对单位、主/副轴及启用的序列，再保存CSV或PNG。
4. 需要写设定值时，记录原值、目标值和影响，确认后才使用写入控件。

## 常见错误与尚未核实

Web kit是课程示例；当前设备的页面路径、权限、变量列表及刷新周期仍需读取实际部署。录屏的网页写值仅为课程演示，本任务未写设备。[Web服务器](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0408_Web%E6%9C%8D%E5%8A%A1%E5%99%A8.md)


## 来源及定位

- [0102_c.suite培训课程_2.8_中文版.pdf](../90-%E5%8E%9F%E5%A7%8B%E8%B5%84%E6%96%99/PDF%E5%85%A8%E6%96%87/PDF03_0102_c.suite%E5%9F%B9%E8%AE%AD%E8%AF%BE%E7%A8%8B_2.8_%E4%B8%AD%E6%96%87%E7%89%88.pdf.md)
- [Web服务器](../09-%E8%A7%86%E9%A2%91%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0/0408_Web%E6%9C%8D%E5%8A%A1%E5%99%A8.md)

公开版保留学习归纳与出处说明；原始PDF、课件、离线HTML及设备工程需自行合法获取并核对。
