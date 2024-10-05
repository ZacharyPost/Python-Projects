#Planet Generator created by Zachary Post 9/13/2022

#Remember to send the newest version on Discord after editing!
from turtle import *

def main():




    #Planet Type Choices
    planet_types = ['habitable','gas','moon']

    

    debug = input('Debug? y = yes: ')








    
    if debug == 'y':
        

        import random
        from random import randint
        import time
        import turtle as t
        t.colormode(255)
    
        #Canvas Definer
        #time.sleep(2)
        t.penup()
        t.goto(300,300)
        t.pendown()
        t.fillcolor("white")
        t.begin_fill()
        t.goto(300,-300)
        t.goto(-300,-300)
        t.goto(-300,300)
        t.goto(300,300)
        t.end_fill()

        #TURLTE POINTS
        TX = 0
        TY = 0

        t.pencolor("green")
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.left(90)


        #t.colormode(255)
        #COLORS
        colors = ['green','red','blue','yellow','gray','black','white','purple','teal']

        #Habitable planet template
        defPH = input("Enter y for default habitable planet: ")
        if defPH == 'y':
            exec(open('habitable/habitable_planet_template_DEBUG.py').read())
        t.goto(0,0)
        movement_power = float(input("Enter movement power: "))
        #print('Standard time is 0.1 seconds')
        timez = 0
        move = input("Enter movement! Q to exit, help for help: ")
        comment = 'hi'
        pencolorz = 'hi'
        fillcolorz = 'hi'
        circle_size = 0
        #timez = 0
        planetFiles = open("planetfiles.py","w")
        planetFiles.write('t.goto(0,0)')
        planetFiles.write('\n')
        planetFiles.write(f'###START OF NEW CODE###')
        planetFiles.write('\n')
        planetFiles.close()
        #planetPrint = open("planetprint.txt","a")
        while(move != 'q'):
            if move == 'w':
                t.forward(movement_power)
                TY += movement_power
                print(f'Turtle Y:{TY}')
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'd':
                t.right(90)
                t.forward(movement_power)
                t.left(90)
                TX += movement_power
                print(f'Turtle X:{TX}')
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'a':
                t.left(90)
                t.forward(movement_power)
                t.right(90)
                TX -= movement_power
                print(f'Turtle X:{TX}')
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 's':
                t.left(180)
                t.forward(movement_power)
                t.right(180)
                TY -= movement_power
                print(f'Turtle Y:{TY}')
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'b':
                print('-')
                print(f'Turtle X:{TX}')
                print(f'Turtle Y:{TY}')
                print('-')
            elif move == 'c':
                try:
                    circle_size = int(input('Enter circle size: '))
                except ValueError as error:
                    print('ERROR please enter a number')
                finally:
                    t.circle(circle_size)
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'f':
                try:
                    movement_power = float(input("Enter movement power: "))
                except ValueError as error:
                    print('ERROR please enter a number')
            elif move == 'h':
                print('Pen Lifted')
                t.penup()
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'j':
                print('Pen Dropped')
                t.pendown()
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'n':
                comment = input('Enter comment: ')
                print('Comment added')
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'y':
                #turtle.TurtleGraphicsError
                the_chosen_color = input('Enter color: ')
                if the_chosen_color in colors:
                    pencolorz = the_chosen_color
                else:
                    print('ERROR color not known! Would you like to proceed?')
                    yes = input('Enter: ')
                    if yes == 'y' or yes == 'Y':
                        pencolorz = the_chosen_color
                t.pencolor(pencolorz)
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'u':
                the_chosen_color = input('Enter color: ')
                if the_chosen_color in colors:
                    fillcolorz = the_chosen_color
                else:
                    print('ERROR color not known! Would you like to proceed?')
                    yes = input('Enter: ')
                    if yes == 'y' or yes == 'Y':
                        fillcolorz = the_chosen_color
                #fillcolorz = input('Enter color: ')
                t.fillcolor(fillcolorz)
                t.begin_fill()
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'i':
                t.end_fill()
                logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)
            elif move == 'help':
                print('WASD - move\nB - display location\nC - draw circle\nF - chance speed\nH - lift pen\nJ - drop pen\nN - comment\nY - change color\nU - begin fill\nI - end fill')
            move = input("Enter movement Q to exit: ")

        logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size)





    else:

        #planet_choice = random.choice(planet_types)
        planet_choice = 'habitable'

        #Planet Definer

        #Habitable
        if planet_choice == 'habitable':
            import Planet_Tester









def logger(planetFiles,TX,TY,move,comment,pencolorz,fillcolorz,timez,circle_size):

    #Code file builder

    
    planetFiles = open("planetfiles.py","a")
    #planetPrint = open("planetprint.txt","a")
    planetFiles.write(f'time.sleep({timez})')
    planetFiles.write('\n')
    if move == 'h':
        planetFiles.write(f't.penup()')
        planetFiles.write('\n')
        planetFiles.write(f'print("lifting pen")')
        planetFiles.write('\n')
    elif move == 'j':
        planetFiles.write(f't.pendown()')
        planetFiles.write('\n')
        planetFiles.write(f'print("dropping pen")')
        planetFiles.write('\n')
    elif move == 'n':
        planetFiles.write(f'###{comment}###')
        planetFiles.write('\n')
    elif move == 'y':
        planetFiles.write(f't.pencolor(land1,land2,land3)')
        planetFiles.write('\n')
        planetFiles.write(f'print("Changing pen color to land")')
        planetFiles.write('\n')
    elif move == 'u':
        planetFiles.write(f't.fillcolor(land1,land2,land3)')
        planetFiles.write('\n')
        planetFiles.write(f'print("changing fill color to land")')
        planetFiles.write('\n')
        planetFiles.write(f't.begin_fill()')
        planetFiles.write('\n')
        planetFiles.write(f'print("begining fill")')
        planetFiles.write('\n')
    elif move == 'i':
        planetFiles.write(f't.end_fill()')
        planetFiles.write('\n')
        planetFiles.write(f'print("filling")')
        planetFiles.write('\n')
    elif move == 'c':
        planetFiles.write(f't.circle({circle_size})')
        planetFiles.write('\n')
        planetFiles.write(f'print("drawing circle")')
        planetFiles.write('\n')
    elif move == 'q':
        planetFiles.write(f't.penup()')
        planetFiles.write('\n')
        planetFiles.write(f'print("lifting pen")')
        planetFiles.write('\n')
        planetFiles.write(f't.goto(0,0)')
        planetFiles.write('\n')
        planetFiles.write(f't.pendown()')
        planetFiles.write('\n')
        planetFiles.write(f'print("dropping pen")')
        planetFiles.write('\n')
        planetFiles.write(f'print("DONE")')
    else:
        planetFiles.write(f't.goto({TX},{TY})')
        planetFiles.write('\n')
        planetFiles.write(f'print("moving to x:{TX} y:{TY}")')
        planetFiles.write('\n')
    planetFiles.close()
    #planetPrint.close()
    

#PLANET BUILDER
#t.penup()
#TX = -100
#TY = -100
#t.goto(TX,TY)
#GROUND PLANET ALPHA
#ocean = "blue"
#earth = "green"


if __name__ == '__main__':
    main()

