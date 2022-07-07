#!/usr/bin/env pybricks-micropython
# !! please, all comments are in czech...
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

# funkce, co roztočí motory podle vstupu
def run_m (lu, ru, rd, ld):
    global m_lu
    global m_ru
    global m_rd
    global m_ld

    lu = round(lu)
    ru = round(ru)
    rd = round(rd)
    ld = round(ld)    
    
    rd *= -1
    ld *= -1

    m_lu.dc(lu)
    m_ru.dc(ru)
    m_rd.dc(rd)
    m_ld.dc(ld)

# funkce, co zastaví motory
def stop_m ():
    global m_lu
    global m_ru
    global m_rd
    global m_ld
    
    m_lu.hold()
    m_ru.hold()
    m_rd.hold()
    m_ld.hold()

# funkce z vstupu se pohne nahoru/dolů/otočí se
def UDLR(ud, lr, rot):
    lu = ud + lr + rot
    ru = ud - lr - rot
    rd = ud + lr - rot
    ld = ud - lr + rot

    run_m(lu, ru, rd, ld)

# funkce z vstupní úhle se pohne tím úhlem a tou rychlostí
def move(theta, power):
    theta = math.radians(theta)     #!!!!!!!!!!!!!!!!!!!! FAKING RADIANS

    vx = power * math.sin(theta)
    vy = power * math.cos(theta)
    # print(vx, vy)
    UDLR(vx, vy, 0)


# some code
# for _ in range (20):
    # move(0, 40)
    # wait(1000)
    # move(90, 40)
    # wait(1000)
    # move(180, 40)
    # wait(1000)
    # move(270, 40)
    # wait(1000)
for _ in range(10):
    for angle in range(360):
        move(angle, 100)
    for angle in range(360):
        move(-1 * angle, 100)
    stop_m()


