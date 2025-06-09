import keyboard
import time
import random
import time

def main():
    start = input("Start: ")
    end = "0"
    while True:
        log_printer(end)
        end = input("Try again? ")
        if end == "y":
            print("ok!")
        elif end == "autobot":
            print()
        else:
            exit()

def log_printer(end):
    timez = 0.01
    x = "."
    point = "0"
    spacer = 120
    g = 0
    y = 1
    hidden = range(1000)
    hidden_choice = random.choice(hidden)
    #hidden_choice = 5
    g -= hidden_choice
    if end == "autobot":
        print("AUTO")
        while g != 0:
            time.sleep(timez)
            y += 1
            g += 1
            if y == hidden_choice:
                print(point * spacer)
                #g += 1
            else:
                print(x * spacer)
        if g == 0:
            print("YOU WIN!!!!")
        else:
            print(f"You were off by {g}")

            
    else:
        while not keyboard.is_pressed("ctrl"):
            time.sleep(timez)
            y += 1
            g += 1
            if y == hidden_choice:
                print(point * spacer)
                #g += 1
            else:
                print(x * spacer)
        if g == 0:
            print("YOU WIN!!!!")
        else:
            print(f"You were off by {g}")

            



main()
