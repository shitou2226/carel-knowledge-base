---
title: "CAREL 本地检索使用方法"
source_files: []
source_type: "other"
controller_model: []
software_version: []
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL 本地检索使用方法

在仓库根目录运行，Python 3.10+即可：

```shell
python tools/search_carel.py "PID_Adv_2"
python tools/search_carel.py "Online error" --scope topics
python tools/search_carel.py "DEV" --scope all --limit 10
```

自动模式先读首页与总索引，再查02–08主题；无结果时查来源说明与课程导读。检测到ripgrep时使用rg，否则退回Python标准库。支持--root指定自行扩充后的CAREL目录。

输出包括命中文件、行号与片段。公开版来源说明不含原文；精确参数和适用条件需打开自行获取的原件。没有命中时先扩展中英文同义词，再说明缺少的资料。
