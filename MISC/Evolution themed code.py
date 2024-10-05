import random
import time
def main():
    start = input('Enter: ')
    g = 1
    j = 1
    x = 0.5
    y = 0.5
    while j == 1:
        time.sleep(0.1)
        if random.random() < x:
            x += 0.01
            y -= 0.01
            print('x')
        else:
            y += 0.01
            x -= 0.01
            print('y')
        if x >= 1:
            j = 0
        elif y >=1:
            j = 0
    print()
    print()
    time.sleep(1)
    print(f'x is {round(x, 5)} y is {round(y, 5)}')
    print()
    print('=' * 100)
    if x > y:
        print('x has won this war')
    elif y > x:
        print('y has won this war')
    ends = input('Enter: ')

if __name__ == '__main__':
    main()
            
