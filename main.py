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

def closegrip():  
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 

def elbowup():
    ev3.screen.print("ELBOW UP")
    elbow_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    elbow_motor.reset_angle(90) 

def opengrip():
    ev3.screen.print("OPEN GRIP")

    gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(200, -90)

def elbowdown():
    ev3.screen.print("ELBOW DOWN")
    elbow_motor.run_until_stalled(-200, then=Stop.COAST, duty_limit=50)


elbow_motor.control.limits(speed=120, acceleration=120)
base_motor.control.limits(speed=120, acceleration=120)

# Close gripper -- Open Gripper
elbowup()
opengrip()
elbowdown()
closegrip()
elbowup()
ev3.speaker.beep()


