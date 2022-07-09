#!/usr/bin/env pybricks-micropython
# tohole musí být 1. rádek

# importy
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
import sys

import functions as fn

# setup kostka, stopky
ev3 = EV3Brick()

# setup motory 
m_lu = Motor(Port.A)
m_ru = Motor(Port.C)
m_rd = Motor(Port.B)
m_ld = Motor(Port.D)

while True:
    buts = ev3.buttons.pressed()
    if "LEFT" in str(buts):
        fn.move(0, 50)
        # wait(500)
        
    if "DOWN" in str(buts):
        fn.move(90, 50)
        # wait(500)
        
    if "RIGHT" in str(buts):
        fn.move(180, 50)
        # wait(500)
        
    if "UP" in str(buts):
        fn.move(270, 50)
        # wait(500)
        
    if "CENTER" in str(buts):
        fn.rot(100)
        # wait(500)
        
    print(buts)
    fn.stop_m()
