import turtle
from turtle import Turtle, Screen
import random
is_race_on=False
screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")
colors=["red","orange", "yellow", "green", "blue", "purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
if user_bet:
    is_race_on=True
for turtles in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtles])
    new_turtle.goto(-235,y_positions[turtles])
    all_turtles.append(new_turtle)
while is_race_on:
     for turtles in all_turtles:
        if turtles.xcor()>210:
            winner=turtles.pencolor()
            if winner==user_bet:
                print(f"Your {winner} Turtle Wins")
                is_race_on=False
            else:
                print(f"Your {user_bet} Turtle Loses")
                is_race_on=False
        Random_distance=random.randint(0,20)
        turtles.forward(Random_distance)
screen.exitonclick()