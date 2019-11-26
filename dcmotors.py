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


def straight():
    pTemp = 99
    p.ChangeDutyCycle(pTemp)
    p2.ChangeDutyCycle(pTemp)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def flipItAndReverseIt(frontLeft,frontRight):
    if frontLeft == True and frontRight == False:
        pTemp = 90
        pTemp2 = 0
        p.ChangeDutyCycle(pTemp)
        p2.ChangeDutyCycle(pTemp2)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    elif frontLeft == False and frontRight == True:
        pTemp = 0
        pTemp2 = 90
        p.ChangeDutyCycle(pTemp)
        p2.ChangeDutyCycle(pTemp2)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    elif frontLeft ==True and frontRight == True:
        pTemp = 99
        pTemp2 = 60
        p.ChangeDutyCycle(pTemp)
        p2.ChangeDutyCycle(pTemp2)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)


def modifyDirection(leftCorrection,rightCorrection):
    pTemp = 99 - (leftCorrection*3)
    pTemp2 = 99 - (rightCorrection*3)
    p.ChangeDutyCycle(pTemp)
    p2.ChangeDutyCycle(pTemp2)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

#this needs to tell the motors what to do
#given triggers from the left, front, and right list
def decide(leftList,frontList,rightList):
    straightBool = True
    lSum = sum(leftList)
    rSum = sum(rightList)
    lFront = []
    rFront = []

    if len(frontList) > 4 and sum(frontList) != 0:
        for i in range(2,int(len(frontList)/2),1):
            lFront.append(frontList[i])
        for j in range((int(len(frontList)/2)),(len(frontList)-2),1):
            rFront.append(frontList[j])
        if sum(lFront) == 0:
            if sum(rFront) != 0:
                tBool = True
                flipItAndReverseIt( True,False)
        elif sum(lFront) + sum(rFront) > 9:
            flipItAndReverseIt(True,True)
        elif sum(rFront) == 0:
            if sum(lFront) != 0:
                flipItAndReverseIt(False,True)
        straightBool = False
                
    elif (sum(leftList) + sum(rightList) > 0) and sum(frontList) < 10:
        for i in range(len(leftList)):
            if leftList[i] == 2:
                modifyDirection(lSum,rSum)
        for i in range(len(rightList)):
            if rightList[i] == 2:
                modifyDirection(lSum,rSum)
        straightBool = False
    elif straightBool:
        straight()

def clean():
    GPIO.cleanup()
