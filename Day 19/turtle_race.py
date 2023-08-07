import random
import turtle as t


is_race_on = False # to activate or deactivate the race


screen = t.Screen()
screen.setup(width=500, height=400) # resize window
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'green', 'yellow', 'orange', 'purple', 'blue']
all_turtles = []

def turtle_pos(turtle_colors, x_pos):
    y_pos = -150
    for color in turtle_colors:
        new_turtle = t.Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=x_pos, y=y_pos)
        y_pos += 60
        all_turtles.append(new_turtle)

turtle_pos(turtle_colors=colors, x_pos=-230)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210: # determine a winner
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. {winning_color.capitalize()} made you money")
            else:
                print(f"You've lost. {winning_color.capitalize()} is a winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
