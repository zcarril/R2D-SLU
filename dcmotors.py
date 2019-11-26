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

#correct
def turnLeft():
    pTemp = 99
    pTemp2 = 0
    p.ChangeDutyCycle(pTemp)
    p2.ChangeDutyCycle(pTemp2)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)


def straight():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def flipItAndReverseIt(frontLeft,frontRight):
    if frontLeft == True and frontRight == False:
        pTemp = 99
        pTemp2 = 0
        p.ChangeDutyCycle(pTemp)
        p2.ChangeDutyCycle(pTemp2)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    elif frontLeft == False and frontRight == True:
        pTemp = 0
        pTemp2 = 99
        p.ChangeDutyCycle(pTemp)
        p2.ChangeDutyCycle(pTemp2)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    elif frontLeft ==True and frontRight == True:
        pTemp = 60
        pTemp2 = 99
        p.ChangeDutyCycle(pTemp)
        p2.ChangeDutyCycle(pTemp2)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)


def modifyDirection(leftCorrection,rightCorrection):
    pTemp = 99 - (leftCorrection*4)
    pTemp2 = 99 - (rightCorrection*4)
    p.ChangeDutyCycle(pTemp)
    p2.ChangeDutyCycle(pTemp2)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

#this needs to tell the motors what to do
#given triggers from the left, front, and right list
def decide(leftList,frontList,rightList):
    lSum = sum(leftList)
    rSum = sum(rightList)
    lFront = []
    rFront = []
    if sum(frontList) != 0:
        for i in range(int(len(frontList)/2)):
            lFront.append(frontList[i])
        for j in range((int(len(frontList)/2)),(len(frontList)),1):
            rFront.append(frontList[j])
        if sum(lFront) == 0:
            if sum(rFront) != 0:
                flipItAndReverseIt(True,False)
        elif sum(rFront) == 0:
            if sum(lFront) != 0:
                flipItAndReverseIt(False,True)
        elif sum(lFront) != 0 and sum(rFront) != 0:
            flipItAndReverseIt(True,True)
    else:
        modifyDirection(lSum,rSum)

def clean():
    GPIO.cleanup()
