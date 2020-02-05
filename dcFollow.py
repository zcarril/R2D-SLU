import RPi.GPIO as GPIO
from time import sleep

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
#initial duty cycle
p.start(pTemp)
p2.start(pTemp)

#SIDE NOTE/ LEGEND
# p = right
# p2 = left
global gCheck
global gCount
gCount = 10000

def motors(pT1, p2, sameDirection):
    p.ChangeDutyCycle(pT1)
    p2.ChangeDutyCycle(pT2)
    if sameDirection == True:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW) 
    else:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)

def straight():
    motors(99,99,True)

def flipItAndReverseIt(frontLeft,frontRight):
    if frontLeft == True and frontRight == False:
        motors(90,60,True)
    elif frontLeft == False and frontRight == True:
        motors(60,90,True)
    elif frontLeft ==True and frontRight == True:
        motors(60,60,False)

def modifyDirection(leftCorrection,rightCorrection):
    pTemp = 99 - (leftCorrection*3)
    pTemp2 = 99 - (rightCorrection*3)
    motors(pTemp,pTemp2,True)
    
    
#following stuff
def follow (dist, angle):
    dConst = 0
    if angle is not None:
        if dist is not None:
            if angle < 200 and angle > 160:
                if dist < 800 and dist > 500:
                    dConst = dist
                    #set var here
                    if angle < 175:
                        while (count > 0):
                            flipItAndReverseIt( True,False)
                            check -= 1
                    #set var here
                    elif angle > 185:
                        while (count > 0):
                            flipItAndReverseIt( False,True)
                            check -= 1
                    #set var here
                    else:
                        while (count > 0):
                            straight()
                            check -= 1
                else:
                    flipItAndReverseIt(True,True)
            #set if var cleared
            else:
                motors(0,0,True)

#this needs to tell the motors what to do
#given triggers from the left, front, and right list
def decide(leftList,frontList,rightList, dist, angle):
    followBool = True
    lSum = sum(leftList)
    rSum = sum(rightList)
    lFront = []
    rFront = []
                
    if (sum(leftList) + sum(rightList) > 0) and sum(frontList) < 10:
        for i in range(len(leftList)):
            if leftList[i] == 2:
                modifyDirection(lSum,rSum)
        for i in range(len(rightList)):
            if rightList[i] == 2:
                modifyDirection(lSum,rSum)
        followBool = False
    elif followBool:
        #globalCheck = follow(dist, angle)
        dConst = 0
        if angle is not None:
            if dist is not None:
                if angle < 200 and angle > 160:
                    if dist < 800 and dist > 500:
                        dConst = dist
                        #set var here for left (l)
                        if angle < 175 or gCheck == "l":
                            gCheck = "l"
                            flipItAndReverseIt( True,False)
                        #set var here for right (r)
                        elif angle > 185 or gCheck == "r":
                            gCheck = "r"
                            flipItAndReverseIt( False,True)
                        #set var here for straight (s)
                        else:
                            straight()
                            check -= 1
                    elif gCount > 0:
                        flipItAndReverseIt(True,True)
                        gCount -= 1
                        gCheck = ""
                #set if var cleared
                else:
                    motors(0,0,True)

def clean():
    GPIO.cleanup()
