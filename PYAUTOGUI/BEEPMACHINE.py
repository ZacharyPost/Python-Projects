import pyautogui as p
import time
import winsound

y = 0
start = input("Enter to start: ")

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    time.sleep(0.01)
    x = p.position()
    winsound.SND_NOSTOP
    if y != x:
        x1 = x.x + 550
        x2 = x.y + 100
        y = x
    winsound.Beep(x1, x2)
    print(f"Frequency: {x1}")

