from djitellopy import tello
import KeyBoard as kp
import cv2
import time
import numpy as np
import math


fSpeed = 117/10
aSpeed = 360/10
interval = 0.25

dInterval = fSpeed*interval
aInterval = aSpeed*interval

x,y = 500,500
a = 0
yaw = 0

kp.init()
me = tello.Tello()
me.connect()
me.streamon()
print(me.get_battery())
points = [(0,0),(0,0)]

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    sp = 20
    asp = 50
    global x, y, yaw, a
    d = 0

    if kp.getKey("LEFT"):
        lr = -sp
        d = dInterval
        a = -180

    elif kp.getKey("RIGHT"):
        lr= sp
        d= -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = sp
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"):
        fb= -sp
        d = -dInterval
        a = -90

    if kp.getKey("w"):
        ud = sp

    elif kp.getKey("s"):
        ud= -sp

    if kp.getKey("a"):
        yv = -asp
        yaw -= aInterval

    elif kp.getKey("d"):
        yv = asp
        yaw += aInterval

    if kp.getKey("l"):
        me.land()


    if kp.getKey("t"):
        me.takeoff()

    if kp.getKey("c"):
        cv2.imwrite(f'/Users/bharath/PycharmProjects/DRONE/photos/{time.time()}.jpg',frame)

    time.sleep(interval)
    a += yaw
    x += int(d*math.cos(math.radians(a)))
    y += int(d*math.sin(math.radians(a)))

    return[lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)
    cv2.putText(img,f'({(points[-1][0] - 500) / 100}, {(points[-1][1] - 500) / 100})m',
                (points[-1][0] + 10, points[-1][1] +30), cv2.FONT_HERSHEY_PLAIN, 1,
    (255, 0, 255),1)

while True:
    val = getKeyboardInput()
    me.send_rc_control(val[0], val[1], val[2], val[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    if(points[-1][0] != val[4] or points [-1][1] != val[5]):
        points.append((val[4], val[5]))

    drawPoints(img, points)
    cv2.imshow("output", img)
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("Drone's POV", frame)
    cv2.waitKey(1)














