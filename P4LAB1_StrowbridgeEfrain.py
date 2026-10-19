# Efrain Strowbridge
# 10/19/26
# P4LAB1
# This program will visualize a square and a triangle, in the shape of a house, using turtle graphics.

# create the turtle
import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)
t.color("green")
t.pencolor("black")
t.shape("turtle")

# define the triangle function
def draw_triangle():
    for i in range(3):
        t.forward(50)
        t.left(120)
        t.forward(50)

# define the square function
def draw_square():
    i = 0
    while i < 4:
        t.forward(50)
        t.right(90)
        t.forward(50)
        i += 1

# define the drawing name function
def draw_name():
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.write("Efrain Strowbridge", font=("courier", 30, "normal", "bold"))
    t.penup()
    t.goto(0, 0)
    t.pendown()

# define the main function
def main():
    draw_triangle()
    draw_square()
    t.left(90)
    draw_name()

# Run the code.
main()
window.mainloop()