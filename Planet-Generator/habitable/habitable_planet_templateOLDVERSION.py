t.goto(0,0)
###START OF NEW CODE###
time.sleep(0.0)
t.penup()
print("lifting pen")
time.sleep(0.0)
t.goto(50.0,0)
print("moving to x:50.0 y:0")
time.sleep(0.0)
t.goto(100.0,0)
print("moving to x:100.0 y:0")
time.sleep(0.0)
t.goto(150.0,0)
print("moving to x:150.0 y:0")
time.sleep(0.0)
t.goto(170.0,0)
print("moving to x:170.0 y:0")
time.sleep(0.0)
t.pencolor(atmo1,atmo2,atmo3)
print("changing pen color to atmosphere")
time.sleep(0.0)
#sea atmosphere
t.fillcolor(atmo1,atmo2,atmo3)
print("changing fill color to atmosphere")
t.begin_fill()
print("begining fill")
time.sleep(0.0)
t.circle(170)
print("drawing circle")
time.sleep(0.0)
t.end_fill()
print("filling")
time.sleep(0.0)
t.penup()
print("lifting pen")
time.sleep(0.0)
t.goto(150.0,0)
print("moving to x:150.0 y:0")
time.sleep(0.0)
t.pendown()
print("dropping pen")
time.sleep(0.0)
t.fillcolor(sea1,sea2,sea3)
print("changing fill color to sea")
t.begin_fill()
print("begining fill")
time.sleep(0.0)
t.circle(150)
print("drawing circle")
time.sleep(0.0)
t.end_fill()
print("filling")
time.sleep(0.0)
t.penup()
print("lifting pen")
time.sleep(0.0)
t.goto(100.0,0)
print("moving to x:100.0 y:0")
time.sleep(0.0)
t.goto(50.0,0)
print("moving to x:50.0 y:0")
time.sleep(0.0)
t.goto(0.0,0)
print("moving to x:0.0 y:0")