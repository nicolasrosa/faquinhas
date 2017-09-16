#!/bin/bash
echo cape-universaln > /sys/devices/bone_capemgr.*/slots
config-pin -l P9.14
config-pin -l P9.16
config-pin P9.14 pwm
config-pin P9.16 pwm
echo pwm > /sys/devices/ocp.*/P9_14_pinmux.*/state
echo pwm > /sys/devices/ocp.*/P9_16_pinmux.*/state
echo 3 > /sys/class/pwm/export
echo 4 > /sys/class/pwm/export

echo 250000 > /sys/class/pwm/pwm3/duty_ns
echo 500000 > /sys/class/pwm/pwm3/period_ns
echo 1 > /sys/class/pwm/pwm3/run

echo 250000 > /sys/class/pwm/pwm4/duty_ns
echo 500000 > /sys/class/pwm/pwm4/period_ns
echo 1 > /sys/class/pwm/pwm4/run

cat /sys/class/pwm/pwm3/duty_ns /sys/class/pwm/pwm3/period_ns /sys/class/pwm/pwm3/run
cat /sys/class/pwm/pwm4/duty_ns /sys/class/pwm/pwm4/period_ns /sys/class/pwm/pwm4/run
