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
    if ".LEFT" in str(buts):
        fn.UDLR(50,0,0)
        
    if ".DOWN" in str(buts):
        fn.UDLR(0,0,-100)
        
    if ".RIGHT" in str(buts):
        fn.UDLR(-50,0,0)
        
    if ".UP" in str(buts):
        fn.UDLR(0,0,100)
        
    print(buts)
    fn.stop_m()
