#!/usr/bin/python
import serial
import requests
import time
import atexit
import os
import sys

pid = str(os.getpid())
pidfile = "/tmp/light.pid"


file(pidfile, 'w').write(pid)

def goodbye():
    os.remove(pidfile)

atexit.register(goodbye)


state = 0;

ser = serial.Serial('/dev/ttyACM0', 9600)
while True:

    temp = ser.readline()
    temp = temp.rstrip()
    print("http://home.tomasharkema.nl/light/"+temp+"/")
    r = requests.get("http://home.tomasharkema.nl/light/"+temp+"/")
    time.sleep(60)