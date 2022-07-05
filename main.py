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

m_lu.dc(-30)
wait(1000)
# where = ve stupních, dokola
# rychlost = rychlost
# kolik = o kolik se posune (součet otočení všech motorů)
def run_m (lu, ru, rd, ld):
    global m_lu
    global m_ru
    global m_rd
    global m_ld
    
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

    rychx = rych * math.cos(angle)
    rychy = rych * math.sin(angle)
    run_m (rychx + rychy, rychx - rychy, -1 * (rychx + rychy), -1 * (rychx - rychy))

# def move(angle, rych):
#     rychx =

move(45, 30)
# wait(5000)
# x = 0
# y = 20
# while True:
#     x = x % 40
#     y = y % 40
    
#     x += 2
#     y += 2

#     print(x, y)

#     run_m (x,y, x*-1, y*-1)

#     wait(10)
# rych = 20
# while True:
#     for phase in range (0, 1, 0.01):
#         run_m(phase)


#         wait(100)

