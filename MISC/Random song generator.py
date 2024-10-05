import time
import random
def main():
    print('Welcome to the musical program!')
    print('Please select your option')
    print('1. Random tune\n2. Key lookup')
    answer1 = input('Enter: ')
    if answer1 == '1':
        Auto()
    elif answer1 == '2':
        Manual()

def Auto():



    
    #Measure

    
    bx1 = [4, 4, 6]
    bx = random.choice(bx1)




    
    #KEYS LIST

    
    Keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    #Keys = ['A','B','C','D','E','F','G']

    A = ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#']
    AS = ['A#', 'Cm', 'Dm', 'D#', 'F', 'Gm', 'A']
    B = ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#']
    C = ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B']
    CS = ['C#', 'D#m', 'Fm', 'F#', 'G#', 'A#m', 'C']
    D = ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#']
    DS = ['D#', 'Fm', 'Gm', 'G#', 'A#', 'Cm', 'D']
    E = ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#']
    F = ['F', 'Gm', 'Am', 'A#', 'C', 'Dm', 'E']
    FS = ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'F']
    G = ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#']
    GS = ['G#', 'A#m', 'Cm', 'C#', 'D#', 'Fm', 'G']
    #ch = 'A#'
    ch = random.choice(Keys)
    #print(Keys)
    print()
    print()
    print()
    time.sleep(1)

    ab = 0.151
    spe = ['2', '4', '7']



    #CHORDS

    print('The chords are')
    print()
    print('=' * 50)
    print()

    if ch == 'A':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(A), random.choice(spe))
            else:
                print(random.choice(A))
            print()
    elif ch == 'A#':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(AS), random.choice(spe))
            else:
                print(random.choice(AS))
            print()
    elif ch == 'B':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(B), random.choice(spe))
            else:
                print(random.choice(B))
            print()
    elif ch == 'C':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(C), random.choice(spe))
            else:
                print(random.choice(C))
            print()
    elif ch == 'C#':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(CS), random.choice(spe))
            else:
                print(random.choice(CS))
            print()
    elif ch == 'D':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(D), random.choice(spe))
            else:
                print(random.choice(D))
            print()
    elif ch == 'D#':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(DS), random.choice(spe))
            else:
                print(random.choice(DS))
            print()
    elif ch == 'E':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(E), random.choice(spe))
            else:
                print(random.choice(E))
            print()
    elif ch == 'F':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(F), random.choice(spe))
            else:
                print(random.choice(F))
            print()
    elif ch == 'F#':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(FS), random.choice(spe))
            else:
                print(random.choice(FS))
            print()
    elif ch == 'G':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(G), random.choice(spe))
            else:
                print(random.choice(G))
            print()
    elif ch == 'G#':
        for x in range(bx):
            if random.random() < ab:
                print(random.choice(GS), random.choice(spe))
            else:
                print(random.choice(GS))
            print()
    print('=' * 50)
    print()
    print()








    #BPM


    
    bp = range(45,110)
    bpm = random.choice(bp)














    #STRUMMING PATTERN GENERATOR


    if bpm < 65:
        PatternsList = {'1':'1','2':'4th','3':'4th','4':'4th','5':'8th'}
    else:
        PatternsList = {'1':'4th','2':'8th','3':'16th','4':'4th','5':'4th','6':'8th'}
    pattern1 = random.choice(list(PatternsList.values()))
    pattern2 = random.choice(list(PatternsList.values()))
    pattern3 = random.choice(list(PatternsList.values()))
    pattern4 = random.choice(list(PatternsList.values()))
    if bx == 6:
        pattern5 = random.choice(list(PatternsList.values()))
        pattern6 = random.choice(list(PatternsList.values()))


    

    print()
    print('=' * 50)
    print()
    print(f'The key is in {ch} the BPM is {bpm} the measure is {bx}')
    print()
    if bx == 6:
        print(f'The strumming pattern is {pattern1}, {pattern2}, {pattern3}, {pattern4}, {pattern5}, {pattern6}')
    else:
        print(f'The strumming pattern is {pattern1}, {pattern2}, {pattern3}, {pattern4}')
    print()
    print('=' * 50)
 
def Manual():
    A = ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#']
    B = ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#']
    C = ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B']
    D = ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#']
    E = ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#']
    F = ['F', 'Gm', 'Am', 'A#', 'C', 'Dm', 'E']
    G = ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#']
    answer = input('Enter key: ')
    if answer == 'A':
        print(A)
    elif answer == 'B':
        print(B)
    elif answer == 'C':
        print(C)
    elif answer == 'D':
        print(D)
    elif answer == 'E':
        print(E)
    elif answer == 'F':
        print(F)
    elif answer == 'G':
        print(G)


main()
