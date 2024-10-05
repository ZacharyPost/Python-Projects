import pyautogui as p
import time
import random


y = 0
start = input("Enter to start: ")

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    time.sleep(0.01)
    x = p.position()
    if y != x:
        x1 = x.x // 7
        x2 = x.y // 6
        a = random.choice(alphabet)
        b = random.choice(alphabet.lower())
        y = x
    print(x1 * a, x2 * b)
