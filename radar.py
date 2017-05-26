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
GAIN = 1
distance = 0

#channels for radars are as follows:
#forward = 1
#right = 2
#left = 3


print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

while True:
    # Read all the ADC channel values in a list.
    values=[0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN)
        distance = 5.005*values[1]
    
    print("Object is %s mm away" %distance)
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    
    time.sleep(0.5)
