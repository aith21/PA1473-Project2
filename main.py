#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.parameters import Color, SoundFile
from pybricks.tools import wait

MENUTEXT = """What do you want to do?
(1) Pick a position to pick up from
(2) Pick a position to put down
(3) Close"""

boolcheckcolor=True

# Initialize the EV3 Brick
ev3 = EV3Brick()

gripper_motor = Motor(Port.A)

elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

touch_sensor = TouchSensor(Port.S1)

color_sensor = ColorSensor(Port.S2)

#color_sensor = ColorSensor(Port.S2)

elbow_motor.control.limits(speed=120, acceleration=120)
base_motor.control.limits(speed=120, acceleration=120)

#positions on paper in degrees
#pos1=180
#pos2=135
#pos3=90
#pos4=0

positions = [177,135,82,-15]
colors = [Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN]

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

def pickup(pos,cc):
    ev3.screen.print("PICK UP")

    pickupposition(pos) 

    opengrip()
    elbowdown()
    closegrip()
    if cc is True:
        checkcolor()

    elbowup()
    ev3.speaker.beep()

def checkcolor():
    Colorfound = False
    ev3.speaker.say("Will check color")
    elbow_motor.reset_angle(0)
    elbow_motor.run_target(50, 40)
    wait(2000)
    while Colorfound == False:
        # Read the raw RGB values
        measuredcolor = color_sensor.color()

        if measuredcolor in colors:
            if measuredcolor == Color.BLUE:
                ev3.speaker.say("blue")
                ev3.screen.print("BLUE COLOR")
            elif measuredcolor == Color.RED:
                ev3.speaker.say("red")
                ev3.screen.print("RED COLOR")
            elif measuredcolor == Color.GREEN:
                ev3.speaker.say("green")
                ev3.screen.print("GREEN COLOR")
            elif measuredcolor == Color.YELLOW:
                ev3.speaker.say("yellow")
                ev3.screen.print("YELLOW COLOR")

            Colorfound = True
       
    ev3.speaker.beep()
    


def pickupposition(pos):

    elbowup()
    base_motor.run_target(90, pos)

def gotoposition(pos):
    elbowup()
    base_motor.run_target(60, pos)

def setbaseposition():
    ev3.screen.print("SETTING BASE POSITION...")

    elbowup()

    base_motor.run(-60)
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
    pickup(positions[0], boolcheckcolor)
    dropoff(positions[3])
    pickup(positions[2], boolcheckcolor)
    dropoff(positions[0])
    gotoendposition()
    ev3.screen.print("Finished")
    wait(3000)
    ev3.speaker.beep()
    ev3.speaker.beep()
    ev3.speaker.beep()



    

run()
#ev3.speaker.say("Why are you late Fabian")







