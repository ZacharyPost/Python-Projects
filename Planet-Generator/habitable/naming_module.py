t.goto(0,0)
###START OF NEW CODE###
time.sleep(0)
t.penup()
print("lifting pen")
time.sleep(0)
t.goto(-80.0,-190.0)
time.sleep(0)
t.pendown()
print("dropping pen")
time.sleep(0)
t.pencolor("white")
print("Changing pen color to white")
t.write("Planet", align="left",font=('Arial',12))
t.penup()


t.goto(-80.0,-215.0)
time.sleep(0)
t.pendown()
print("dropping pen")
time.sleep(0)
t.pencolor("white")
print("Changing pen color to white")

#Random Name

with open("names.txt", "r") as file:
    allText = file.read()
    file.close()
    names = list(map(str, allText.split()))
name = random.choice(names)
#print(name)
t.write(name, align="left",font=('Arial',15,'bold'))
time.sleep(1.5)
t.penup()
