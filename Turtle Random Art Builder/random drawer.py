import time
import random
import turtle
import tkinter as tk
from PIL import ImageGrab
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
t = turtle.RawTurtle(canvas)




Bcolor = input('Enter y for a black backgroud: ')
infidraw = input('Enter y for infinite draw: ')
error_block = 1
#Try strokes
while error_block == 1:
    try:
        strokes = int(input('Enter amount of strokes before ending: '))
    except ValueError as error:
        print('ERROR please enter a valid interger')
    else:
        error_block = 0
        

    
save = input('Enter y to save art as .png file: ')
saveName = input('Enter name of save or enter "spam" for auto incremented saves: ')
num = 0


def dump_gui():
    global num
    print('Saving...')

    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + root.winfo_width()
    y1 = y0 + root.winfo_height()
    if saveName == 'spam':
        num += 1
        #print('number is',num)
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(f"Turtle_Art {num}.png")
    else:
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(f"{saveName}.png")

    
def main():
    colors = ['yellow','blue','green','red','blue','black','purple','white']
    if Bcolor == 'y':
        colors.remove('black')
    else:
        colors.remove('white')
    
    
    
    movex = range(-200, 200)
    movey = range(-200, 200)
    rotation = range(20, 100)
    direction = (1,1,2,3)
    start = input('press enter to start: ')
    x = 1
    y = 0
    #print(colors)
    #ssd = turtle.getscreen()
    #t = turtle.Turtle()


    #infidraw

    if infidraw == 'y':
        while True:
            if Bcolor == 'y':
                t.penup()
                t.goto(-200,-200)
                t.pendown()
                t.fillcolor("black")
                t.begin_fill()
                t.goto(200,-200)
                t.goto(200,200)
                t.goto(-200,200)
                t.end_fill()
                t.penup()
                t.goto(0,0)
                t.pendown()
            for j in range(strokes):
                print(y)
                y += 1
                t.pencolor(random.choice(colors))
                t.goto(random.choice(movex),(random.choice(movey)))
            time.sleep(2)
            print('Resetting board...')
            if save == 'y':
                t.hideturtle()
                #num += 1
                dump_gui()
                t.showturtle()
            time.sleep(1)
            y = 0
    else:
        if Bcolor == 'y':
            t.goto(-200,-200)
            t.fillcolor("black")
            t.begin_fill()
            t.goto(200,-200)
            t.goto(200,200)
            t.goto(-200,200)
            t.end_fill()
            t.penup()
            t.goto(0,0)
            t.pendown()
        for j in range(strokes):
            print(y)
            y += 1
            t.pencolor(random.choice(colors))
            t.goto(random.choice(movex),(random.choice(movey)))
        print('Done!')
        if save == 'y':
            t.hideturtle()
            #num += 1
            dump_gui()
            t.showturtle()
        done = input('Enter to exit: ')
    
main()
