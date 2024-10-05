import random
import time
from openai import OpenAI
import os




def main():
    #global money
    money = 1
    #x1,x2,x3,x4,x5,x6,x7,x8,x9 = "O","O","O","O","O","O","O","O","O"
    farm = ["X","X","X","X","X","X","X","X","X"]
    inventory = {"wheat":1,"tulips":2}
    crop_time = [0,0,0,0,0,0,0,0,0]
    #farm = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
    seeds = {}
    crops = {}
    day = 0
    game = 1
    print("MAIN")
    #time.sleep(1)
    while game == 1:
        for key, value in inventory.items() :
            if key not in seeds:
                seeds.update({key: 0})
        for key, value in inventory.items() :
            if key not in crops:
                crops.update({key: 0})
        #day += 1
        print()
        print()
        print(f"======== DAY #{day} ========")
        PrintFarm(farm,crop_time)
        




            
            
            
        print()
        print()
        #print("money" , money)
        print(f"Seeds: {seeds}")
        print(f"Crops: {crops}")
        #print(money)
        print(f"Money: {money}")
        print("1. Buy seeds\n2. Plant seeds\n3. Next day\n4. Sell crops")
        choice = input("Enter: ")
        print()
        
        
        if choice == "1":
            #print(money)
            
            print("=== STORE ===")
            print(f"Money: {money}")
            print(inventory)
            choice = input("Enter: ")
            if choice in inventory:
                choice = choice.lower()
                amount = int(input("Enter amount: "))
                amount_price = amount * inventory.get(choice)
                if money < amount_price:
                    print("=== ERROR not enough money ===")
                    #time.sleep(2)
                else:
                    money -= amount_price
                    seeds[choice] += amount
            else:
                print("=== ERROR seed does not exist ===")
            
        elif choice == "2":
            print()
            print("=== PLANT ===")
            print(f"Seeds: {seeds}")
            seed = input("Select seed: ")
            if seed in seeds:
                if seeds.get(seed) >= 1:
                    print(f"What plot would you like to plant {seed}?")
                    plot = input("Enter: ")
                    print(plot)
                    random_time = range(2,4)
                    if plot == "1":
                        if farm[0] == "X":
                            farm[0] = seed
                            crop_time[0] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")
                    elif plot == "2":
                        if farm[1] == "X":
                            farm[1] = seed
                            crop_time[1] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")
                    elif plot == "3":
                        if farm[2] == "X":
                            farm[2] = seed
                            crop_time[2] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")                            
                    elif plot == "4":
                        if farm[3] == "X":
                            farm[3] = seed
                            crop_time[3] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")
                    elif plot == "5":
                        if farm[4] == "X":
                            farm[4] = seed
                            crop_time[4] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")
                    elif plot == "6":
                        if farm[5] == "X":
                            farm[5] = seed
                            crop_time[5] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")
                    elif plot == "7":
                        if farm[6] == "X":
                            farm[6] = seed
                            crop_time[6] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")
                    elif plot == "8":
                        if farm[7] == "X":
                            farm[7] = seed
                            crop_time[7] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")
                    elif plot == "9":
                        if farm[8] == "X":
                            farm[8] = seed
                            crop_time[8] = random.choice(random_time)
                            seeds[seed] -= 1
                        else:
                            print("=== ERROR plot is in use ===")
                    else:
                        print("=== ERROR plot does not exist ===")
                    
                    
                else:
                    print("=== ERROR not enough seeds ===")
            else:
                print("=== ERROR seed does not exist ===")
                
        elif choice == "3":
            chance = [1,0,0,0]
            random_chance = random.choice(chance)
            if random_chance == 1:
                random_price = range(2, 7)
                bob = ""
                ai = TalkAI(bob)
                #print(ai)
                inventory.update({ai.lower(): random.choice(random_price)})
            time.sleep(2)
            day += 1
            if crop_time[0] >= 1:
                crop_time[0] -= 1
                if crop_time[0] == 0:
                    crops[farm[0]] += 1
                    farm[0] = "X"
                    
            if crop_time[1] >= 1:
                crop_time[1] -= 1
                if crop_time[1] == 0:
                    crops[farm[1]] += 1
                    farm[1] = "X"
                    
            if crop_time[2] >= 1:
                crop_time[2] -= 1
                if crop_time[2] == 0:
                    crops[farm[2]] += 1
                    farm[2] = "X"
                    
            if crop_time[3] >= 1:
                crop_time[3] -= 1
                if crop_time[3] == 0:
                    crops[farm[3]] += 1
                    farm[3] = "X"
                    
            if crop_time[4] >= 1:
                crop_time[4] -= 1
                if crop_time[4] == 0:
                    crops[farm[4]] += 1
                    farm[4] = "X"
                    
            if crop_time[5] >= 1:
                crop_time[5] -= 1
                if crop_time[5] == 0:
                    crops[farm[5]] += 1
                    farm[5] = "X"
                    
            if crop_time[6] >= 1:
                crop_time[6] -= 1
                if crop_time[6] == 0:
                    crops[farm[6]] += 1
                    farm[6] = "X"
                    
            if crop_time[7] >= 1:
                crop_time[7] -= 1
                if crop_time[7] == 0:
                    crops[farm[7]] += 1
                    farm[7] = "X"
                    
            if crop_time[8] >= 1:
                crop_time[8] -= 1
                if crop_time[8] == 0:
                    crops[farm[8]] += 1
                    farm[8] = "X"
                    
        elif choice == "4":
            print(f"Crops: {crops}")
            crop = input("Select crop: ")
            if crop in crops:
                if crops.get(crop) >= 1:
                    amount = int(input("Enter amount: "))
                    #print(inventory[crop])
                    amount2 = range(2,4)
                    amount1 = amount * random.choice(amount2)
                    money += inventory[crop] * amount1
                    crops[crop] -= amount
                    
                else:
                    print("=== ERROR not enough seeds ===")
            else:
                print("=== ERROR seed does not exist ===")
        
def PrintFarm(farm,crop_time):
    print()
    print(f"|{farm[0]}-{crop_time[0]}|{farm[1]}-{crop_time[1]}|{farm[2]}-{crop_time[2]}|\n|{farm[3]}-{crop_time[3]}|{farm[4]}-{crop_time[4]}|{farm[5]}-{crop_time[5]}|\n|{farm[6]}-{crop_time[6]}|{farm[7]}-{crop_time[7]}|{farm[8]}-{crop_time[8]}|")

def TalkAI(bob):
    
    AI_prompt = "Give me a random plant or flower NAME ONLY"
    tokens = 2000
    os.environ['OPENAI_API_KEY'] = 'ENTER YOUR API KEY'
    client = OpenAI()
    system = "Normal"
    #system = "Creative Vision, Technical Proficiency, Attention to Detail, Innovation, Adaptability, Emotional Depth, Communication Skills, Persistence, Influence, Business Acumen"
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      max_tokens = tokens,
          messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": AI_prompt}
          ]
    )
    return completion.choices[0].message.content
#def FarmCropTime(crop_time,farm):


    

main()
