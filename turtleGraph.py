# # Name: Teng Tze Hui & Ng Jace Xin
# # Student ID: 2214209 & 2214593
# # Class: DAAA/2B/01

# import turtle
# import sympy as sp
# import numpy as np

# class EquationGraph:
#     def __init__(self):
#         self.equation = None

#     def input_equation(self):
#         equation_str = input("Enter a mathematical equation (eg. y = x + 1): ")
#         if '=' in equation_str:
#             _, equation_str = equation_str.split('=')
#         # x = sp.symbols('x')
#         self.equation = sp.simplify(equation_str)

#     def draw_graph(self):

#         # set the speed of drawing
#         turtle.speed("fastest")

#         # Set up the turtle window
#         turtle.title("Equation Solver Game")
#         turtle.bgcolor("white")
#         turtle.setup(width=800, height=600)

#         # Draw x-axis
#         turtle.penup()
#         turtle.goto(-400, 0)
#         turtle.pendown()
#         turtle.forward(800)

#         # Draw y-axis
#         turtle.penup()
#         turtle.goto(0, -300)
#         turtle.pendown()
#         turtle.setheading(90)
#         turtle.forward(600)

#         # Draw the graph of the equation
#         x_vals = np.linspace(-10, 10, 400)
#         y_vals = np.array([sp.N(self.equation.subs('x', val)) for val in x_vals])

#         turtle.penup()
#         turtle.color("blue")
#         turtle.goto(x_vals[0] * 40, y_vals[0] * 40)

#         turtle.pendown()
#         for i in range(1, len(x_vals)):
#             turtle.goto(x_vals[i] * 40, y_vals[i] * 40)

        
#         turtle.hideturtle()
#         turtle.done()

#     def play_game(self):
#         self.input_equation()
#         print(f"Solving equation: {self.equation}")
#         self.draw_graph()



import turtle
import sympy as sp
import numpy as np

class EquationGraph:
    def __init__(self):
        self.equations = []

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
            equation_str = input(f"Enter equation {i + 1} (eg. y = x + 1): ")
            if '=' in equation_str:
                _, equation_str = equation_str.split('=')
            self.equations.append(sp.simplify(equation_str))

    def customize_graph(self):
        color = input("Enter the color for the graph (default is blue): ") or "blue"
        linestyle = input("Enter the linestyle for the graph (default is solid line): ") or "-"

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

        # # Ask the user if they want to save the graph
        # save_choice = input("Do you want to save the graph? (yes/no): ").lower()
        # if save_choice == "yes" or save_choice == "y":
        #     self.save_graph_as_image()
        # elif save_choice == "no" or save_choice == "n":
        #     print("Graph not saved.")
        # else:
        #     print("Invalid choice. Please enter 'yes' or 'no'.")
        #     return

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
        turtle.forward(600)

        for i in range(1, len(x_vals)):
            turtle.goto(x_vals[i] * 40, y_vals[i] * 40)

    def on_click(self, x, y):
        print(f"Clicked at ({x}, {y})")

    # def save_graph_as_image(self):
    #     save_path = input("Enter the path to save the graph image (include file extension, e.g., graph.png): ")
        
    #     try:
    #         turtle.hideturtle()
    #         cv = turtle.getcanvas()
    #         cv.postscript(file=save_path, colormode="color")
    #         turtle.done()

    #         print(f"Graph saved successfully at: {save_path}")
    #     except turtle.Terminator:
    #         print("Error: Unable to save the graph as an image.")


# # Example usage
# game = EquationGraph()
# game.input_equations()
# color, linestyle = game.customize_graph()
# game.draw_graph(color, linestyle)
# # game.save_graph_as_image()
