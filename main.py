import turtle

colours = [
    "yellow", "cyan", "red", "blue", "magenta", "white", "green"
]

cycles = 6
size = 50
offset = 10
window = turtle.Screen()
window.bgcolor("black")
turtle.pensize(0.5)
turtle.speed(0.5)

for i in range(cycles):
    for c in colours:
        turtle.color(c)
        turtle.circle(size)
        turtle.left(offset)

turtle.hideturtle()            