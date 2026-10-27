# CAREL 卡乐技术学习知识库

面向c.suite / c.pCO与旧pCO资料查阅的中文笔记，配有本地检索工具、课程导读和MCP工程操作规范。

| 内容 | 当前公开版 |
|---|---|
| 技术主题 | 22篇，涵盖型号、软件、变量与功能块、I/O、Modbus、PID、报警和排查 |
| 视频课程 | 35节导读，其中10节补充中文操作步骤，1节用无音轨画面时间定位 |
| 本地检索 | Python标准库可运行；有ripgrep时自动使用rg |
| MCP说明 | 18个真实工具签名、只读与修改分类、修改确认流程 |
| 示例 | 温控回差ST执行体与独立变量表；未做物理控制器验证 |

## 开始使用

1. 下载仓库，把`vault`文件夹作为Obsidian知识库打开；也可将其下`03 PLC/CAREL`并入已有Vault。
2. 从[知识库首页](vault/03%20PLC/CAREL/00-%E9%A6%96%E9%A1%B5%E4%B8%8E%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/CAREL%20%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A6%96%E9%A1%B5.md)或[资料总索引](vault/03%20PLC/CAREL/%E8%B5%84%E6%96%99%E6%80%BB%E7%B4%A2%E5%BC%95.md)查阅。
3. 安装Python 3.10+，在仓库根目录运行：

```shell
python tools/search_carel.py "PID_Adv_2"
python tools/search_carel.py "Retries" --scope topics
python -m unittest discover -s tests -v
python tools/audit_public.py
```

搜索先读取首页和索引，再查主题；不足时查课程导读和来源说明。原件补入自己的本地库后再核对关键技术值。

## 按问题查阅

- [CAREL 型号与开发平台](vault/03%20PLC/CAREL/02-%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/CAREL%20%E5%9E%8B%E5%8F%B7%E4%B8%8E%E5%BC%80%E5%8F%91%E5%B9%B3%E5%8F%B0.md)
- [CAREL c.pCO端口与硬件查表](vault/03%20PLC/CAREL/04-%E6%8E%A7%E5%88%B6%E5%99%A8%E4%B8%8E%E7%A1%AC%E4%BB%B6/CAREL%20c.pCO%E7%AB%AF%E5%8F%A3%E4%B8%8E%E7%A1%AC%E4%BB%B6%E6%9F%A5%E8%A1%A8.md)
- [CAREL 工程创建与保存](vault/03%20PLC/CAREL/03-%E8%BD%AF%E4%BB%B6%E6%93%8D%E4%BD%9C/CAREL%20%E5%B7%A5%E7%A8%8B%E5%88%9B%E5%BB%BA%E4%B8%8E%E4%BF%9D%E5%AD%98.md)
- [CAREL 变量声明与发布](vault/03%20PLC/CAREL/05-%E7%BC%96%E7%A8%8B%E4%B8%8E%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/CAREL%20%E5%8F%98%E9%87%8F%E5%A3%B0%E6%98%8E%E4%B8%8E%E5%8F%91%E5%B8%83.md)
- [CAREL 函数与功能块实例](vault/03%20PLC/CAREL/05-%E7%BC%96%E7%A8%8B%E4%B8%8E%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/CAREL%20%E5%87%BD%E6%95%B0%E4%B8%8E%E5%8A%9F%E8%83%BD%E5%9D%97%E5%AE%9E%E4%BE%8B.md)
- [CAREL FBD执行顺序](vault/03%20PLC/CAREL/05-%E7%BC%96%E7%A8%8B%E4%B8%8E%E7%A8%8B%E5%BA%8F%E7%BB%93%E6%9E%84/CAREL%20FBD%E6%89%A7%E8%A1%8C%E9%A1%BA%E5%BA%8F.md)
- [CAREL 仿真与在线调试](vault/03%20PLC/CAREL/03-%E8%BD%AF%E4%BB%B6%E6%93%8D%E4%BD%9C/CAREL%20%E4%BB%BF%E7%9C%9F%E4%B8%8E%E5%9C%A8%E7%BA%BF%E8%B0%83%E8%AF%95.md)
- [CAREL I_O通道与换算](vault/03%20PLC/CAREL/04-%E6%8E%A7%E5%88%B6%E5%99%A8%E4%B8%8E%E7%A1%AC%E4%BB%B6/CAREL%20I_O%E9%80%9A%E9%81%93%E4%B8%8E%E6%8D%A2%E7%AE%97.md)
- [CAREL DEV默认值与参数导入导出](vault/03%20PLC/CAREL/03-%E8%BD%AF%E4%BB%B6%E6%93%8D%E4%BD%9C/CAREL%20DEV%E9%BB%98%E8%AE%A4%E5%80%BC%E4%B8%8E%E5%8F%82%E6%95%B0%E5%AF%BC%E5%85%A5%E5%AF%BC%E5%87%BA.md)
- [CAREL LOG记录与导出](vault/03%20PLC/CAREL/03-%E8%BD%AF%E4%BB%B6%E6%93%8D%E4%BD%9C/CAREL%20LOG%E8%AE%B0%E5%BD%95%E4%B8%8E%E5%AF%BC%E5%87%BA.md)
- [CAREL Modbus主站配置](vault/03%20PLC/CAREL/06-%E9%80%9A%E4%BF%A1%E4%B8%8E%E6%95%B0%E6%8D%AE%E4%BA%A4%E6%8D%A2/CAREL%20Modbus%E4%B8%BB%E7%AB%99%E9%85%8D%E7%BD%AE.md)
- [CAREL Modbus从站与数据表示](vault/03%20PLC/CAREL/06-%E9%80%9A%E4%BF%A1%E4%B8%8E%E6%95%B0%E6%8D%AE%E4%BA%A4%E6%8D%A2/CAREL%20Modbus%E4%BB%8E%E7%AB%99%E4%B8%8E%E6%95%B0%E6%8D%AE%E8%A1%A8%E7%A4%BA.md)
- [CAREL Modbus故障定位](vault/03%20PLC/CAREL/08-%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5%E4%B8%8E%E6%A1%88%E4%BE%8B/CAREL%20Modbus%E6%95%85%E9%9A%9C%E5%AE%9A%E4%BD%8D.md)
- [CAREL pGD1的NO LINK排查](vault/03%20PLC/CAREL/08-%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5%E4%B8%8E%E6%A1%88%E4%BE%8B/CAREL%20pGD1%E7%9A%84NO%20LINK%E6%8E%92%E6%9F%A5.md)
- [CAREL 报警类型与保护逻辑](vault/03%20PLC/CAREL/07-%E5%88%B6%E5%86%B7%E4%B8%8E%E6%8E%A7%E5%88%B6%E7%AE%97%E6%B3%95/CAREL%20%E6%8A%A5%E8%AD%A6%E7%B1%BB%E5%9E%8B%E4%B8%8E%E4%BF%9D%E6%8A%A4%E9%80%BB%E8%BE%91.md)
- [CAREL PID_Adv_2查阅与参数](vault/03%20PLC/CAREL/07-%E5%88%B6%E5%86%B7%E4%B8%8E%E6%8E%A7%E5%88%B6%E7%AE%97%E6%B3%95/CAREL%20PID_Adv_2%E6%9F%A5%E9%98%85%E4%B8%8E%E5%8F%82%E6%95%B0.md)
- [CAREL 温控回差与联锁示例](vault/03%20PLC/CAREL/07-%E5%88%B6%E5%86%B7%E4%B8%8E%E6%8E%A7%E5%88%B6%E7%AE%97%E6%B3%95/CAREL%20%E6%B8%A9%E6%8E%A7%E5%9B%9E%E5%B7%AE%E4%B8%8E%E8%81%94%E9%94%81%E7%A4%BA%E4%BE%8B.md)
- [CAREL MCP只读工程分析案例](vault/03%20PLC/CAREL/08-%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5%E4%B8%8E%E6%A1%88%E4%BE%8B/CAREL%20MCP%E5%8F%AA%E8%AF%BB%E5%B7%A5%E7%A8%8B%E5%88%86%E6%9E%90%E6%A1%88%E4%BE%8B.md)
- [CAREL c.mask画面与按键层级](vault/03%20PLC/CAREL/03-%E8%BD%AF%E4%BB%B6%E6%93%8D%E4%BD%9C/CAREL%20c.mask%E7%94%BB%E9%9D%A2%E4%B8%8E%E6%8C%89%E9%94%AE%E5%B1%82%E7%BA%A7.md)
- [CAREL c.mask多语言文本导入导出](vault/03%20PLC/CAREL/03-%E8%BD%AF%E4%BB%B6%E6%93%8D%E4%BD%9C/CAREL%20c.mask%E5%A4%9A%E8%AF%AD%E8%A8%80%E6%96%87%E6%9C%AC%E5%AF%BC%E5%85%A5%E5%AF%BC%E5%87%BA.md)
- [CAREL Web套件页面与日志图解](vault/03%20PLC/CAREL/03-%E8%BD%AF%E4%BB%B6%E6%93%8D%E4%BD%9C/CAREL%20Web%E5%A5%97%E4%BB%B6%E9%A1%B5%E9%9D%A2%E4%B8%8E%E6%97%A5%E5%BF%97%E5%9B%BE%E8%A7%A3.md)
- [CAREL 旧pCO拓扑与扩展卡图解](vault/03%20PLC/CAREL/04-%E6%8E%A7%E5%88%B6%E5%99%A8%E4%B8%8E%E7%A1%AC%E4%BB%B6/CAREL%20%E6%97%A7pCO%E6%8B%93%E6%89%91%E4%B8%8E%E6%89%A9%E5%B1%95%E5%8D%A1%E5%9B%BE%E8%A7%A3.md)

## 来源与适用范围

笔记保留文件名、PDF文件页序、PPT幻灯片、帮助章节和实际视频时间。公开版的“90-原始资料”目录保存来源说明与演示源码，第三方原件需自行获取。完整PDF/PPT、离线HTML、视频、配音、字幕转录、软件安装包和用户工程保留在本地。

c.suite/c.pCO、旧1tool/pCO和STone按实际型号与版本分开。示例参数不代表设备默认值；机器转写、原文冲突及尚未验证项目保留明确状态。

[来源元数据](data/sources.json) · [公开范围与来源说明](THIRD_PARTY_NOTICES.md) · [发布验收](docs/发布验收.md)

## MCP工程操作

先读状态、模型和源码，再展示具体diff。写工程、构建、启停或改写仿真、修改设备配置前，须确认目标、影响、备份与验证方法。工具目录未提供的设备操作不会被视为可用能力。

本仓库提供知识库与能力文档；MCP服务端和CAREL软件需自行安装配置。

## 持续维护

新增资料先查重和核对版本，再更新来源、主题与待处理。提交前运行测试及公开范围审计；案例标明源码分析、软件构建、仿真或实物验证的实际范围。
