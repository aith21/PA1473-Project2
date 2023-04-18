#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

MENUTEXT = """What do you want to do?
(1) Pick a position to pick up from
(2) Pick a position to put down
(3) Close"""

# Initialize the EV3 Brick
ev3 = EV3Brick()

gripper_motor = Motor(Port.A)

elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

touch_sensor = TouchSensor(Port.S1)

elbow_motor.control.limits(speed=120, acceleration=120)
base_motor.control.limits(speed=120, acceleration=120)

#positions on paper in degrees
#pos1=180
#pos2=135
#pos3=90
#pos4=0

positions = [177,135,82,-15]

def printmenu():
    choice = 0
    print(MENUTEXT)
    choice = input("Your choice: ")

def closegrip():  
    ev3.screen.print("CLOSE GRIP")
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 

def elbowup():
    ev3.screen.print("ELBOW UP")
    elbow_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=50)
    elbow_motor.reset_angle(90) 

def opengrip():
    ev3.screen.print("OPEN GRIP")
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0) 
    gripper_motor.run_target(200, -90)

def elbowdown():
    ev3.screen.print("ELBOW DOWN")
    elbow_motor.run_until_stalled(-50, then=Stop.COAST, duty_limit=50)

def pickup(pos):
    ev3.screen.print("PICK UP")

    pickupposition(pos)    
    opengrip()
    elbowdown()
    closegrip()
    elbowup()
    ev3.speaker.beep()

def pickupposition(pos):

    elbowup()
    base_motor.run_target(60, pos)

def gotoposition(pos):
    elbowup()
    base_motor.run_target(60, pos)

def setbaseposition():
    ev3.screen.print("SETTING BASE POSITION...")

    elbowup()

    base_motor.run(-100)
    while not touch_sensor.pressed():
        pass
    base_motor.stop()
    wait(1000)
    base_motor.reset_angle(0)

    ev3.screen.print("BASE POSITION FOUND")

def dropoff(position):
    gotoposition(position)
    elbowdown()
    opengrip()
    elbowup()
    
def gotoendposition():
    elbowup()
    gotoposition(40)
    elbowdown()


def run():
    ev3.screen.print("Starting")
    #printmenu()
    gotoposition(30)
    setbaseposition()
    pickup(positions[0])
    dropoff(positions[3])
    pickup(positions[2])
    dropoff(positions[0])
    gotoendposition()
    ev3.screen.print("Finished")
    wait(3000)
    ev3.speaker.beep()
    ev3.speaker.beep()
    ev3.speaker.beep()



    

run()