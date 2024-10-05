import time
import random
from random import randint
import turtle
import tkinter as tk
from PIL import ImageGrab
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()
t = turtle.RawTurtle(canvas)



while(True):
    new = input('Enter for random color: ')

    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)
    print(f'R:{c1}\nG:{c2}\nB{c3}')
    t.colormode(255)
    t.color((c1,c2,c3))
    t.penup()
    t.goto(-10,0)
    t.pendown()
    t.goto(-10,-100)
    t.penup()
    t.goto(-10,0)
    #goto(randint(-100,100),randint(-100,100))
    
    hue = input('Enter for darker hues of that color: ')
    go = -20
    for x in range(5):
        if c1 >= 20:
            c1 -= 20
        if c2 >= 20:
            c2 -= 20
        if c3 >= 20:
            c3 -= 20
        print(f'R:{c1}\nG:{c2}\nB{c3}')
        t.pencolor(c1,c2,c3)
        t.penup()
        t.goto(go,0)
        t.fillcolor(c1,c2,c3)
        t.pendown()
        #c1 = 255
        #pencolor(0,255,0)
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        t.penup()
        t.goto(-10,0)
        t.pendown()
        go -= 20
