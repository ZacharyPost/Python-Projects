import random
import time
def main():
    game = 1
    timezz = 1
    intro()
    auto1 = input('Would you like auto mode? y = yes: ')
    loadSave = input('Would you like to load from a save? Or start new *default is load y = new: ')
    start = input('Press enter to start: ')
    if loadSave == 'y':
        loadingSave = open('Box Game progress.data','r')
        LoadedSaveBal = loadingSave.readlines()
        loadingSave.close()
        balance = float(LoadedSaveBal[0])
        upgrade = int(LoadedSaveBal[1])
        price = int(LoadedSaveBal[2])
        boxes = int(LoadedSaveBal[3])
        upgradePrice = float(LoadedSaveBal[4])
        upgradePrice1 = float(LoadedSaveBal[5])
    else: 
        balance = 0
        boxes = 0
        upgrade = 500
        price = 1
        upgradePrice = 1200
        upgradePrice1 = 1200
    while game == 1:
        time.sleep(0.5)
        print()
        print('1. Produce boxes\n2. Display owned boxes\n3. Display Balance\n4. Sell boxes\n5. Upgrade\n6. Win\n7. Remove time\n8. Save and Exit')
        print()
        answer = input('Enter: ')
        print()
        

        #Produce
        
        
        if answer == '1':
            if auto1 == 'y':
                if timezz == 1:
                    time.sleep(1)
                print(f'You have produced {upgrade} boxes!')
                boxes += upgrade
            else:
                amount = int(input('Enter amount of boxes you would like to produce: '))
                if amount > upgrade:
                    print(f'Sorry, you cannot produce more than {upgrade} boxes')
                else:
                    if timezz == 1:
                        time.sleep(1)
                    print(f'You have produced {amount} boxes!')
                    boxes += amount

                    
        #Display boxes

                    
        elif answer == '2':
            print(f'You have {boxes} boxes in stock')

        #Display balance

            
        elif answer == '3':
            print(f'Your current balance is ${round(balance, 2)}')

        #Sell

            
        elif answer == '4':
            success = 0
            defective = 0
            if auto1 == 'y':
                ab = 0.85
                x = range(boxes)
                success = 0
                defective = 0
                b = 0
                for b in x:
                    if random.random() < ab:
                        success += 1
                    else:
                        defective += 1
                if timezz == 1:
                    time.sleep(1)
                print(f'You sold {success} boxes at prices of ${price} each!')
                balance += success * price
                boxes = 0
            else:
                
                amount2 = int(input('Enter amount of boxes to be sold: '))
                if amount2 > boxes:
                    print(f'You only have {boxes} boxes')
                else:
                    ab = 0.85
                    x = range(amount2)
                    success = 0
                    defective = 0
                    b = 0
                    for b in x:
                        if random.random() < ab:
                            success += 1
                        else:
                            defective += 1
                if timezz == 1:
                    time.sleep(1)
                print(f'You sold {success} boxes at prices of ${price} each!')
                balance += success
                boxes -= amount2

        #Upgrade

                
        elif answer == '5':
            print('What would you like to upgrade?')
            print(f'1. Price per box ${upgradePrice1}\n2. Storage[COMING SOON]')
            answer44 = input('Enter: ')
            if answer44 == '1':
                if balance >= upgradePrice1:
                    balance -= upgradePrice1
                    price *= 2
                    time.sleep(1)
                    upgradePrice1 = upgradePrice * 1.5
                    upgradePrice = upgradePrice1
                    print(f'Alright! Now your boxes sell for ${price} per box!')
                    
                elif balance < upgradePrice1:
                    print(f'Sorry, you have ${balance}, you need at least ${upgradePrice1}')
            elif answer44 == '2':
                print('COMING SOON')


        elif answer == 'hat':
            time.sleep(2)
            print('Hello, master')
            time.sleep(0.7)
            print('How much money does my lord desire?')
            moneyYES = int(input('Enter: ' ))
            time.sleep(0.5)
            print(f'Alright, ${moneyYES} has been added to your balance')
            balance += moneyYES
            time.sleep(1)
            print()
            print()

        #WIN!!!!!

                
        elif answer == '6':
            if balance >= 1000000:
                print('YOU WIN!!!!')
                timeedd = 0
                for xxxx in range(235):
                    print('=' * timeedd)
                    timeedd += 1
                    time.sleep(0.02)
                    if timeedd == 50:
                        print('yooo how it be?')
                time.sleep(0.1)
                time.sleep(2)
                import turtle
                t = turtle.getscreen()
                turtle = turtle.Turtle()
                turtle.fillcolor("yellow")
                turtle.begin_fill()
                turtle.circle(150)
                time.sleep(1)
                turtle.end_fill()
                time.sleep(2)
              # turtle.bye()
                game = 0
            else:
                print(f'Sorry... To win, you need $1,000,000 in your balance. You currently have ${balance}')

        elif answer == '7':
            print('1. Remove time (costs $300,000)\n2. Back')
            answertime = input('Enter: ')
            if answertime == '1':
                if balance >= 300000:
                    timezz = 0
                    balance -= 300000
                elif balance < 300000:
                    print(f'Sorry you only have ${balance}')

        #Save and Exit

                    
        elif answer == '8':
            print('Alright, save/exit.exe starting...')
            savefile = open('Box Game progress.data','w')
            savefile.write(str(balance))
            savefile.write('\n')
            savefile.write(str(upgrade))
            savefile.write('\n')
            savefile.write(str(price))
            savefile.write('\n')
            savefile.write(str(boxes))
            savefile.write('\n')
            savefile.write(str(upgradePrice))
            savefile.write('\n')
            savefile.write(str(upgradePrice1))
            savefile.close()
            time.sleep(2)
            game = 0
            #exit()
                 
def intro():
    print('Welcome to the Box Company!')
    print('===========================')


main()
