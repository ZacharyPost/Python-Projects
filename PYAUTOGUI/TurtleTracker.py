import pyautogui as p
import time
import random
import turtle as t






y = 0
start = input("Enter to start: ")
t.Turtle()
t.forward(5)
x = p.position()
y = x

while True:
    time.sleep(0.01)
    x = p.position()
    #print(x)
        # p.moveTo(e)
        # p.click()
        # p.moveTo(1064, 780)
        # p.click()
        #print(x)
        #time.sleep(0.5)
        
        # Changing LED values randomly
    if y != x:
        if y.x > x.x:
            t.left(5)
        elif y.x < x.x:
            t.right(5)
        if y.y > x.y:
            t.forward(15)
        elif y.y < x.y:
            t.backward(5)
        y = x
        # x1 = x.x // 7
        # x2 = x.y // 6
        # a = t.forward(x1)
        # b = t.left(x2)
        # y = x
    #print(x1 * a, x2 * b)




#amount = int(input("Enter amount of times: "))

#amount = 10




