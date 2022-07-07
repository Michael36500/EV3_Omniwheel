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

a_lu = []
a_ru = []
a_rd = []
a_ld = []


# where = ve stupních, dokola
# rychlost = rychlost
# kolik = o kolik se posune (součet otočení všech motorů)
def run_m (lu, ru, rd, ld):
    global m_lu
    global m_ru
    global m_rd
    global m_ld

    global a_lu
    global a_ru
    global a_rd
    global a_ld
    
    rd *= -1
    ld *= -1

    m_lu.dc(lu)
    m_ru.dc(ru)
    m_rd.dc(rd)
    m_ld.dc(ld)

    a_lu.append(m_lu.speed())
    a_ru.append(m_ru.speed())
    a_rd.append(m_rd.speed())
    a_ld.append(m_ld.speed())

    print()

    print("lu", lu, end = "   ")
    print("ru", ru, end = "   ")
    print("rd", rd, end = "   ")
    print("ld", ld, end = "   ")
    
    print()
    print()


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


def UDLR(ud, lr, rot):
    lu = ud + lr + rot
    ru = ud - lr - rot
    rd = ud + lr - rot
    ld = ud - lr + rot

    run_m(lu, ru, rd, ld)

def move(theta, power):
    # sin = math.sin(theta - math.pi / 4)
    # cos = math.cos(theta - math.pi / 4)
    sin = math.sin(theta - 3.14 / 4)
    cos = math.cos(theta - 3.14 / 4)

    run_m(power * cos, power * sin, power * cos, power * sin)


rot = 0
for _ in range (50):
    # print(rot)
    rot += 1
    move(rot, 30)
    
for a in 

