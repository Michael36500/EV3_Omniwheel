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
# def move(angle, rych):
#     global m_lu
#     global m_ru
#     global m_rd
#     global m_ld

#     toc_ang = angle + 45
#     toc_ang %= 360
# def move(theta, power, turn):
#     sin = math.sin(theta - math.pi/4)
#     cos = math.cos(theta - math.pi/4)
#     maxi = max(abs(sin), abs(sin))

#     lu = int(power * cos / maxi + turn)
#     ru = int(power * sin / maxi - turn)
#     rd = int(power * sin / maxi + turn)
#     ld = int(power * cos / maxi - turn)

#     print(lu, ru, rd, ld)

#     run_m(lu, ru, rd, ld)
#     # rychx =
#     # rychy = 


    
#     # ru a ld jsou \, rd a lu jsou /

#     # run_m ()
#     wait(2000)

# run_m(20,20,20,20)
# ud - +dopředu -dozadu
# lr - vlevo vpravo (+ vpravo, - vlevo)
# rot - otáčení (+ posměru/doprava, - protisměru/doleva)
def move(ud, lr, rot):
    lu = ud + lr + rot
    ru = ud - lr - rot
    rd = ud + lr - rot
    ld = ud - lr + rot

    run_m(lu, ru, rd, ld)




move(20, 0, 0)
wait(2000)
move(-20, 0, 0)
wait(2000)
move(0, 0, 20)
wait(2000)
move(0, 0, -20)
wait(2000)
