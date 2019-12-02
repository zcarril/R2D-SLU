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

#TODO add opposite directions the other way
def motors(pT1, pT2, sameDirection):
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
    motors(90,90,True)

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
    


#this needs to tell the motors what to do
#given triggers from the left, front, and right list
def decide(leftList,frontList,rightList, dist, angle):
    followBool = True
    lSum = sum(leftList)
    rSum = sum(rightList)
    lFront = []
    rFront = []
    
    #removing analysis of front angles bc following needs to happen instead of avoidance            
    #if (sum(leftList) + sum(rightList) > 0) and sum(frontList) < 10:
    #print("Side avoidance count: " + str(sum(leftList) + sum(rightList)))
    if (sum(leftList) + sum(rightList) > 5):
        for i in range(len(leftList)):
            if leftList[i] == 2:
                modifyDirection(lSum,rSum)
        for i in range(len(rightList)):
            if rightList[i] == 2:
                modifyDirection(lSum,rSum)
        followBool = False

def clean():
    GPIO.cleanup()
