# Add your Python code here. E.g.
from microbit import *
import os
# compass calibration
if not compass.is_calibrated():
    compass.calibrate()

# main loop
while True:
    # prepare data
    comp = compass.heading()
    temp = temperature()
    content = str(comp) + ',' + str(temp)
    # optional addition(first part)
    display.scroll(content, wait=False, loop=True)
    file_list = os.listdir()
    # if data.csv exist
    if 'data.csv' in file_list:
        # load current file
        data_in = open('data.csv', 'r')
        old = data_in.read()
        data_in.close()
        # update the data file
        data_out = open('data.csv', 'w')
        data_out.write(old + content + '\n')
        data_out.close()
    # if data.csv not exist, build a file and save the data
    else:
        data_out = open('data.csv', 'w')
        data_out.write(content + '\n')
        data_out.close()
    sleep(10000)
    
