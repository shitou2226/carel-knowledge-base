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
