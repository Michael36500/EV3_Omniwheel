#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

import math

# setup kostka, stopky
ev3 = EV3Brick()

# setup motory 
m_lu = Motor(Port.A)
m_ru = Motor(Port.C)
m_rd = Motor(Port.B)
m_ld = Motor(Port.D)

# where = ve stupních, dokola
# rychlost = rychlost
# kolik = o kolik se posune (součet otočení všech motorů)
def run_m (lu, ru, rd, ld):
    global m_lu
    global m_ru
    global m_rd
    global m_ld
    
    rd *= -1
    ld *= -1

    m_lu.dc(lu)
    m_ru.dc(ru)
    m_rd.dc(rd)
    m_ld.dc(ld)
    wait(1000)

def stop_m ():
    global m_lu
    global m_ru
    global m_rd
    global m_ld
    
    m_lu.hold()
    m_ru.hold()
    m_rd.hold()
    m_ld.hold()
    wait(500)
# rych = rychlost
def move(angle, rych):
    global m_lu
    global m_ru
    global m_rd
    global m_ld

    toc_ang = angle + 45
    toc_ang %= 360

    # rychx =
    # rychy = 


    
    # ru a ld jsou \, rd a lu jsou /

    # run_m ()
    wait(2000)

run_m(20,20,20,20)
wait(5000)
