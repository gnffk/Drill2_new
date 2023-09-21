from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
cx,cy, r = 400,300, 200
def run_circle():
    print("CIRCLE")

    # 그림그리기

    
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.05)

def run_rectangle():
    print("rectangle")

    for x in range(50,750+1,10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.05)        
        
    

while True:
    #run_circle()
    run_rectangle()
    break
    
close_canvas()
