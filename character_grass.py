from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)   

def run_top():
    print('TOP')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass

def run_right():
    print('RIGHT')
    for y in range(550,0,-10):
        draw_boy(800,y)
    pass

def run_bottom():
    print('BOTTOM')
    for x in range(800,0,-10):
        draw_boy(x,0)
    pass

def run_left():
    print('LEFT')
    for y in range(0,550,10):
        draw_boy(0,y)
    pass

def run_rectangle():
    print('RECTANGLE')

    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_circle():
    print('CIRCLE')
    
    r, cx, cy = 300, 800//2, 600//2
    for d in range(0,360):
        x = r * cos(radians(d)) + cx
        y = r * sin(radians(d)) + cy

        draw_boy(x,y)
    pass

def run_tri_right():
    print('TRI_RIGHT')
    y = 600
    for x in range(400,800,10):
        y -= 15
        draw_boy(x,y)
    pass
def run_tri_left():
    print('TRI_LEFT')
    y = 0
    for x in range(0,400,10):
        y += 15
        draw_boy(x,y)
    pass

def run_triangle():
    print('TRIANGLE')
    run_tri_left()
    run_tri_right()
    run_bottom()
    pass

while(True):
    #run_rectangle()
    #run_circle()
    run_triangle()
    break
    

close_canvas()
