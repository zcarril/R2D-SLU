from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')


while(1):
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            #print (str(angle) + " "+ str(distance)+"\n")
            if angle < 181 and angle > 179:
                print(distance)


"""
			if angle < 185 and angle > 175:
				if distance < 500:
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

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
