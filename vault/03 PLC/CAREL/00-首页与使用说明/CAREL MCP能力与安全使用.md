---
title: "CAREL MCP能力与安全使用"
source_files: []
source_type: "other"
controller_model: []
software_version: []
tags: ["carel"]
status: "partial"
edition: "public"
---

# CAREL MCP能力与安全使用

本页记录本地c.suite 4.4.22 / carel-plc bridge 0.2.0实际暴露的18个工具。仓库提供能力说明与使用规则；MCP服务端、安装软件及连接配置由使用者自行提供。

## 实际工具与副作用

| 工具 | 分类 |
|---|---|
| `carel_build_project` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_build_status` | 只读查询 |
| `carel_close_project` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_create_project` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_create_st_program` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_launch` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_list_projects` | 只读查询 |
| `carel_model` | 只读查询 |
| `carel_open_project` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_read_program` | 只读查询 |
| `carel_save_project` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_simulation_read` | 只读查询 |
| `carel_simulation_start` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_simulation_status` | 只读查询 |
| `carel_simulation_stop` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_simulation_write` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |
| `carel_status` | 只读查询 |
| `carel_write_program` | 修改文件、工程或IDE/仿真状态；执行前确认具体目标 |

## 真实参数签名

### carel_build_project

```ts
declare const tools: { mcp__carel_plc__carel_build_project(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_build_status

```ts
declare const tools: { mcp__carel_plc__carel_build_status(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_close_project

```ts
declare const tools: { mcp__carel_plc__carel_close_project(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_create_project

```ts
declare const tools: { mcp__carel_plc__carel_create_project(args: { directory: string; name: string; pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_create_st_program

```ts
declare const tools: { mcp__carel_plc__carel_create_st_program(args: { name: string; pid?: number | null; resource: string; source: string; variables: Array<{ [key: string]: string; }>; }): Promise<CallToolResult>; };
```

### carel_launch

```ts
declare const tools: { mcp__carel_plc__carel_launch(args: { application?: "strategy" | "mask" | "design" | "factory"; }): Promise<CallToolResult>; };
```

### carel_list_projects

```ts
declare const tools: { mcp__carel_plc__carel_list_projects(args: { [key: string]: unknown; }): Promise<CallToolResult>; };
```

### carel_model

```ts
declare const tools: { mcp__carel_plc__carel_model(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_open_project

```ts
declare const tools: { mcp__carel_plc__carel_open_project(args: { pid?: number | null; solution_path: string; }): Promise<CallToolResult>; };
```

### carel_read_program

```ts
declare const tools: { mcp__carel_plc__carel_read_program(args: { pid?: number | null; program: string; }): Promise<CallToolResult>; };
```

### carel_save_project

```ts
declare const tools: { mcp__carel_plc__carel_save_project(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_simulation_read

```ts
declare const tools: { mcp__carel_plc__carel_simulation_read(args: { pid?: number | null; program: string; }): Promise<CallToolResult>; };
```

### carel_simulation_start

```ts
declare const tools: { mcp__carel_plc__carel_simulation_start(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_simulation_status

```ts
declare const tools: { mcp__carel_plc__carel_simulation_status(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_simulation_stop

```ts
declare const tools: { mcp__carel_plc__carel_simulation_stop(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_simulation_write

```ts
declare const tools: { mcp__carel_plc__carel_simulation_write(args: { pid?: number | null; program: string; values: { [key: string]: boolean | number | number; }; }): Promise<CallToolResult>; };
```

### carel_status

```ts
declare const tools: { mcp__carel_plc__carel_status(args: { pid?: number | null; }): Promise<CallToolResult>; };
```

### carel_write_program

```ts
declare const tools: { mcp__carel_plc__carel_write_program(args: { expected_sha256: string; pid?: number | null; program: string; source: string; }): Promise<CallToolResult>; };
```

## 使用顺序

1. 先carel_status，再用本次真实pid读取carel_model与carel_read_program。
2. 核对控制器、OS、软件及库版本；不能读取的内容标明范围。
3. 提出目标、原值、具体diff、原因、影响、备份及验证方法。
4. 写工程、覆盖文件、构建、启停仿真、改仿真变量或设备操作，必须先获得用户对具体操作的确认。
5. 修改前重新读取源码与SHA，使用expected_sha256；按工具真实返回值验证。构建等待最终状态，仿真检查Running、Good质量与时间戳。

工具目录没有物理控制器下载、启动/停止或强制I/O接口。不能由本机仿真通过推定实物验证；不解码绕过受保护程序体。

## 本地历史验证

知识库整理期间完成6类只读查询：状态、工程列表、模型、源码、仿真状态和仿真变量。读取演示ST及已有Running会话的12个Good变量。公开仓库不包含用户工程、进程信息或原始工具返回；这些记录描述当时的本地验证范围。
