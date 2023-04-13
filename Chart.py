from QuadraticTurtle import *
from tkinter import *
from tkinter import ttk

def draw_chart(canvas):
    
    graphy = turtle.RawTurtle(canvas)
    graphy.ht()
    graphy.speed(0)
    graphy.penup()
    graphy.goto(250, 0)
    graphy.pendown()
    for i in range(0, 50):
        graphy.back(10)
        graphy.left(90)
        graphy.forward(3)
        graphy.back(3)
        graphy.right(90)
    graphy.penup()
    graphy.goto(0, -250)
    graphy.pendown()
    graphy.left(90)
    for i in range(0, 50):
        graphy.forward(10)
        graphy.left(90)
        graphy.forward(3)
        graphy.back(3)
        graphy.right(90)

class GUI():
    
    root = Tk()

    #This is the canvas the turtle will exist in
    canvas = Canvas(root, width = 500, height = 500)
    canvas.pack()
    draw_chart(canvas)
    turtles = [QuadraticTurtle(canvas)]
    

    turtles[0].color("red")
    turtles[0].solve_y(-.04, -.4, 5, -15, 15)
    
    turtles[0].color("blue")
    turtles[0].solve_y(.05, -.4, 5)
    turtles[0].color("green")
    turtles[0].solve_y(-.55, 1.5, 3.2)
    turtles[0].color("pink")
    turtles[0].solve_y(.27, 1.5, 1.8)
    

    
    root.mainloop()

GUI()


