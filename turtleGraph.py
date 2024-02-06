# # Name: Teng Tze Hui & Ng Jace Xin
# # Student ID: 2214209 & 2214593
# # Class: DAAA/2B/01

import turtle
import sympy as sp
import numpy as np
import re

class EquationGraph:
    def __init__(self):
        self.equations = []

    def is_valid_equation(self, equation_str):
        # Check if 'x' and 'y' are present in the equation
        if 'x' in equation_str and 'y' in equation_str:
            return True
        return False

    def input_equations(self):
        while True:
            try:
                num_equations = int(input("Enter the number of equations (must be a positive integer): "))
                if num_equations > 0:
                    break  # Break out of the loop if a valid input is provided
                else:
                    print("Please enter a positive integer greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
                

        for i in range(num_equations):
            while True:
                equation_str = input(f"Enter equation {i + 1} in a suitable format (eg. y = 2 * x + 1): ")
                
                # Validate the input format
                if self.is_valid_equation(equation_str):
                    break  # Break out of the loop if a valid input is provided
                else:
                    print("Invalid input. Please enter 'x' and 'y' in the equation.")

            if '=' in equation_str:
                _, equation_str = equation_str.split('=')

            self.equations.append(sp.simplify(equation_str))

    def customize_graph(self):
        color = input("Enter the color for the graph (default is blue): ") or "blue"
        linestyle = input("Enter the linestyle for the graph ('-' or '-.') (default is solid line): ") or "-"
        return color, linestyle

    def draw_graph(self, color="blue", linestyle="-"):
        turtle.speed("fastest")
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

        for equation in self.equations:
            self.draw_single_equation(equation, color, linestyle)

        # Implement interactive features
        turtle.onscreenclick(self.on_click)
        turtle.done()
        
    def draw_single_equation(self, equation, color, linestyle):
        turtle.speed("fastest")

        x_vals = np.linspace(-10, 10, 400)
        y_vals = np.array([sp.N(equation.subs('x', val)) for val in x_vals])

        turtle.penup()
        turtle.color(color)
        turtle.goto(x_vals[0] * 40, y_vals[0] * 40)

        turtle.pendown()
        turtle.pencolor(color)
        turtle.pensize(2)
        turtle.setheading(90)
        turtle.pendown()

        # Set linestyle
        if linestyle == "-.":
            for i in range(1, len(x_vals), 3):
                turtle.speed("fastest")
                turtle.penup()
                turtle.goto(x_vals[i] * 40, y_vals[i] * 40)
                turtle.pendown()
                turtle.goto(x_vals[i + 2] * 40, y_vals[i + 2] * 40)
        else:
            for i in range(1, len(x_vals)):
                turtle.speed("fastest")
                turtle.penup()
                turtle.goto(x_vals[i - 1] * 40, y_vals[i - 1] * 40)
                turtle.pendown()
                turtle.goto(x_vals[i] * 40, y_vals[i] * 40)

        # Reset linestyle
        turtle.pendown()
        turtle.pencolor(color)
        turtle.pensize(2)

    def on_click(self, x, y):
        print(f"Clicked at ({x}, {y})")


# # Example usage
# game = EquationGraph()
# game.input_equations()
# color, linestyle = game.customize_graph()
# game.draw_graph(color, linestyle)
