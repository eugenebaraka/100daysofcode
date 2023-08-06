import turtle as t

timmy = t.Turtle()

timmy.speed("fastest")

for _ in range(100):
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)





screen = t.Screen()
screen.exitonclick()
