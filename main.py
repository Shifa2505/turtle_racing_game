from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
new_turtle = []


for turtle_index in range(0,6):
    rhys = Turtle(shape="turtle")
    rhys.color(colors[turtle_index])
    rhys.penup()
    rhys.goto(x=-230, y= y_position[turtle_index])
    new_turtle.append(rhys)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in new_turtle:

        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You've won! The {winner} turtle has won the race.")
            else:
                print(f"You've lost! The {winner} turtle has won the race.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
