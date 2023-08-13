import subprocess
import os
import qwiic_vl53l1x
import time
import utils

# def sensor_reset(sensor):
#     #  sensor = ToF # Comment out this line before running
#      SOFT_RESET = 0x0000
#      status = 0
#      status = sensor.__i2cWrite(sensor.address,SOFT_RESET,0x01,1)
#      time.sleep(0.1)
#      return status


print("VL53L1X Qwiic Test\n")
ToF = qwiic_vl53l1x.QwiicVL53L1X()

if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")

"""
	def sensor_reset(self):
		self.status = 0
		self.status = self.__i2cWrite(self.address, SOFT_RESET, 0x01, 1)
		self.sensor_init()

		return self.status
"""

# Turn screen off: subprocess.call('xset dpms force off', shell=True)
# Turn screen on: subprocess.call('xset dpms force on', shell=True)

screen_state = utils.screen_status()
zero_counter = 0
prev_dist = 0
hang_counter = 0

while True:
    try:
        ToF.start_ranging()						 # Write configuration bytes to initiate measurement
        time.sleep(0.05)
        # print("Data ready: {}".format(ToF.check_for_data_ready()))
        distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
        time.sleep(0.05)
        ToF.stop_ranging()
        time.sleep(.05)

        if distance == 0:
             zero_counter += 1
             print(zero_counter)

        if zero_counter > 10:
             ToF.sensor_init() 
             time.sleep(0.05)            

        if screen_state and distance > 1200:
            utils.screen_off()
            screen_state = False
        elif not screen_state and distance < 300:
            utils.screen_on()
            screen_state = True

        if prev_dist == distance:
            hang_counter += 1
        else:
             hang_counter = 0
             prev_dist = distance

        # distanceInches = distance / 25.4
        # distanceFeet = distanceInches / 12.0

		# print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))
        # print("Distance(mm): %s" % (distance))
        if hang_counter:
            print("Distance(mm): {:4d}  {:5d}".format(distance, hang_counter)) 
        else:
            print("Distance(mm): {:4d}".format(distance))

    except Exception as e:
        print(e)