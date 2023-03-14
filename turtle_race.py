# Author : D. Sai Hemanth Reddy
# Date : 13 March 2023

# Import required modules and classes
import random
from turtle import Turtle, Screen

# Create a Screen object and set its dimensions
sc = Screen()
sc.setup(width=800, height=600)

# Ask the user to bet on a turtle
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race ? (Enter a number [0,4])")

# Define a list of colors to choose from
colors = ["red", "blue", "green", "yellow", "orange", "pink", "violet", "black", "brown"]

# Create five Turtle objects and set their colors randomly
t = [0 for i in range(5)]
for i in range(5):
    t[i] = Turtle(shape="turtle")
    t[i].penup()
    t[i].color(random.choice(colors))

# Position the turtles at the starting line
t[4].goto(-380, -200)
t[3].goto(-380, -100)
t[1].goto(-380, 100)
t[0].goto(-380, 200)
t[2].goto(-380, 0)

# Define a function that moves each turtle forward by a random amount
def race():
    t[0].forward(random.randint(0, 10))
    t[1].forward(random.randint(0, 10))
    t[2].forward(random.randint(0, 10))
    t[3].forward(random.randint(0, 10))
    t[4].forward(random.randint(0, 10))

# Keep running the race until one of the turtles crosses the finish line
while t[0].pos()[0] < 360 and t[1].pos()[0] < 360 and t[2].pos()[0] < 360 and t[3].pos()[0] < 360 and t[4].pos()[0] < 360:
    race()

# Determine whether the user's bet turtle crossed the finish line before the others
if t[int(user_bet)].pos()[0] >= 360:
    print("You won")
else:
    print("You Lost")

# Close the screen when the user clicks on it
sc.exitonclick()
