import time
import board
import digitalio

button1out = digitalio.DigitalInOut(board.GP16)
button1out.direction = digitalio.Direction.OUTPUT
button1out.value = True

green = digitalio.DigitalInOut(board.GP15)
green.direction = digitalio.Direction.OUTPUT

blue = digitalio.DigitalInOut(board.GP14)
blue.direction = digitalio.Direction.OUTPUT

red = digitalio.DigitalInOut(board.GP12)
red.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)
state=1
while True:
    if button.value:
        print("You pressed the button!")
        state=state+1
        if state == 4:
            state = 1
        if state==1 :
            blue.value = False
            red.value = False
            green.value = False
        
        elif state==2 :
            blue.value = True
            red.value = True
            green.value = False
           
        elif state==3 :
            blue.value = True
            red.value = True
            green.value = True
        print(state)
        time.sleep(0.5) # wait 0.5 seconds
        '''
        green.value = True # Turn on the LED
        blue.value = False # Turn on the LED
        time.sleep(5) # wait 0.5 seconds
        green.value = False # Turn off the LED
        blue.value = True # Turn on the LED
        '''
        if blue.value:
            print('blue')
        
