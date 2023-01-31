import subprocess
import os
import qwiic_vl53l1x
import time

print("VL53L1X Qwiic Test\n")
ToF = qwiic_vl53l1x.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")

# Turn screen off: subprocess.call('xset dpms force off', shell=True)
# Turn screen on: subprocess.call('xset dpms force on', shell=True)

os.environ['DISPLAY'] = ':0.0'
screen_on = True
subprocess.call('xset dpms force on', shell=True)


while True:
    try:
        ToF.start_ranging()						 # Write configuration bytes to initiate measurement
        time.sleep(.05)
        distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
        if screen_on and distance > 1000:
            subprocess.call('xset dpms force off', shell=True)
            screen_on = False
        elif not screen_on and distance < 300:
            subprocess.call('xset dpms force on', shell=True)
            screen_on = True
        time.sleep(.05)
        ToF.stop_ranging()

        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0

		# print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))
        print("Distance(mm): %s" % (distance))

    except Exception as e:
        print(e)