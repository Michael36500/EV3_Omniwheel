#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch


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
    
    m_lu.dc(lu)
    m_ru.dc(ru)
    m_ru.dc(rd)
    m_ru.dc(ld)
    wait(2)

def stop_m (lu, ru, rd, ld):
    global m_lu
    global m_ru
    global m_rd
    global m_ld
    
    m_lu.stop()
    m_ru.stop()
    m_ru.stop()
    m_ru.stop()
    wait(2)
# rych = rychlost
# def move(where, rych, kolik):
#     global ev3
#     global m_lu
#     global m_ru
#     global m_rd
#     global m_ld


rych = 50

# rovně
run_m (1 * rych, 1 * rych, -1 * rych, -1 * rych)
stop_m()

# doleva
run_m (-1 * rych, 1 * rych, 1 * rych, -1 * rych)
stop_m()

# dozadu
run_m (-1 * rych, -1 * rych, 1 * rych, 1 * rych)
stop_m()

# doprava
run_m (1 * rych, -1 * rych, -1 * rych, 1 * rych)
stop_m()



