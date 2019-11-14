#GPIOs imports
import RPi.GPIO as GPIO
import time
#lidar imports and setup
from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')
import threading


try:
    while(1):
        for scan in lidar.iter_scans():
            for (_, angle, distance) in scan:
                
                #FRONT
                if angle < 185 and angle > 175:
                    p2.ChangeDutyCycle(pTemp2)
                
                #LEFT FRONT
                if angle < 240 and angle > 200:
                    if distance < 400:
                #LEFT 
                if angle < 300 and angle > 240:
                
                #RIGHT FRONT
                if angle < 160 and angle > 120:
                #RIGHT
                if angle < 120 and angle > 60:
                    
                    

except KeyboardInterrupt:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    print("YOU DIED")

