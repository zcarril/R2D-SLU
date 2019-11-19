#average angle program
#lidar imports and setup
from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')
import threading

distanceConst = 400

def avgList(avg, *args):
    if avg[0] != []:
        avgL = avg[0]
        dist = avg[1]
        for i in range(len(avgL)):
            dist += avgL[i]
        dist = dist/(len(avgL))
        return dist



def printSame(num, check):
    dConstMedium = 800
    dConstClose = 400
    try:
        if check == False:
            if num < dConstClose:
                print("# ", end=" ")
            elif num < dConstMedium:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        if check == True:
            if num < dConstClose:
                print("#")
            elif num < dConstMedium:
                print("*")
            else:
                print(" ")
    except TypeError:
        print("big oof")


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
            
         
            for (_, angle, distance) in scan:
                #Left
                #L1
                if angle > 45  and angle <= 54:
                    lList1.append(distance)
                #L2
                if angle > 54 and angle <= 63:
                    lList2.append(distance)
                #F3
                if angle > 63 and angle <= 72:
                    lList3.append(distance)
                #F4
                if angle > 72 and angle <= 81:
                    lList4.append(distance)
                #F5
                if angle > 81 and angle <= 90:
                    lList5.append(distance)
                #F6
                if angle > 90 and angle <= 99:
                    lList6.append(distance)
                #F7
                if angle > 99 and angle <= 108:
                    lList7.append(distance)
                #F8
                if angle > 108 and angle <= 117:
                    lList8.append(distance)
                #F9
                if angle > 117 and angle <= 126:
                    lList9.append(distance)
                #F10
                if angle > 126 and angle <= 135:
                    lList10.append(distance)
                
                #Front
                #F1
                if angle > 135 and angle <= 144:
                    fList1.append(distance)
                #F2
                if angle > 144 and angle <= 153:
                    fList2.append(distance)
                #F3
                if angle > 153 and angle <= 162:
                    fList3.append(distance)
                #F4
                if angle > 162 and angle <= 171:
                    fList4.append(distance)
                #F5
                if angle > 171 and angle <= 180:
                    fList5.append(distance)
                #F6
                if angle > 180 and angle <= 189:
                    fList6.append(distance)
                #F7
                if angle > 189 and angle <= 198:
                    fList7.append(distance)
                #F8
                if angle > 198 and angle <= 207:
                    fList8.append(distance)
                #F9
                if angle > 207 and angle <= 216:
                    fList9.append(distance)
                #F10
                if angle > 216 and angle <= 225:
                    fList10.append(distance)
                
                #RIGHT
                #R1
                if angle > 225 and angle <= 234:
                    rList1.append(distance)
                #R2
                if angle > 234 and angle <= 243:
                    rList2.append(distance)
                #R3
                if angle > 243 and angle <= 252:
                    rList3.append(distance)
                #R4
                if angle > 252 and angle <= 261:
                    rList4.append(distance)
                #R5
                if angle > 261 and angle <= 270:
                    rList5.append(distance)
                #R6
                if angle > 270 and angle <= 279:
                    rList6.append(distance)
                #R7
                if angle > 279 and angle <= 288:
                    rList7.append(distance)
                #R8
                if angle > 288 and angle <= 297:
                    rList8.append(distance)
                #R9
                if angle > 297 and angle <= 306:
                    rList9.append(distance)
                #R10
                if angle > 306 and angle <= 315:
                    rList10.append(distance)
                    
                    
            #creating distance list and (empty) average variable touples
            #TODO: put list of angles instead of "lAvg1"
            main.extend(((lList1,lAvg1),
                         (lList2,lAvg2),
                         (lList3,lAvg3),
                         (lList4,lAvg4),
                         (lList5,lAvg5),
                         (lList6,lAvg6),
                         (lList7,lAvg7),
                         (lList8,lAvg8),
                         (lList9,lAvg9),
                         (lList10,lAvg10),
                         (fList1,fAvg1),
                         (fList2,fAvg2),
                         (fList3,fAvg3),
                         (fList4,fAvg4),
                         (fList5,fAvg5),
                         (fList6,fAvg6),
                         (fList7,fAvg7),
                         (fList8,fAvg8),
                         (fList9,fAvg9),
                         (fList10,fAvg10),
                         (rList1,rAvg1),
                         (rList2,rAvg2),
                         (rList3,rAvg3),
                         (rList4,rAvg4),
                         (rList5,rAvg5),
                         (rList6,rAvg6),
                         (rList7,rAvg7),
                         (rList8,rAvg8),
                         (rList9,rAvg9),
                         (rList10,rAvg10)))
            
            #iterating through list of touples
            for i in range(len(main)):
                avgDist = avgList(main[i])
                endLine = False
                if avgDist != None:
                    if i < len(main)-1:
                        printSame(avgDist,endLine)
                    else:
                        endLine = True
                        printSame(avgDist,endLine)

except KeyboardInterrupt:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    print("YOU DIED")