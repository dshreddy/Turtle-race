# Author : D. Sai Hemanth Reddy
# Date : 13 March 2023
import random
from turtle import Turtle, Screen

sc = Screen()
sc.setup(width=800, height=600)
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race ? (Enter a number [0,4])")

colors = ["red", "blue", "green", "yellow", "orange", "pink", "violet", "black", "brown"]

t = [0 for i in range(5)]

for i in range(5):
    t[i] = Turtle(shape="turtle")
    t[i].penup()
    t[i].color(random.choice(colors))

t[4].goto(-380, -200)
t[3].goto(-380, -100)
t[1].goto(-380, 100)
t[0].goto(-380, 200)
t[2].goto(-380, 0)


def race():
    t[0].forward(random.randint(0, 10))
    t[1].forward(random.randint(0, 10))
    t[2].forward(random.randint(0, 10))
    t[3].forward(random.randint(0, 10))
    t[4].forward(random.randint(0, 10))


while t[0].pos()[0] < 360 and t[1].pos()[0] < 360 and t[2].pos()[0] < 360 and t[3].pos()[0] < 360 and t[4].pos()[0] < 360:
    race()

if t[int(user_bet)].pos()[0] >= 360:
    print("You won")
else:
    print("You Lost")
sc.exitonclick()
