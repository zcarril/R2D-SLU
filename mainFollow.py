#python file that controls the motors
import dcFollow
#for math stuff
import math
#average angle program
#lidar imports and setup
from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')
#for threading(if needed)
import threading
from operator import itemgetter
temp1 = 0
temp2 = 0
distanceConst = 400

def avgList(avg, *args):
    if avg[0] != []:
        avgL = avg[0]
        dist = 0
        for i in range(len(avgL)):
            dist += avgL[i]
        dist = dist/(len(avgL))
        return dist

def getThresh(ang, *args):
    if ang[1] != []:
        base = 0
        dist = distanceConst
        angle = ang[1]
        midAngle = angle[int(len(angle)/2)]
        if abs(midAngle-90) < 45:
            base = 90
        elif abs(midAngle-180) < 45:
            base = 180
        elif abs(midAngle-270) < 45:
            base = 270
        midAngle = abs(base - midAngle)
        threshold = dist/math.cos(math.radians(midAngle))
        return threshold

def getAvgAngle(ang, *args):
    if ang[1] != []:
        angle = ang[1]
        midAngle = angle[int(len(angle)/2)]
        return midAngle

    

def printSame(num, check, limit):
    x=0
    dConstMedium = limit
    dConstClose = limit-100
    if check == False:
        if num < dConstClose:
            x=2
            print("# ", end=" ")
        elif num < dConstMedium:
            x=1
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    if check == True:
        if num < dConstClose:
            x=2
            print("#")
        elif num < dConstMedium:
            x=1
            print("*")
        else:
            print(" ")
    return x



try:
    while(1):
        for scan in lidar.iter_scans():
            #setting up lists while clearing every iteration
            main=[]
            fList1,fList2,fList3,fList4,fList5,fList6,fList7,fList8,fList9,fList10 = ([] for i in range(10))
            lList1,lList2,lList3,lList4,lList5,lList6,lList7,lList8,lList9,lList10 = ([] for i in range(10))
            rList1,rList2,rList3,rList4,rList5,rList6,rList7,rList8,rList9,rList10 = ([] for i in range(10))

            #setting up average variables while clearing every iteration
            fAvg1,fAvg2,fAvg3,fAvg4,fAvg5,fAvg6,fAvg7,fAvg8,fAvg9,fAvg10 = (0 for i in range(10))
            lAvg1,lAvg2,lAvg3,lAvg4,lAvg5,lAvg6,lAvg7,lAvg8,lAvg9,lAvg10 = (0 for i in range(10))
            rAvg1,rAvg2,rAvg3,rAvg4,rAvg5,rAvg6,rAvg7,rAvg8,rAvg9,rAvg10 = (0 for i in range(10))
            
            #TODO need to have list for angles
            fAng1,fAng2,fAng3,fAng4,fAng5,fAng6,fAng7,fAng8,fAng9,fAng10 = ([] for i in range(10))
            lAng1,lAng2,lAng3,lAng4,lAng5,lAng6,lAng7,lAng8,lAng9,lAng10 = ([] for i in range(10))
            rAng1,rAng2,rAng3,rAng4,rAng5,rAng6,rAng7,rAng8,rAng9,rAng10 = ([] for i in range(10))
            
            #new list of triggers to motors
            mListLeft,mListFront,mListRight=([] for i in range(3))
            targetCount = 0
            for (_, angle, distance) in scan:
                #Left
                #L1
                if angle > 45  and angle <= 54:
                    lList1.append(distance)
                    lAng1.append(angle)
                #L2
                if angle > 54 and angle <= 63:
                    lList2.append(distance)
                    lAng2.append(angle)
                #L3
                if angle > 63 and angle <= 72:
                    lList3.append(distance)
                    lAng3.append(angle)
                #L4
                if angle > 72 and angle <= 81:
                    lList4.append(distance)
                    lAng4.append(angle)
                #L5
                if angle > 81 and angle <= 90:
                    lList5.append(distance)
                    lAng5.append(angle)
                #L6
                if angle > 90 and angle <= 99:
                    lList6.append(distance)
                    lAng6.append(angle)
                #L7
                if angle > 99 and angle <= 108:
                    lList7.append(distance)
                    lAng7.append(angle)
                #L8
                if angle > 108 and angle <= 117:
                    lList8.append(distance)
                    lAng8.append(angle)
                #L9
                if angle > 117 and angle <= 126:
                    lList9.append(distance)
                    lAng9.append(angle)
                #L10
                if angle > 126 and angle <= 135:
                    lList10.append(distance)
                    lAng10.append(angle)
                
                #Front
                #F1
                if angle > 135 and angle <= 144:
                    fList1.append(distance)
                    fAng1.append(angle)
                #F2
                if angle > 144 and angle <= 153:
                    fList2.append(distance)
                    fAng2.append(angle)
                #F3
                if angle > 153 and angle <= 162:
                    fList3.append(distance)
                    fAng3.append(angle)
                #F4
                if angle > 162 and angle <= 171:
                    fList4.append(distance)
                    fAng4.append(angle)
                #F5
                if angle > 171 and angle <= 180:
                    fList5.append(distance)
                    fAng5.append(angle)
                #F6
                if angle > 180 and angle <= 189:
                    fList6.append(distance)
                    fAng6.append(angle)
                #F7
                if angle > 189 and angle <= 198:
                    fList7.append(distance)
                    fAng7.append(angle)
                #F8
                if angle > 198 and angle <= 207:
                    fList8.append(distance)
                    fAng8.append(angle)
                #F9
                if angle > 207 and angle <= 216:
                    fList9.append(distance)
                    fAng9.append(angle)
                #F10
                if angle > 216 and angle <= 225:
                    fList10.append(distance)
                    fAng10.append(angle)
                
                #RIGHT
                #R1
                if angle > 225 and angle <= 234:
                    rList1.append(distance)
                    rAng1.append(angle)
                #R2
                if angle > 234 and angle <= 243:
                    rList2.append(distance)
                    rAng2.append(angle)
                #R3
                if angle > 243 and angle <= 252:
                    rList3.append(distance)
                    rAng3.append(angle)
                #R4
                if angle > 252 and angle <= 261:
                    rList4.append(distance)
                    rAng4.append(angle)
                #R5
                if angle > 261 and angle <= 270:
                    rList5.append(distance)
                    rAng5.append(angle)
                #R6
                if angle > 270 and angle <= 279:
                    rList6.append(distance)
                    rAng6.append(angle)
                #R7
                if angle > 279 and angle <= 288:
                    rList7.append(distance)
                    rAng7.append(angle)
                #R8
                if angle > 288 and angle <= 297:
                    rList8.append(distance)
                    rAng8.append(angle)
                #R9
                if angle > 297 and angle <= 306:
                    rList9.append(distance)
                    rAng9.append(angle)
                #R10
                if angle > 306 and angle <= 315:
                    rList10.append(distance)
                    rAng10.append(angle)
                    
                    
            #creating distance list and (empty) average variable touples
            #TODO: put list of angles instead of "lAvg1"
            main.extend(((lList1,lAng1),
                         (lList2,lAng2),
                         (lList3,lAng3),
                         (lList4,lAng4),
                         (lList5,lAng5),
                         (lList6,lAng6),
                         (lList7,lAng7),
                         (lList8,lAng8),
                         (lList9,lAng9),
                         (lList10,lAng10),
                         (fList1,fAng1),
                         (fList2,fAng2),
                         (fList3,fAng3),
                         (fList4,fAng4),
                         (fList5,fAng5),
                         (fList6,fAng6),
                         (fList7,fAng7),
                         (fList8,fAng8),
                         (fList9,fAng9),
                         (fList10,fAng10),
                         (rList1,rAng1),
                         (rList2,rAng2),
                         (rList3,rAng3),
                         (rList4,rAng4),
                         (rList5,rAng5),
                         (rList6,rAng6),
                         (rList7,rAng7),
                         (rList8,rAng8),
                         (rList9,rAng9),
                         (rList10,rAng10)))
            
            #iterating through list of touples
            for i in range(len(main)):  
                avgDist = avgList(main[i])
                thresh = getThresh(main[i])
                angle = getAvgAngle(main[i]) #get angle here
                endLine = False
                if avgDist != None:
                    if i < len(main)-1:
                        if i < 10:
                            mListLeft.append(printSame(avgDist,endLine,thresh))
                        elif i < 20:
                            mListFront.append(printSame(avgDist,endLine,thresh))
                        elif i < 30:
                            mListRight.append(printSame(avgDist,endLine,thresh))
                    else:
                        endLine = True
                        mListRight.append(printSame(avgDist,endLine,thresh))
            #TODO: designate what the motors should given anything.
            #the function below will do that
            
            for i in range(len(main)):
                
                angle = getAvgAngle(main[i]) #get angle here
                dist = avgList(main[i])
                #print (angle)
                if angle is not None:
                    if dist is not None:
                        if (angle > 155 and angle < 205) and (dist > 300 and dist < 1000):
                            targetCount += 1
                            if 180-angle < 0:
                                print("on the right")
                                temp1 = 90 - 3*(abs(180-angle))
                                dcFollow.motors(temp1,90,True)
                            elif 180-angle > 0:
                                print("on the left")
                                temp2 = 90 - 3*(abs(180-angle))
                                dcFollow.motors(90,temp2,True)
                        else:
                            targetCount -= 1
                                    
                        dcFollow.decide(mListLeft,mListFront,mListRight,dist, angle)
            print (targetCount)    
            if targetCount <= -30:
                dcFollow.motors(0,0,True)
                print("LOST")

except KeyboardInterrupt:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    dcFollow.clean()
    print("YOU DIED")
