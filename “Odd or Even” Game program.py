# Add your Python code here. E.g.
from microbit import *

import random
# game description
display.scroll('Press "a" button if the given number is odd, and press "b" button if the given number is even. Ready? go!') 
sleep(500)
# initialization
game = True

# main loop
while game:
    number = random.randint(1,9)
    display.show(number)
    # wait for the answer and judge
    while True:
        if button_a.is_pressed() and (number % 2) == 0:
            display.show(Image.NO)
            break
        elif button_b.is_pressed() and (number % 2) == 0:
            display.show(Image.YES)
            break
        elif button_a.is_pressed() and (number % 2) == 1:
            display.show(Image.YES)
            break
        elif button_b.is_pressed() and (number % 2) == 1:
            display.show(Image.NO)
            break
    sleep(1500)
    # wether to continue
    display.scroll('Press "a" to continue, "b" to quit.', wait = False, loop = True, delay = 100)
    # wait for the answer and judge
    while True:
        if button_a.is_pressed():
            sleep(1000)
            break
        elif button_b.is_pressed():
            game = False
            break
# game ends
display.scroll('See ya!')
    
