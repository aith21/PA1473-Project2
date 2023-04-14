#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

gripper_motor = Motor(Port.A)

elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

# Move motors

elbow_motor.control.limits(speed=120, acceleration=120)
base_motor.control.limits(speed=120, acceleration=120)

# Close gripper -- Open Gripper 

gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)

# Lower elbow

elbow_motor.run_target(60, -40)

#Close gripper

gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)

#Raise elbow

elbow_motor.control.limits(speed=120, acceleration=120)
