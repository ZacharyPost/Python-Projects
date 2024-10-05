import time
import random
import turtle
def main():
    play = 1
    intro()
    while play == 1:
        turtle.clear()
        turtle.reset()
        print('Planting bombs........')
        #time.sleep(2)
        

        ss = turtle.getscreen()
        t = turtle.Turtle()


        #Background

        turtle.goto(-200,-200)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.goto(200,-200)
        turtle.goto(200,200)
        turtle.goto(-200,200)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        
        turtle.color('white')
        
        #BOMB


        x = range(-200,200, 20)
        y = range(20, 180, 20)

        bomb1 = random.choice(x),random.choice(y)
        bomb2 = random.choice(x),random.choice(y)
        bomb3 = random.choice(x),random.choice(y)
        bomb4 = random.choice(x),random.choice(y)
        bomb5 = random.choice(x),random.choice(y)
        bomb6 = random.choice(x),random.choice(y)
        bomb7 = random.choice(x),random.choice(y)
        bomb8 = random.choice(x),random.choice(y)
        bomb9 = random.choice(x),random.choice(y)
        bomb10 = random.choice(x),random.choice(y)




        #Winning gate


        gate = random.choice(x),200
        #gate = 60,200
        turtle.penup()
        turtle.goto(gate)
        turtle.color('blue')
        turtle.left(90)
        turtle.backward(5)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(0,0)
        turtle.right(90)
        turtle.color('white')
        turtle.pendown()

        #print(bomb8)

        #Player Stuff
        
        life = 1
        x = 0
        y = 0
        player = x,y


        #While Loop
        turtle.left(90)
        while life == 1:
            

            #Player Movement

            movement = input('Enter: ')
            print()
            if movement == 'w':
                if y >= 200:
                    print('You are at a wall')
                else:
                    print('You move foward.')
                    turtle.forward(20)
                    y += 20
            elif movement == 'd':
                if x >= 200:
                    print('You are at a wall')
                else:
                    print('You move right.')
                    turtle.right(90)
                    turtle.forward(20)
                    turtle.left(90)
                    x += 20
            elif movement == 'a':
                if x <= -200:
                    print('You are at a wall')
                else:
                    print('You move left.')
                    turtle.left(90)
                    turtle.forward(20)
                    turtle.right(90)
                    x -= 20
            elif movement == 's':
                print('You move back.')
                turtle.left(180)
                turtle.forward(20)
                turtle.right(180)
                y -= 20
            elif movement == 'blacksheep':
                #print(f'Bomb2 is at {bomb2}')
                turtle.color('green')
                turtle.penup()
                turtle.goto(bomb1)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb2)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb3)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb4)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb5)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb6)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb7)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb8)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb9)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(0.03)

                turtle.penup()
                turtle.goto(bomb10)
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(2)
                turtle.end_fill()
                time.sleep(1)
                turtle.penup()
                turtle.goto(player)
                turtle.pendown()
                turtle.color('white')


            elif movement == 'rat':
                print('Ok, plotting safest route to gate...')
                time.sleep(1.5)
                turtle.penup()
                turtle.color('purple')
                turtle.goto(0,0)
                turtle.pendown()
                x = 0
                y = 0
                ghate = 1
                player = x,y
                #print(gate[0])
                #print(bomb1[0])
                #print(f'This is x {x}')
                while player != gate:
                    while ghate == 1:
                        while x != gate[0]:
                            if gate[0] < 1:               

                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                x -= 20
                                player = x,y
                                      
                            elif gate[0] > 1:
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                x += 20
                                player = x,y

                            if player == bomb1:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb2:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb3:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb4:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb5:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb6:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb7:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb8:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb9:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb10:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20


                                
                        while y != gate[1]:
                            turtle.forward(20)
                            y += 20
                            player = x,y

                            if player == bomb1:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb2:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb3:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb4:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(5)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb5:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb6:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb7:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb8:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb9:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20

                            elif player == bomb10:
                                turtle.circle(5)
                                turtle.right(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.left(90)
                                turtle.forward(20)
                                turtle.right(90)
                                y += 20
                        ghate = 0


                turtle.penup()
                turtle.goto(0,0)
                turtle.pendown()
                turtle.color('white')
                x = 0
                y = 0
                player = x,y
                        
            elif movement == 'lazy':
                print('Ok...')
                time.sleep(1)
                time.sleep(0.5)
                turtle.goto(gate)
                x = gate[0]
                y = gate[1]

            elif movement == 'kamikaze':
                print('For the emperor!')
                time.sleep(1)
                turtle.goto(bomb1)
                x = bomb1[0]
                y = bomb1[1]

            elif movement == 'CleanUp':
                print('Ok, I am removing the bombs.')
                time.sleep(1)

                bomb1 = 300,300
                bomb2 = 300,300
                bomb3 = 300,300
                bomb4 = 300,300
                bomb5 = 300,300
                bomb6 = 300,300
                bomb7 = 300,300
                bomb8 = 300,300
                bomb9 = 300,300
                bomb10 = 300,300
                    
            else:
                print('Invalid input!')

            player = x,y
            #print(f'You are at {player}')




            #Explosion
            print()
            if player == bomb1:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            elif player == bomb2:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            elif player == bomb3:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            elif player == bomb4:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            elif player == bomb5:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            elif player == bomb6:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            #s
            elif player == bomb7:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            elif player == bomb8:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            elif player == bomb9:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            elif player == bomb10:
                print('Ya blew up!')
                turtle.fillcolor("red")
                turtle.begin_fill()
                turtle.circle(15)
                turtle.end_fill()
                life = 0
            else:
                print('Safe!')
            print()
            time.sleep(0.01)

            #Win

            if player == gate:
                print('YOU WON!!!')
                for xg in range(200):
                    print('=' * xg)
                    xg += 1
                turtle.penup()
                turtle.goto(130,0)
                turtle.fillcolor("yellow")
                turtle.pendown()
                turtle.begin_fill()
                turtle.circle(150)
                time.sleep(0.1)
                turtle.end_fill()
                life = 0
                print()

            if life == 0:
                print()
                print('Would you like to play again? y = yes')
                yesAgain = input('Enter: ')
                if yesAgain != 'y':
                    print('Exiting...')
                    time.sleep(1)
                    play = 0
    time.sleep(2)




def intro():
    print('Welcome to BombTravel! Would you like a copy of the rules?')
    rules = input('Enter y for yes, n for no: ')
    print()
    if rules == 'y':
        print("BombTravel is a game where the objective is to get to the blue dot (the gate)\nEnter W, A, S, or D to move your character (The white triangle).\nWatch out though, there're 10 randomly planted bombs\n in this field. Good luck!")
    else:
        print()
    print()
    print('Would you like a list of the cheat codes?')

    answer = input('Enter y for yes, n for no: ')
    if answer == 'y':
        print()
        print('blacksheep\nrat\nkamikaze\nlazy\nCleanUp')
        time.sleep(1)
    else:
        print()
    print()




main()
