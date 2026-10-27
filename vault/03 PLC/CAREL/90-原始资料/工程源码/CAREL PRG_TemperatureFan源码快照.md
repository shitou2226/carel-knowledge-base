---
title: "PRG_TemperatureFan 演示源码"
source_files: ["PRG_TemperatureFan.isaxml"]
source_type: "other"
controller_model: []
software_version: []
tags: ["carel"]
status: "partial"
edition: "public"
---

# PRG_TemperatureFan 演示源码

本地演示工程的只读源码记录，供解释回差与联锁。变量声明与执行语句分开；未在物理控制器验证。

## 变量

| 变量 | 类型 | 说明 |
|---|---|---|
| InitDone | BOOL | One-time parameter initialization complete |
| Enable | BOOL | Demo input: enable temperature control |
| SensorFault | BOOL | Demo input: TRUE means temperature sensor fault |
| Temperature | REAL | Demo input: measured temperature in degC |
| Setpoint | REAL | Editable stop threshold in degC; initial 25.0 |
| Deadband | REAL | Editable positive start offset in degC; initial 2.0 |
| HighLimit | REAL | Editable high temperature alarm threshold; initial 35.0 |
| ParamFault | BOOL | Invalid deadband or alarm threshold |
| HighTempAlarm | BOOL | High temperature alarm with valid sensor and parameters |
| FanDemand | BOOL | Internal hysteresis state |
| FanRunCmd | BOOL | Demo output: fan run command |
| StatusCode | INT | 0 disabled; 1 idle; 2 running; 10 sensor; 11 parameter; 12 high temp |

## 源码

```st
(* Initialize editable demonstration parameters once. *)
IF NOT InitDone THEN
    Setpoint := 25.0;
    Deadband := 2.0;
    HighLimit := 35.0;
    InitDone := TRUE;
END_IF;

(* Validate thresholds before allowing the fan output. *)
ParamFault := (Deadband <= 0.0) OR (HighLimit <= (Setpoint + Deadband));
HighTempAlarm := (NOT SensorFault) AND (NOT ParamFault) AND (Temperature >= HighLimit);

(* Hysteresis: start at Setpoint + Deadband, stop at Setpoint. *)
IF (NOT Enable) OR SensorFault OR ParamFault THEN
    FanDemand := FALSE;
ELSE
    IF Temperature >= (Setpoint + Deadband) THEN
        FanDemand := TRUE;
    ELSIF Temperature <= Setpoint THEN
        FanDemand := FALSE;
    END_IF;
END_IF;

FanRunCmd := Enable AND (NOT SensorFault) AND (NOT ParamFault) AND FanDemand;

(* Status: 0 disabled, 1 idle, 2 running, 10 sensor, 11 parameters, 12 high temperature. *)
IF SensorFault THEN
    StatusCode := 10;
ELSIF ParamFault THEN
    StatusCode := 11;
ELSIF HighTempAlarm THEN
    StatusCode := 12;
ELSIF NOT Enable THEN
    StatusCode := 0;
ELSIF FanRunCmd THEN
    StatusCode := 2;
ELSE
    StatusCode := 1;
END_IF;
```

## 行号定位

1. `(* Initialize editable demonstration parameters once. *)`
2. `IF NOT InitDone THEN`
3. `    Setpoint := 25.0;`
4. `    Deadband := 2.0;`
5. `    HighLimit := 35.0;`
6. `    InitDone := TRUE;`
7. `END_IF;`
8. ``
9. `(* Validate thresholds before allowing the fan output. *)`
10. `ParamFault := (Deadband <= 0.0) OR (HighLimit <= (Setpoint + Deadband));`
11. `HighTempAlarm := (NOT SensorFault) AND (NOT ParamFault) AND (Temperature >= HighLimit);`
12. ``
13. `(* Hysteresis: start at Setpoint + Deadband, stop at Setpoint. *)`
14. `IF (NOT Enable) OR SensorFault OR ParamFault THEN`
15. `    FanDemand := FALSE;`
16. `ELSE`
17. `    IF Temperature >= (Setpoint + Deadband) THEN`
18. `        FanDemand := TRUE;`
19. `    ELSIF Temperature <= Setpoint THEN`
20. `        FanDemand := FALSE;`
21. `    END_IF;`
22. `END_IF;`
23. ``
24. `FanRunCmd := Enable AND (NOT SensorFault) AND (NOT ParamFault) AND FanDemand;`
25. ``
26. `(* Status: 0 disabled, 1 idle, 2 running, 10 sensor, 11 parameters, 12 high temperature. *)`
27. `IF SensorFault THEN`
28. `    StatusCode := 10;`
29. `ELSIF ParamFault THEN`
30. `    StatusCode := 11;`
31. `ELSIF HighTempAlarm THEN`
32. `    StatusCode := 12;`
33. `ELSIF NOT Enable THEN`
34. `    StatusCode := 0;`
35. `ELSIF FanRunCmd THEN`
36. `    StatusCode := 2;`
37. `ELSE`
38. `    StatusCode := 1;`
39. `END_IF;`
