import random
import time
def main():
    Ptickets = 0
    tickets = []
    winning = []


    ticketBase = range(1, 1000)
    Goal = 0.3
    ticketValue = range(10, 100000)
    Goal2 = 0.6
    print('Welcome to the lottery machine!')
    balance = int(input('Input your starting balance: '))
    print()
    #print('Alright! It is $', format(balance, ",.2f"))
    print('Perfect! loading screen....')
    time.sleep(2)
    play = 1
    while play == 1:
        if Ptickets >= 1000:
            print('You win! You have 1,000 tickets!')
            print("Thanks for playing! Now you will be 'disposed' for being SUSpiciously good the lottery")
            time.sleep(5)
            break
        x = 0
        y = 0
        nope = 1
        print()
        print('1. Run lottery\n2. Purchase tickets\n3. Earn money\n4. Display money/owned tickets\n5. Exit')
        answer = input('Enter: ')




        if answer == 'loan':
            print('How much money would you like to borrow?')
            loan = int(input('Enter: '))
            balance += loan



        elif answer == '1':
            print()
            if Ptickets == 0:
                print('Please purchase lotto tickets')
            else:
                print('Starting lottery...')


                #LOTTERY

                times = 5
                while y < times:
                    y += 1
                    time.sleep(1)
                    print()
                    RandomTicket = random.choice(ticketBase)
                    print(RandomTicket)
                    if RandomTicket in tickets:
                        value = random.choice(ticketValue)
                        print('WINNER!!')
                        print(f'Your ticket is worth ${value}')
                        print()
                        time.sleep(0.3)
                        print('Would you like to take a 30-60 chance for double? y = Yes')
                        
                        TheAnswer = input('Enter: ')
                        if TheAnswer == 'y':
                            print('Alright!...')
                            time.sleep(1)
                            if random.random() > Goal:
                                print('WINNER!!!!!!!')
                                doubleValue = value * 2
                                print()
                                print(f'You earned ${doubleValue}')
                                print()
                                balance += doubleValue
                                time.sleep(1)
                            else:
                                print('Nope')
                                nope = 0
                                time.sleep(1)
                        else:
                            if nope == 1:
                                print(f'Ok :( You earned ${value}')
                                balance += value
                                time.sleep(1)
                                #balance += value
                            else:
                                print()

                print('=' * 100)
                print('LOTTERY END')
                print('=' * 100)
                Ptickets = 0
                tickets = []
                            


        
        elif answer == '2':
            print()
            print('How many tickets would you like to buy? Each ticket is $2')
            answerBuy = int(input('Enter: '))
            #print(balance)
            #print(answerBuy)
            answerBuy2 = answerBuy * 2
            #print(answerBuy2)
            if balance < answerBuy2:
                print('ERROR Insuffcient funds you need $',format(answerBuy2, ",.2f"))
            else:
                print('Perfect! adding tickets now...')
                time.sleep(1)
                balance -= answerBuy2
                #Ptickets += answerBuy

                #PLAYER'S RANDOM TICKET GENERATOR

                while x < answerBuy:
                    ticketGen = random.choice(ticketBase)
                    if ticketGen == 10000 or ticketGen == 0:
                        print(ticketGen)
                        ticketGen = random.choice(ticketBase)
                        asdasd = input('YES IT HAPPENED')
                    else:
                        tickets.append(ticketGen)
                        Ptickets += 1
                        x += 1
                        print(ticketGen)


        elif answer == '3':
            print("Welcome to the job! please enter the amount of hours (in seconds) you'd like to work")
            print('Each second is worth $10.00')
            job = int(input('Enter: '))
            print('Alright! Now, get to work!')

            
            time.sleep(job)

            
            print()
            earnings = job * 10
            print('You earned $', format(earnings,",.2f"))
            balance += earnings

        elif answer == '4':
            print()
            print('Would you like to check your balance or tickets?\n1. Balance\n2. Tickets')
            gggg = input('Enter: ')
            if gggg == '1':
                print('Your balance is $', format(balance, ",.2f"))
            elif gggg == '2':
                print(f'You have {Ptickets} tickets')




        elif answer == '5':
            print('Exiting....')
            play = 0





        else:
            print('Please enter a valid choice')
                
                

    


if __name__ == '__main__':
    main()
