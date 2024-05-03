from djitellopy import tello
import KeyBoard as kp
import cv2
import time
import numpy as np
import math

global img


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


me.streamon()


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    sp = 50


    if kp.getKey("LEFT"):
        lr = -sp


    elif kp.getKey("RIGHT"):
        lr= sp


    if kp.getKey("UP"):
        fb = sp


    elif kp.getKey("DOWN"):
        fb= -sp


    if kp.getKey("w"):
        ud = sp

    elif kp.getKey("s"):
        ud= -sp

    if kp.getKey("a"):
        yv = -sp


    elif kp.getKey("d"):
        yv = sp


    if kp.getKey("l"):
        me.land()


    if kp.getKey("t"):
        me.takeoff()


    if kp.getKey("c"):
        cv2.imwrite(f'/Users/bharath/PycharmProjects/DRONE/photos/{time.time()}.jpg',frame)


    return[lr, fb, ud, yv,]


while True:
    val = getKeyboardInput()
    me.send_rc_control(val[0], val[1], val[2], val[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("Drone's POV", frame)
    cv2.waitKey(1)













