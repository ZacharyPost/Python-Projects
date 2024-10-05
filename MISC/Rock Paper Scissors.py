import random
import time
def main():
    intro()
    one = 0
    two = 0
    choices = [1, 2, 3]
    print('Let us begin!')
    print()
    print('First to 5 points wins?')
    print('1. Yes\n2. No')
    answerz = input('Enter: ')
    x = 1
    print()
    while x == 1:
        if answerz == '1':
            if one == 5:
                print()
                print()
                print('=' * 30)
                print('=' * 40)
                print('=' * 50)
                print('=' * 60)
                print()
                print(f'You are the winner!!\nI had {two} and you had {one}')
                print()
                print('=' * 60)
                print('=' * 50)
                print('=' * 40)
                print('=' * 30)
                print()
                print()
                x = 0
            elif two == 5:
                print()
                print()
                print('=' * 30)
                print(f'I am the winner!!\nI had {two} and you had {one}')
                print('=' * 30)
                print()
                print()
                x = 0
            else:
                print()
                print('I am deciding...')
                time.sleep(0.5)
                choice = random.choice(choices)
                print()
                print('I have decided!')
                #print(choice)
                print()
                print('1. Rock\n2. Paper\n3. Scissors\n4. Exit')
                print()
                oppose = input('Enter your choice: ')

                if oppose == 'peak':
                    if choice == 1:
                        choice2 = 'Rock'
                    elif choice == 2:
                        choice2 = 'Paper'
                    elif choice == 3:
                        choice2 = 'Scissors'
                    print()
                    print(f"I chose {choice2}")
                    print() 
                    oppose = input('Enter your NEW choice: ')
                    print()

                #ROCK
                if oppose == '1':
                    if choice == 1:
                        print()
                        print('=' * 30)
                        print()
                        print("That's what I picked...")
                        print() 
                        print('=' * 30)
                        print()
                    elif choice == 2:
                        print()
                        print('=' * 30)
                        print()
                        print("I chose Paper")
                        print()
                        print('=' * 30)
                        two += 1
                        print(f"I now have {two} point(s)")
                        print()
                        
                        
                    elif choice == 3:
                        print()
                        print('=' * 30)
                        print()
                        print("I chose Scissors")
                        print()
                        print('=' * 30)
                        one += 1
                        print(f"You now have {one} point(s)")
                        print()

                #PAPER

                if oppose == '2':
                    if choice == 1:
                        print()
                        print('=' * 30)
                        print()
                        print("I chose Rock")
                        print() 
                        print('=' * 30)
                        one += 1
                        print(f"You now have {one} point(s)")
                        print()
                        print()
                    elif choice == 2:
                        print()
                        print('=' * 30)
                        print()
                        print("That's what I picked...")
                        print() 
                        print('=' * 30)
                        print()
                        
                        
                    elif choice == 3:
                        print()
                        print('=' * 30)
                        print()
                        print("I chose Scissors")
                        print()
                        print('=' * 30)
                        two += 1
                        print(f"I now have {two} point(s)")
                        print()

                #SCISSORS

                if oppose == '3':
                    if choice == 1:
                        print()
                        print('=' * 30)
                        print()
                        print("I chose Rock")
                        print() 
                        print('=' * 30)
                        two += 1
                        print(f"I now have {two} point(s)")
                        print()
                        print()
                    elif choice == 2:
                        print()
                        print('=' * 30)
                        print()
                        print("I chose Paper")
                        print()
                        print('=' * 30)
                        one += 1
                        print(f"You now have {one} point(s)")
                        
                        
                    elif choice == 3:
                        print()
                        print('=' * 30)
                        print()
                        print("That's what I picked...")
                        print() 
                        print('=' * 30)
                        print()


                #GUN

                if oppose == 'gun':
                    time.sleep(0.2)
                    print('=' * 30)
                    print()
                    print("Well, I can't beat that")
                    print()
                    print('=' * 30)
                    one += 1
                    print(f"You now have {one} point(s)")

                    

                #EXIT

                elif oppose == '4':
                    print()
                    print()
                    print('Exitting....')
                    time.sleep(1.3)
                    x = 0
                
def intro():
    pass

main()
