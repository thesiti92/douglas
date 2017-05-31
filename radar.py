#Mateen Tabatabaei

import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 2/3
distance = 0
converg_factor = 0.156254768517
#channels for radars are as follows:
#forward = 0
#right = 1
#left = 2


print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

def brake(dist):
	print('**********Breaking! Object detected {0:>3} meters away**********'.format(distance))
	time.sleep(1)

def stop(dist):
	print('HARD STOP: OBJECT DETECTED IN {0:<3} METERS'.format(dist))

def drive():
	print('No object detected. Smooth sailing!')
	time.sleep(1)

while True:
    # Read all the ADC channel values in a list.
    
   	adc_num = adc.read_adc(0,GAIN)
   	distance = adc_num*converg_factor/1000
   	print('ADC is: {0:>6}'.format(adc_num))
   	print("")
   	print('Distance is: {0:<6} meters'.format(distance))
   	print("")
    #print (values[1])
    #print("Object is %s mm away" %distance)
	#print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    #print("")

   	if distance > 5:
   		drive()
   	elif 3 < distance < 5:
   		brake(distance)
   	elif distance < 3:
   		stop(distance)
   	else:
   		drive()

   	time.sleep(.5)



