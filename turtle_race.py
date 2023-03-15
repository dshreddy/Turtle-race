# Author : D. Sai Hemanth Reddy
# Date : 13 March 2023

import random
from turtle import Turtle, Screen

sc = Screen()
sc.setup(width=800, height=600)


def game():
    colors = ["red", "blue", "green", "yellow", "orange", "pink", "violet", "black", "brown"]
    t = [0 for i in range(5)]

    for i in range(5):
        t[i] = Turtle(shape="turtle")
        t[i].speed("fastest")
        t[i].penup()
        t[i].color(random.choice(colors))

    t[4].goto(-380, -200)
    t[3].goto(-380, -100)
    t[1].goto(-380, 100)
    t[0].goto(-380, 200)
    t[2].goto(-380, 0)

    allowed_values = ['0', '1', '2', '3', '4']
    user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race ? (Enter a number [0,4])")

    while user_bet not in allowed_values:
        user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race ? (Enter a number [0,4])")

    def race():
        t[0].forward(random.randint(0, 10))
        t[1].forward(random.randint(0, 10))
        t[2].forward(random.randint(0, 10))
        t[3].forward(random.randint(0, 10))
        t[4].forward(random.randint(0, 10))

    while t[0].pos()[0] < 360 and t[1].pos()[0] < 360 and t[2].pos()[0] < 360 and t[3].pos()[0] < 360 and t[4].pos()[
        0] < 360:
        race()

    res = []
    res.append((t[0].pos()[0], 0))
    res.append((t[1].pos()[0], 1))
    res.append((t[2].pos()[0], 2))
    res.append((t[3].pos()[0], 3))
    res.append((t[4].pos()[0], 4))
    res.sort()
    res.reverse()

    if res[0][0]!=res[1][0]:
        pr = '''Press 1 to play again, any other key to exit
        '''+"Winner(s) ="+str(res[0][1])
    else:
        pr = '''Press 1 to play again, any other key to exit
        ''' + "Winner(s) =" + str(res[0][1])
        i = 1
        while i <= 4 and res[i][0] == res[0][0]:
            pr += " "+str(res[i][1])
            i += 1

    if t[int(user_bet)].pos()[0] >= 360:

        inp = sc.textinput(title="You Won", prompt=pr)
        if inp == '1':
            sc.clear()
            game()
    else:
        inp = sc.textinput(title="You Lost", prompt=pr)
        if inp == '1':
            sc.clear()
            game()


game()

