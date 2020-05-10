# Add your Python code here. E.g.
from microbit import *
import random
import time

def generate_mole(n, flag):
    # This function is to generate moles in each round, 
    # n is the maximum number of moles
    # flag is a list initialized with 0, each of which indicates whether the mole is selected
    count = random.randrange(n) + 1  # Choose a number from 1 to n
    i = 0
    # Select count moles randomly
    while i < count:
        index = random.randrange(len(flag))
        if flag[index]==0:
            flag[index]=1
            i = i+1
    return count, flag
    
def set_mole(flag,pins):
    # This function is to set the mole based on the generated list
    for m in range(len(flag)):
        pins[m].write_digital(flag[m])

# Const definition
n = 3 # Maximum lights;
pins = [pin6, pin7, pin8, pin9] # Light controller
btns = [pin1, pin2, pin3, pin4] # Btn controller
flag= [0, 0, 0, 0] # Mole indicator

display.show(Image.SMILE)
while True:
    game=False
    if pin0.read_digital() == 1:
        game=True
        display.scroll('Ready?Go!', wait=True)
        display.off()
        set_mole([0,0,0,0],pins)
        sleep(1000)
    gamestarttime=time.ticks_ms()
    score = 0
    while game:
        # Initialization
        flag = [0,0,0,0]
        count,flag = generate_mole(n,flag)
        set_mole(flag, pins)
        starttime = time.ticks_ms()
        # Game start
        while time.ticks_diff(time.ticks_ms(), starttime) < 1000:
            for idx in range(4):
                if btns[idx].read_digital() == 1 and flag[idx] == 1:
                    # Success
                    pins[idx].write_digital(0)
                    score = score + 1
            sleep(180)

        if time.ticks_diff(time.ticks_ms(), gamestarttime) > 60000:
            game = False
            display.on()
            display.scroll(score)