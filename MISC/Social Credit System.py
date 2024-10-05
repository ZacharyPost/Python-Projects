import random
import time
#print('This is a test!')
print()
play = 1
dead = 0
ab = 0.01
disDEATH = range(5, 25)
day = range(4,10)

    #Random.random chances

humanchances = [3, 3, 2, 2, 2, 1, 1, 1, 1]
#humanchances = [1]

humancreate = 0.3
humanright = 0.4
humanwrong = 0.2
    #Human properties


humanscore = {'Bob':1000,'Jack':1000}

humansage = {'Bob':20,'Jack':40}

humanseye = {'Bob':'blue','Jack':'green'}

humansheight = {'Bob':160,'Jack':172}

humansanimal = {'Bob':'Cat','Jack':'Parakeet'}

humansgenre = {'Bob':'Metal','Jack':'Rock'}

humansfood = {'Bob':'Steak','Jack':'Sushi'}

humansbrand = {'Bob':'ZZ Corporations','Jack':'Google'}

humanscatchphrase = {'Bob':'Great!'}


    #Human properties resources


    #HUMAN ACTIONS

wrongactions = ['Robbed','Protested','Watched','VPN','Murder','GiveSeat']
#wrongactions = ['Murder']
rightactions = ['Gave','Return','Reported','Watched','GiveSeat']


age = range(10,90)
height = range(120,200)
eye = ['blue','brown','hazel','green']
animals = ['Cat','Dog','Parakeet','Zebra','Dolphin','Hampster','Parrot','Eagle']
genre = ['Pop','Metal','Rock','Country','Blues','Jazz','Opera','Funk']
food = ['Steak','Chicken','Pizza','Waffles','Beef','Mozzarella cheese','Bacon','Asparagus','Sushi','Sushi','Cashew nuts','Chai Tea']
brand = ['Nike','Addidas','Google','Apple','Samsung','Disney','ZZ Corporations']
catchphrase = ['Hello there!']
score = 1000

execution = 300


    #List of potential names

with open("names.txt", "r") as file:
    allText = file.read()
    file.close()
    names = list(map(str, allText.split()))

    #List of living humans

#humans = ['Bob','Jack']
humans = []
DEADhumans = []

    #Human creator

#print(humans)
#print()
#create = input('Enter human name: ')
#humans.append(create)
#humansage[create] = random.choice(age)
#humanseye[create] = random.choice(eye)
#humansheight[create] = random.choice(height)

#print(humans)
#print(humansage)
#print(humansheight)
#print(humanseye)
#print()
#print(f'THIS IS TEST')
#print(random.random)


#MAIN WHILE LOOP, THE DAY CYCLE





while play == 1:
    if len(humans) == 0:
        dead = 1
        I = 0
    else:
        dead = 0
        I = 1
    time.sleep(1)
    print()
    print('A new day is beginning')
    #time.sleep(5)
    print()
    print('=' * 60)
    print()
    print('What would you like to do?')
    print('1. Start day\n2. Lookup human\n3. Create human\n4. Misc\n5. Exit')


    #Decision

            #1. START DAY CODE

    answer = input('Enter: ')

    if answer == '1':
        amount = random.choice(day)
        daDead = dead
        #print(f'The amount is {amount}')
        for x in range(amount):
            if dead == 1:
                if daDead == 1:
                    print("There're no humans in your city")
                    daDead = 0
                print()
                amount = 0
            else:
                time.sleep(1.2)
                human_chance = random.choice(humanchances)
                #print(human_chance)
                print()



                #DISASTERS!!!!!!
                if len(humans) > 10:
                    if random.random() < ab:
                        print()
                        print('A flood has occurred!!!!')
                        for Y in range(random.choice(disDEATH)):
                            if I == 1:
                                dishuman = random.choice(humans)
                                print(f'{dishuman} was killed in the flood!')
                                humans.remove(dishuman)
                                DEADhumans.append(dishuman)
                                if len(humans) == 0:
                                    #print('Oh no!! All of your humans have died.')
                                    amount = 0
                                    x = 0
                                    dead = 1
                                    I = 0
                        time.sleep(1)
                        print()
                        asjdas = input('Enter: ')
                        print()
                        time.sleep(1)
                                
                if len(humans) == 0:
                    print('Oh no!! All of your humans have died.')
                    amount = 0
                    x = 0
                    dead = 1
                else:
                    
                            

                    #HUMAN BORN



                        
                    if human_chance == 3:
                        print('A human was born!')
                        newhumanname = random.choice(names)
                        print(f'Their name is {newhumanname}')

                        
                        humans.append(newhumanname)
                        humanscore[newhumanname] = 1000
                        humansage[newhumanname] = random.choice(age)
                        humanseye[newhumanname] = random.choice(eye)
                        humansheight[newhumanname] = random.choice(height)
                        humansanimal[newhumanname] = random.choice(animals)
                        humansgenre[newhumanname] = random.choice(genre)
                        humansbrand[newhumanname] = random.choice(brand)
                        humanscatchphrase[newhumanname] = random.choice(catchphrase)


                #RIGHT ACTIONS

                        
                    elif human_chance == 2:
                        righthuman = random.choice(humans)
                        theiright = random.choice(rightactions)
                        #print(theiright)
                        if theiright == 'Gave':
                            print(f'{righthuman} just gave 50 Renminbi to the government!')
                            print('They earned 30 social credits :)')
                            humanscore[righthuman] += 30

                            
                        elif theiright == 'Return':
                            print(f'{righthuman} just returned some lost items to the government!')
                            print('They earned 15 social credits :)')
                            humanscore[righthuman] += 15

                            
                        elif theiright == 'Reported':
                            print(f'{righthuman} just reported a potential protest to the local law enforcement!')
                            print('They earned 20 social credits :)')
                            humanscore[righthuman] += 20

                        elif theiright == 'Watched':
                            print(f'{righthuman} just watched AND enjoyed a whole speech made by you!')
                            print('They earned 100 social credits :)')
                            humanscore[righthuman] += 100

                        elif theiright == 'GiveSeat':
                            print(f'{righthuman} just gave their seat to an elder!')
                            print('They earned 20 social credits :)')
                            humanscore[righthuman] += 20

                #WRONG ACIONS
                            
                    elif human_chance == 1:
                        wronghuman = random.choice(humans)
                        theirwrong = random.choice(wrongactions)
                        if theirwrong == 'Robbed':
                            print(f'{wronghuman} just robbed a local 7-11 last night!')
                            print('They just lost 100 social credits! :(')
                            humanscore[wronghuman] -= 100
                            
                        elif theirwrong == 'Protested':
                            print(f'{wronghuman} protested in the streets about an inferior opinion!')
                            print('They just lost 50 social credits! :(')
                            humanscore[wronghuman] -= 50

                        elif theirwrong == 'Watched':
                            print(f'{wronghuman} watched and did NOT enjoy a speech made by you!')
                            print('They just lost 200 social credits! :(')
                            humanscore[wronghuman] -= 200

                        elif theirwrong == 'GiveSeat':
                            print(f'{wronghuman} did not give their seat up to a pregnant women :O')
                            print('They just lost 20 social credits! :(')
                            humanscore[wronghuman] -= 20

                        elif theirwrong == 'VPN':
                            print(f'{wronghuman} was caught using a VPN!')
                            print('They just lost 350 social credits! :(')
                            humanscore[wronghuman] -= 350

                        elif theirwrong == 'Murder':
                            if len(humans) < 4:
                                print('A murder was attempted')
                            else:
                                murderchoice = random.choice(humans)
                                print(f'{wronghuman} just murdered {murderchoice}!!!!')
                                humans.remove(murderchoice)
                                DEADhumans.append(murderchoice)
                                time.sleep(1)
                                print()
                                print('What would you like to do about this terrible action?')
                                print('1. Execute\n2. Take 500 social credits\n3. Nothing')
                                print()
                                murderAnswer = input('Enter: ')
                                time.sleep(0.4)
                                if murderAnswer == '1':
                                    print('They shall be executed right away!')
                                    if wronghuman in humans:
                                        humans.remove(wronghuman)
                                        DEADhumans.append(wronghuman)
                                elif murderAnswer == '2':
                                    print('We shall gladly take it from them.')
                                    humanscore[wronghuman] -= 500
                                else:
                                    print('Of course. Your will be done sir.')

                        if humanscore[wronghuman] <= 300:
                            print(f"{wronghuman}'s social score is under 350 :O")
                            time.sleep(1)
                            print(f'{wronghuman} has just been executed')
                            humans.remove(wronghuman)
                            DEADhumans.append(dishuman)
                                
                            #del humansage[wronghuman]
                    else:
                        print('Nothing')
                        print()
                    if len(humans) == 0:
                        print('Oh no!! All of your humans have died.')
                        amount = 0
                        x = 0
                        dead = 1
                    print()
                    print()
                    Nehext = input('Enter to continue: ')
                    print()

    #SEARCH

    elif answer == '2':
        print('Getting newest list of humans')
        time.sleep(1)
        print()
        print(humans)
        print()
        print('Enter the name of the human you would like to inspect')
        inspect = input('Enter: ')
        if inspect in humans:
            print()
            time.sleep(0.1)
            print('=' * 60)
            name_pos = humans.index(inspect)
            print('Name:', humans[name_pos])
            print('Age:', humansage.get(inspect))
            print('Height:', humansheight.get(inspect),'cm')
            print('Eye color:', humanseye.get(inspect))
            print('Favorite animal:', humansanimal.get(inspect))
            print('Favorite musical genre:', humansgenre.get(inspect))
            print('Favorite brand:', humansbrand.get(inspect))
            print('Favorite catchphrase:', humanscatchphrase.get(inspect))
            print()
            print('Current Social score', humanscore.get(inspect))
            print()
            print('=' * 60)
            time.sleep(1.1)
            print()
            print(f'What would you like to do with {inspect}?')
            print('1. Back\n2. Execute\n3. Change Social Score\n4. Change favorite brand')
            print()
            ansa = input('Enter: ')
            print()

            if ansa == '1':
                print('Returning')
            elif ansa == '2':
                print('Are you sure? y = yes n = no')
                Sur = input('Enter: ')
                if Sur == 'y':
                    time.sleep(0.2)
                    print()
                    print('It will be done my lord')
                    time.sleep(1)
                    humans.remove(inspect)
                    DEADhumans.append(inspect)
            elif ansa == '3':
                newnewscore = int(input('Enter new score: '))
                humanscore[inspect] = newnewscore
            elif ansa =='4':
                newnewbrand = input('Enter new favorite brand: ')
                humansbrand[inspect] = newnewbrand
                

        else:
            print()
            print(f'{inspect} does not exist')
            print()
        #print(inspect)




        
        #CREATE HUMAN

    elif answer == '3':
        print('What option would you like?')
        print('1. Create custom human\n2. Mass populate')
        Answer2 = input('Enter: ')
        if Answer2 == '1':
            print()
            time.sleep(0.3)
            NEWname = input('What is their name?: ')
            print()
            time.sleep(0.3)
            NEWage = int(input('How old are they?: '))
            print()
            time.sleep(0.3)
            NEWheight = int(input('What is their height? (in centimeters): '))
            print()
            time.sleep(0.3)
            NEWeye = input('What is their eye color?: ')
            print()
            time.sleep(0.3)
            NEWanimal = input('What is their favorite animal?: ')
            print()
            time.sleep(0.3)
            NEWgenre = input('What is their favorite music genre?: ')
            print()
            time.sleep(0.3)
            NEWbrand = input('What is their favorite brand?: ')
            print()
            time.sleep(0.3)
            NEWcatchphrase = input('What is their favorite catch phrase?: ')
            print()
            time.sleep(0.3)
            print('Alright, creating new human...')

            humans.append(NEWname)
            humanscore[NEWname] = 1000
            humansage[NEWname] = NEWage
            humanseye[NEWname] = NEWeye
            humansheight[NEWname] = NEWheight
            humansanimal[NEWname] = NEWanimal
            humansgenre[NEWname] = NEWgenre
            humansbrand[NEWname] = NEWbrand
            humanscatchphrase[NEWname] = NEWcatchphrase

            time.sleep(2)
            print()
            print(f'{NEWname} has just been added to the game!')


        elif Answer2 == '2':
            print('How many humans would you like to produce?')
            produceEnter = int(input('Enter: '))
            print()
            print(f' Mass producing {produceEnter} humans')
            time.sleep(3)
            for ss in range(produceEnter):
                    newhumannameX = random.choice(names)
                    time.sleep(0.01)
                    print(f'{newhumannameX}')

                    
                    humans.append(newhumannameX)
                    humanscore[newhumannameX] = 1000
                    humansage[newhumannameX] = random.choice(age)
                    humanseye[newhumannameX] = random.choice(eye)
                    humansheight[newhumannameX] = random.choice(height)
                    humansanimal[newhumannameX] = random.choice(animals)
                    humansgenre[newhumannameX] = random.choice(genre)
                    humansbrand[newhumannameX] = random.choice(brand)
                    humanscatchphrase[newhumannameX] = random.choice(catchphrase)
            print()
            print()




    #MISC


    elif answer == '4':
        print()
        time.sleep(0.2)
        print('Miscellaneous stuff')
        print()
        print("1.Nuke city BETA\n2.Change all humans' score")
        print()
        misc_answer = input('Enter: ')
        if misc_answer == '1':
            print('Are you sure? y = yes n = no')
            misc_answer2 = input('Enter: ')
            if misc_answer2 == 'y':
                print()
                print('Nuking city...')
                time.sleep(1.2)
                humans = []
                print('City has been nuked and all humans have died')
        elif misc_answer == '2':
            print('Will be added soon...')



    #EXIT

    elif answer == '5':
        print('Are you sure? y = yes n = no')
        finalanswer = input('Enter: ')
        if finalanswer == 'y':
            print('Removing city')
            time.sleep(2)
            play = 0
            

    #Book of the DEAD

    elif answer == 'dead':
        print('Accessing the Book of the Dead...')
        time.sleep(1.2)
        print()
        print(DEADhumans)
        print()
        print('Enter the name of the human you would like to inspect')
        print()
        DEADinspect = input('Enter: ')


        if DEADinspect in DEADhumans:
            print()
            print(f'BOOK OF THE DEAD - {DEADinspect}')
            print('=' * 60)
            DEADname_pos = DEADhumans.index(DEADinspect)
            print('Name:', DEADhumans[DEADname_pos])
            print('Age:', humansage.get(DEADinspect))
            print('Height:', humansheight.get(DEADinspect),'cm')
            print('Eye color:', humanseye.get(DEADinspect))
            print('Favorite animal:', humansanimal.get(DEADinspect))
            print('Favorite musical genre:', humansgenre.get(DEADinspect))
            print('Favorite brand:', humansbrand.get(DEADinspect))
            print('Favorite catchphrase:', humanscatchphrase.get(DEADinspect))
            print()
            print('Current Social score', humanscore.get(DEADinspect))
            print()
            print('=' * 60)
            print()
            time.sleep(0.5)
            print(f'What would you like to do with {DEADinspect}?')
            print('1. Back\n2. Bring to life')
            DEAD2answer = input('Enter: ')
            if DEAD2answer == '2':
                print(f'Bringing {DEADinspect} back to life...')
                time.sleep(1.1)
                DEADhumans.remove(DEADinspect)
                humans.append(DEADinspect)
                humanscore[DEADinspect] = 1000
            else:
                print('Returning')
        else:
            print()
            print(f'{DEADinspect} does not exist')
            print()




            

