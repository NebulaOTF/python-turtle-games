import turtle
import time

k = turtle.Turtle()
k.speed(100)
k.color("red")
def centre():
  k.penup()
  k.goto(0,0)
  k.pendown()
#one which is at a right angle  
def regular():
  for i in range(12):
    distance =  - (15 * i)
    k.goto(distance, 0)
    k.goto(0, (-180) - distance)
    centre()
  for i in range(12):
    distance = (15 * i)
    k.goto(distance, 0)
    k.goto(0, (-180) + distance)
    centre()
  for i in range(12):
    distance =  - (15 * i)
    k.goto(distance, 0)
    k.goto(0, 180 + distance)
    centre()
  for i in range(12):
    distance =  (15 * i)
    k.goto(distance, 0)
    k.goto(0, (180) - distance)
    centre()
#one which is not at a right angle
def irregular(angle):
  values = []
  for i in range(15):
    k.left(angle*i)
    for i in range(12):
      distance = 15* i
      k.forward(distance)
      values.append(k.pos())
      centre()
    k.left(angle)
    for i in range(12):
      distance = 15*i
      k.forward(distance)
      k.goto(values[-i])
      centre()
  del values[:]
irregular(45)
time.sleep(5)
k.clear()
regular()
