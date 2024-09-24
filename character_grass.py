from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')
    
    r, cx, cy = 300, 800//2, 600//2
    for d in range(0,360):
        x = r * cos(radians(d)) + cx
        y = r * sin(radians(d)) + cy

        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.01)
    
    pass

while(True):
    run_rectangle()
    run_circle()
    break
    

close_canvas()
