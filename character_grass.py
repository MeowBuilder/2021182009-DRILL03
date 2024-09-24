from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')

    clear_canvas_now()
    boy.draw_now(400,300)
    delay(1)
    
    pass

while(True):
    run_rectangle()
    run_circle()
    break
    

close_canvas()
