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
    tempFront = ""
    tempLeft = ""
    while(1):
        for scan in lidar.iter_scans():
            #setting up lists while clearing every iteration
            main = []
            fList1 = []
            fList2 = []
            fList3 = []
            fList4 = []
            fList5 = []
            fList6 = []
            fList7 = []
            fList8 = []
            fList9 = []
            fList10 = []
            
            #setting up average variables while clearing every iteration
            fAvg1 = 0
            fAvg2 = 0
            fAvg3 = 0
            fAvg4 = 0
            fAvg5 = 0
            fAvg6 = 0
            fAvg7 = 0
            fAvg8 = 0
            fAvg9 = 0
            fAvg10 = 0
            for (_, angle, distance) in scan:
                
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
                if angle > 207 and angle <= 216:
                    fList10.append(distance)
                    
                    
            #creating distance list and (empty) average variable touples
            main.extend(((fList1,fAvg1),
                         (fList2,fAvg2),
                         (fList3,fAvg3),
                         (fList4,fAvg4),
                         (fList5,fAvg5),
                         (fList6,fAvg6),
                         (fList7,fAvg7),
                         (fList8,fAvg8),
                         (fList9,fAvg9),
                         (fList10,fAvg10)))
            
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