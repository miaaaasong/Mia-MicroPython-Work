# Add your Python code here. E.g.
from microbit import *
import random

def generate_mole(n, flag):
    # This function is to generate moles in each round, 
    # n is the maximum number of moles
    # flag is a list initialized with 0, each of which indicates whether the mole is selected
    count = random.randint(1,n)  # Choose a number from 1 to n
    i = 0
    # Select count moles randomly
    while i < count:
        index = random.randint(0,len(flag)-1)
        if flag[index]==0:
            flag[index]=1
            i = i+1
    return count, flag
    
def set_mole(flag,pins):
    # This function is to set the mole based on the generated list
    for m in range(len(flag)):
        pins[m].write_digital(flag[m])
    

while True:
    # Const definition
    n = 2 # Maximum lights; TODO: 3 
    pins = [pin0, pin1, pin2] # Light control; TODO: 5 LEDs
    flag=[0, 0, 0] # Mole indicator; TODO: 5 moles
    
    # TODO：another loop for score recording, start button and game time.
    
    # Initialization
    prepared = False
    count,flag = generate_mole(n,flag)
    display.show(count, wait=False)
    set_mole(flag,pins)
    
    # Game start
    prepared = True
    ind = -1
    r = 0
    while prepared:
        if button_a.is_pressed():
            ind = 0
        elif button_b.is_pressed():
            ind = 1
        if ind != -1 and flag[ind] == 1:
            # Success
            display.show(Image.YES, wait=False)
            pins[ind].write_digital(0)
            prepared = False
        else:
            # If not success in 1 sec, restart automatically
            r = r+1
            if r>10:
                prepared = False
        sleep(50)
    # TODO: Display the score