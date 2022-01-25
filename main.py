from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Input the color: ")
print(user_bet)
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            wining_turtle = turtle.pencolor()
            if wining_turtle == user_bet:
                print(f"You won,{wining_turtle} turtle is the winner!!")
            else:
                print(f"You lost,{wining_turtle} turtle is the winner!!")
            is_race_on = False

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
