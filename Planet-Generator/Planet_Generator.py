#Planet Generator created by Zachary Post 9/13/2022

#Remember to send the newest version on Discord after editing!

import random
from turtle import *
from random import randint
import time
import turtle as t
s = t.Screen()
#s.setup(300, 300)
s.bgpic('space2.png')
t.colormode(255)
speed(0)
def habitable():


    #ALL COLOR IS RELETAVE TO SEA COLOR
    #Atmosphere is +50
    #Land is -50

    #Random sea color
    difference = 45

    exotics = [1, 1, 1, 2, 2, 2, 2]
    exotic = random.choice(exotics)
    #difference = int(input('Enter RGB difference (no less than 10 to avoid errors!): '))
    #exotic = input('Enter y for exotic world color: ')
    if exotic == 2:
        sea1 = randint(difference,205)
        sea2 = randint(difference,205)
        sea3 = randint(difference,205)

        atmo1d = sea1 + difference
        atmo2d = sea2 + difference
        atmo3d = sea3 + difference


        atmo1a = atmo1d - 45
        atmo2a = atmo2d - 45
        atmo3a = atmo3d - 45

        atmo1b = atmo1d - 30
        atmo2b = atmo2d - 30
        atmo3b = atmo3d - 30

        atmo1c = atmo1d - 15
        atmo2c = atmo2d - 15
        atmo3c = atmo3d - 15
        atmo3c = atmo3d - 3

        #Random land color
        land1 = randint(10,250)
        land2 = randint(10,250)
        land3 = randint(10,250)

        crater1 = 65
        crater2 = 65
        crater3 = 65

        ring1 = sea1
        ring2 = sea2 + 20
        ring3 = sea3

        river1 = sea1 - 15
        river2 = sea2 - 15
        river3 = sea3 - 15

    else:
        custom = 'a'
        if custom == 'c':
            sea1 = int(input('Enter value for sea1: '))
            sea2 = int(input('Enter value for sea2: '))
            sea3 = int(input('Enter value for sea3: '))
        else:
            sea1 = randint(difference,205)
            sea2 = randint(difference,205)
            sea3 = randint(difference,205)

        #sea atmosphere color

        atmo1d = sea1 + difference
        atmo2d = sea2 + difference
        atmo3d = sea3 + difference


        atmo1a = atmo1d - 45
        atmo2a = atmo2d - 45
        atmo3a = atmo3d - 45

        atmo1b = atmo1d - 30
        atmo2b = atmo2d - 30
        atmo3b = atmo3d - 30

        atmo1c = atmo1d - 15
        atmo2c = atmo2d - 15
        atmo3c = atmo3d - 15

        #Random land color
        land1 = sea1 - difference
        land2 = sea2 - difference
        land3 = sea3 - difference

        #Crater

        crater1 = 65
        crater2 = 65
        crater3 = 65

        #Ring

        ring1 = land1
        ring2 = land2 + 15
        ring3 = land3

        river1 = sea1 - 15
        river2 = sea2 - 15
        river3 = sea3 - 15

    #MOON COLOR 1
    moonDifference = 60
    
    moonColor1 = randint(moonDifference,205)
    moonColor2 = randint(moonDifference,205)
    moonColor3 = randint(moonDifference,205)

    dirt1 = moonColor1 - moonDifference
    dirt2 = moonColor2 - moonDifference
    dirt3 = moonColor3 - moonDifference



    #MOON COLOR 2


    moonColor12 = randint(moonDifference,205)
    moonColor22 = randint(moonDifference,205)
    moonColor32 = randint(moonDifference,205)

    dirt12 = moonColor12 - moonDifference
    dirt22 = moonColor22 - moonDifference
    dirt32 = moonColor32 - moonDifference
    #print(moon1,moon2,moon3)

    canvas_definer = 'a'
    if canvas_definer == 'y':
    #Canvas Definer
    #time.sleep(2)
        t.penup()
        t.goto(300,300)
        t.pendown()
        t.fillcolor(0,0,0)
        #t.fillcolor(atmo1,atmo2,atmo3)
        t.begin_fill()
        t.goto(300,-300)
        t.goto(-300,-300)
        t.goto(-300,300)
        t.goto(300,300)
        t.end_fill()

    #TURLTE POINTS
    TX = 0
    TY = 0

    
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.left(90)


    #Add planet code here
    #t.goto(-80.0,-210.0)
    #t.color(100,100,0)
    exec(open('habitable/habitable_planet_template.py').read())
    topL = ['topL1','topL2','topL3','topL4']
    topR = ['topR1','topR2','topR3','topR4']
    bottomL = ['bottomL1','bottomL2','bottomL3','bottomL4']
    bottomR = ['bottomR1','bottomR2','bottomR','bottomR3']
    craters = ['craterOPT1','craterOPT2']
    moons = ['moon1a','moon2a','moon1b','moon2b','moon2c']
    moons1 = ['moon1a','moon2a']
    moons2 = ['moon1b','moon2b','moon2c']
    rivers = ['river1','river2']
    #moon3 = ['moon3']

    #Random generator

    #crater123 = range(1,10)
    crater123 = [1,1,1,2]
    crater = random.choice(crater123)
    #crater = 2
    ringchoice = [0,0,1]
    ring = random.choice(ringchoice)
    moonchoice = [0,1,1,1,2,2,2,3,3,4]
    moon = random.choice(moonchoice)
    riverchoice = [0,0,0,1,1]
    river = random.choice(riverchoice)
    #river = 1
    #moon = 3
    exec(open(f'habitable/{random.choice(topL)}.py').read())

    #bottom right
    exec(open(f'habitable/{random.choice(bottomR)}.py').read())

    #top right
    exec(open(f'habitable/{random.choice(topR)}.py').read())

    #bottom left
    exec(open(f'habitable/{random.choice(bottomL)}.py').read())

    #Crater
    if crater == 2:
        exec(open(f'habitable/{random.choice(craters)}.py').read())

    if river == 1:
        exec(open(f'habitable/{random.choice(rivers)}.py').read())



    #Moon

    if moon == 1:
        exec(open(f'moon/{random.choice(moons)}.py').read())
    elif moon == 2:
        exec(open(f'moon/{random.choice(moons1)}.py').read())
        exec(open(f'moon/{random.choice(moons2)}.py').read())
    elif moon == 3:
        exec(open(f'moon/{random.choice(moons1)}.py').read())
        exec(open(f'moon/{random.choice(moons2)}.py').read())
        exec(open(f'moon/{random.choice(moons)}.py').read())
    elif moon == 4:
        exec(open(f'moon/{random.choice(moons)}.py').read())
        exec(open(f'moon/moon3.py').read())
    #elif moon == 2:
        #exec(open(f'moon/{random.choice(moons2)}.py').read())
    #elif moon == 3:
        #exec(open(f'moon/{random.choice(moons3)}.py').read())

    #from planetfiles import pl
    #pl()
    
    #exec(open('habitable/topL1.py').read())
    #exec(open('habitable/topR2.py').read())
    #exec(open('habitable/bottomR1.py').read())

    if ring == 1:
        exec(open(f'habitable/ring.py').read())

    
    exec(open('habitable/naming_module.py').read())
    stop = input("Enter to exit: ")


    

habitable()
