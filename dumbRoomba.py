#GPIOs imports
import RPi.GPIO as GPIO
import time
#lidar imports and setup
from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')
import threading
#initializing motors
in1 = 24
in2 = 23
en = 25
in3 = 22
in4 = 27
en2 = 17
temp1=1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
temp1=1
#secondmotor
GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p2=GPIO.PWM(en2,1000)
pTemp = 80
pTemp2 = 80
#initial duty cycle set to "medium"(1-99)
p.start(pTemp)
p2.start(pTemp)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.LOW)


def turn90(dist,scan):
    print("HIT")
    p.ChangeDutyCycle(75)
    p2.ChangeDutyCycle(75)
    while(dist<500.00):
        for scan in lidar.iter_scans():
            for (_, angle, distance) in scan:
                if angle < 185 and angle > 175:
                    GPIO.output(in1,GPIO.HIGH)
                    GPIO.output(in2,GPIO.LOW)
                    GPIO.output(in3,GPIO.LOW)
                    GPIO.output(in4,GPIO.HIGH)
                    dist = distance
                    print(dist)
    print("LEAVING")
    
        


try:
    tempFront = ""
    tempLeft = ""
    while(1):
        for scan in lidar.iter_scans():
            for (_, angle, distance) in scan:
                
                #FRONT
                if angle < 185 and angle > 175:
                    if tempFront == "turn90":
                        print("hit180")
                        GPIO.output(in1,GPIO.HIGH)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.LOW)
                        GPIO.output(in4,GPIO.HIGH)
                        if distance > 500:
                            tempFront = ""
                            print("exit")
                    else:
                        GPIO.output(in1,GPIO.HIGH)
                        GPIO.output(in2,GPIO.LOW)
                        GPIO.output(in3,GPIO.HIGH)
                        GPIO.output(in4,GPIO.LOW)
                        if distance < 1000 and distance > 750:
                            pTemp = 95
                            pTemp2 = 95
                        if distance < 750 and distance > 500:
                            pTemp = 80
                            pTemp2 = 80
                        if distance < 500:
                            pTemp = 99
                            pTemp2 = 99
                            tempFront = "turn90"                                            
                    
                    p.ChangeDutyCycle(pTemp)
                    p2.ChangeDutyCycle(pTemp2)
                
                #LEFT FRONT
                if angle < 240 and angle > 200:
                    if distance < 400:
                            pTemp = 99
                            pTemp2 = 0
                            print ("turning right")
                    p.ChangeDutyCycle(pTemp)
                    p2.ChangeDutyCycle(pTemp2)
                #LEFT
                if angle < 300 and angle > 240:
                    if distance < 200:
                            pTemp = 99
                            pTemp2 = 50
                            print ("shifting right")
                    p.ChangeDutyCycle(pTemp)
                    p2.ChangeDutyCycle(pTemp2)
                
                #RIGHT FRONT
                if angle < 160 and angle > 120:
                    if distance < 400:
                            pTemp = 0
                            pTemp2 = 99
                            print ("turning left")
                    p.ChangeDutyCycle(pTemp)
                    p2.ChangeDutyCycle(pTemp2)
                #RIGHT
                if angle < 120 and angle > 60:
                    if distance < 200:
                            pTemp = 50
                            pTemp2 = 99
                            print("shifting left")
                    p.ChangeDutyCycle(pTemp)
                    p2.ChangeDutyCycle(pTemp2)
                    
                    
                    """
				if angle < 185 and angle > 175:
					if distance < 200:
						print ("FRONT: " + str(distance))
				if angle < 5 or angle > 355:
					if distance < 500:
						print ("BEHIND: " + str(distance))
				if angle < 95 and angle > 85:
					if distance < 500:
						print ("LEFT: " + str(distance))
				if angle < 275 and angle > 265:
					if distance < 500:
						print ("RIGHT: " + str(distance))
                    """
except KeyboardInterrupt:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    GPIO.cleanup()
    print("YOU DIED")

