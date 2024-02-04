# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

import turtle
import sympy as sp
import numpy as np

class EquationGraph:
    def __init__(self):
        self.equation = None

    def input_equation(self):
        equation_str = input("Enter a mathematical equation (eg. y = x + 1): ")
        if '=' in equation_str:
            _, equation_str = equation_str.split('=')
        # x = sp.symbols('x')
        self.equation = sp.simplify(equation_str)

    def draw_graph(self):

        # set the speed of drawing
        turtle.speed("fastest")

        # Set up the turtle window
        turtle.title("Equation Solver Game")
        turtle.bgcolor("white")
        turtle.setup(width=800, height=600)

        # Draw x-axis
        turtle.penup()
        turtle.goto(-400, 0)
        turtle.pendown()
        turtle.forward(800)

        # Draw y-axis
        turtle.penup()
        turtle.goto(0, -300)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(600)

        # Draw the graph of the equation
        x_vals = np.linspace(-10, 10, 400)
        y_vals = np.array([sp.N(self.equation.subs('x', val)) for val in x_vals])

        turtle.penup()
        turtle.color("blue")
        turtle.goto(x_vals[0] * 40, y_vals[0] * 40)

        turtle.pendown()
        for i in range(1, len(x_vals)):
            turtle.goto(x_vals[i] * 40, y_vals[i] * 40)

        
        turtle.hideturtle()
        turtle.done()

    def play_game(self):
        self.input_equation()
        print(f"Solving equation: {self.equation}")
        self.draw_graph()

