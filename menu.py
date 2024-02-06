# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Imports
from utility import Utility
from parseTree import parseTree
from sort import Sort
from graph import GraphUtility
from drawTree import DrawTree
from turtleGraph import EquationGraph

class Menu:

    # Intialise self to run the few programs when called
    def __init__(self):
        self.statement_storage = {}
        self.variable_values = {}
        self.printOutline()
        self.selection()
        self.sorted_statements = None

    # Print the outline 
    def printOutline(self):
        print('\n' + '*' * 65)
        print('* ST1507 DSAA: Evaluating & Sorting Assignment Statements' + '\t' + '*')
        print('*' + '-' * 63 + '*')
        print('*' + '\t'*8 + '*')
        print('*  - Done by: Teng Tze Hui (P2214209) & Ng Jace Xin (P2214593)'+ '\t' + '*')
        print('*  - Class DAAA/2B/01' + '\t' * 6 + '*')
        print('*' + '\t' * 8 + '*')
        print('*' * 65  + '\n' * 2)

    # Show the menu
    def showMenu(enter):
        print('\nPlease select your choice: (1,2,3,4,5,6,7,8)')
        print('\t 1. Add/Modify assignment statement')
        print('\t 2. Display current assignment statements')
        print('\t 3. Evaluate a single variable')
        print('\t 4. Read assignment statements from file')
        print('\t 5. Sort assignment statements')
        print('\t 6. Visualing assignment statements with graphs (Jace)')
        print('\t 7. Turtle Equation Drawing (Jace)')
        print('\t 8. Sorting Game (Tzehui)')
        print('\t 9. Graph Plotting Features (Tzehui)')
        print('\t 10. Exit')

    # Functions for each option the user choose
    def selection(self):
        while True:
            Utility.userInput()
            self.showMenu()

            # print the enter choice
            choice = Utility.enterChoice('Enter Choice: ')

            if choice == 1:
                self.option1()
            elif choice == 2:
                self.option2()
            elif choice == 3:
                self.option3()
            elif choice == 4:
                self.option4()
            elif choice == 5:
                self.option5()
            elif choice == 6:
                self.option6()
            elif choice == 7:
                self.option7()
            elif choice == 8:
                self.option8()
            elif choice == 9:
                self.option9()
            elif choice == 10:
                self.option10()
                return
            else:
                print("Invalid operation. Please try again and enter the correct choices.")

            print()
            
    # Option 1
    def option1(self):
        validated_input = Utility.validateVarName()
        # validated_input = Utility.getVarName()

        # If the validation is successful, update the class attributes
        if validated_input:
            var, exp = validated_input

            # Modifying existing assignment statement
            if var in self.statement_storage:
                self.statement_storage[var] = exp
            else:
                # Store the variables and expression in a dictionary
                self.statement_storage[var] = exp

    # Option 2
    def option2(self):
        # Sort the assignment statements alphabetically ## CHANGE THIS TO A CLASS??
        self.sorted_statements = sorted(self.statement_storage.items(), key=lambda x: x[0])

        while True:
            # Store the current variable values to check for changes later
            current_values = self.variable_values.copy()

            # Iterate through sorted statements
            for var, exp in self.sorted_statements:
                if var not in self.variable_values:
                    
                    tree = parseTree(exp, self.variable_values)
                    new_value = tree.result

                    if new_value is not None:
                        self.variable_values[var] = new_value
                
                # Check if the expression has changed
                elif exp != self.variable_values.get(var):
                    # Parse the modified expression using the current variable values
                    tree = parseTree(exp, self.variable_values)
                    
                    # Get the result of the modified expression
                    new_value = tree.result

                    # If the result is not None, update the variable value and expression
                    if new_value is not None:
                        self.variable_values[var] = new_value
                        # self.variable_values[var] = exp

            # Check for changes in variable values
            if current_values == self.variable_values:
                break
                    
        # Print the format
        print('\nCURRENT ASSIGNMENTS:')
        print('*' * 20)

        # Print the final sorted statements
        for var, exp in self.sorted_statements:
            evaluated_exp = self.variable_values.get(var, None)
            correct_exp = exp.replace(" ", "")
            if evaluated_exp is not None:
                print(f'{var} = {correct_exp} => {evaluated_exp}')
            else:
                print(f'{var} = {correct_exp} => None')

    # Option 3 -- evaluates all the variables 
    def option3(self):
        # Get the user input
        var = Utility.userInput('Please enter the variable you want to evaluate:\n')
        print('\nExpression Tree:')

        if var in self.statement_storage:
            exp = self.statement_storage[var]

            # build the parse tree for evaluation + parse tree
            parsedTree = parseTree(exp, self.variable_values)
            
            # Store the result in self.variable_values
            self.variable_values[var] = parsedTree.result

            # evaluate the statement  
            evaluated_exp = parsedTree.result

            # print the parse tree out 
            parsedTree.tree.printInorder(0)
            print(f'Value for variable \'{var}\' is {evaluated_exp}')       
        else:
            print(f'Variable \'{var}\' not found in statement storage.')

    # Option 4
    def option4(self):
        # Get and Read the file
        filePath = Utility.getFile('Please enter input file: ')
        readFile = Utility.readFile(filePath)

        # Process assignment statements
        Utility.processAssignmentStatements(readFile, self.statement_storage)

        # Sort the assignment statements alphabetically
        # sorted_statements = sorted(self.statement_storage.items(), key=lambda x: x[0])
        self.sorted_statements = sorted(self.statement_storage.items(), key=lambda x: x[0])

        while True:
            # Store the current variable values to check for changes later
            current_values = self.variable_values.copy()

            # Iterate through sorted statements
            for var, exp in self.sorted_statements:
                if var not in self.variable_values:
                    tree = parseTree(exp, self.variable_values)
                    new_value = tree.result

                    if new_value is not None:
                        self.variable_values[var] = new_value

                 # Check if the expression has changed
                elif exp != self.variable_values.get(var):
                    # Parse the modified expression using the current variable values
                    tree = parseTree(exp, self.variable_values)
                    
                    # Get the result of the modified expression
                    new_value = tree.result

                    # If the result is not None, update the variable value and expression
                    if new_value is not None:
                        self.variable_values[var] = new_value
                        # self.variable_values[var] = exp

            # Check for changes in variable values
            if current_values == self.variable_values:
                break

        # Print the format
        print('\nCURRENT ASSIGNMENTS:')
        print('*' * 20)

        # Print the final sorted statements
        for var, exp in self.sorted_statements:
            evaluated_exp = self.variable_values.get(var, None)
            correct_exp = exp.replace(" ", "")
            if evaluated_exp is not None:
                print(f'{var} = {correct_exp} => {evaluated_exp}')
            else:
                print(f'{var} = {correct_exp} => None')

    def option5(self):
        # Check if sorted_statements is available
        try:
            if self.sorted_statements is None:
                print("Sorted statements are not available. Please run option 4 first.")
                return
        except AttributeError:
                print("Sorted statements are not available. Please run option 4 first.")
                return

        # Pass self.variable_values to Utility.validateOutFile
        # outputFile = Utility.validateOutFile("Please enter output file", self.sorted_statements, self.variable_values)
        outputFile = Utility.getOutputFile("Please enter output file", self.sorted_statements, self.variable_values)
        print(f"Output file '{outputFile}' created successfully.")

    # Additional Features 1 (Jace)!
    # let users visualise the graph
    def option6(self):

        print("Hello there! \nThis tree is deisgned to help you understand the flow of dependencies between the variables you have input!\n")
        Utility.userInput()

        print("\nIf the graph is empty, it means that there are no relationships between the current variables stored..\n")
        Utility.userInput()

        if not self.statement_storage:
            print("\nOh no! It seems like your tree is empty, please select options 1 or 4 to input variables!")
            return
        
        tree = DrawTree(self.statement_storage)

        # print("statement storage",self.statement_storage) # check the statements 
        tree_data = tree.build_tree_data(self.statement_storage)
        tree.draw_tree(tree_data)

        user_choice = ""
        while user_choice not in ["yes", "no", "y", "n"]:
            user_choice = Utility.userInputNotEmpty('\nDo you want to display the dependency matrix information? (yes/no): ').lower()

            if user_choice == "yes" or user_choice == "y":
                print(self.statement_storage)
                tree.visualize_dependency_info()
            elif user_choice == 'no' or user_choice == 'n':
                return
            else:
                print('Please enter "yes" or "no"!')

    # Additional Features 2 (Jace)!
    def option7(self):

        equation_graph = EquationGraph()  # Create an instance of EquationGraph
        equation_graph.input_equations()  # Call the input_equations() method
        color, linestyle = equation_graph.customize_graph()
        print("Your graph will be printed shortly.. Click on the graph to get the axis points!")
        equation_graph.draw_graph(color, linestyle)


    # Additional Features 3 (Tzehui)! 
    def option8(self):
        # Introduction to the game
        print("\nWelcome to the Sorting Game!")
        print("This game is designed to help you understand various sorting algorithms and their performance. You can interactively observe how different algorithms work on a given set of data.\n")
        Utility.userInput()

        # Ask the user to choose an option
        print('\nChoose an option:\n1. Input your own data\n2. Generate random data\n')
        option = Utility.enterChoice('Enter a choice: ')

        if option == 1:
            # Get the data from the user
            data = Utility.userInputNotEmpty('\nEnter a list of elements (split by \',\'): ')
            elements = data.split(',')
            original_element = elements.copy()

        elif option == 2:
            # Generate random data based on user input (strings)
            size = Utility.enterChoice("\nEnter the size of the random data: ")
            str_length = Utility.enterChoice("Enter the length of each random string: ")
            elements = Utility.generateRandomData(size, str_length)
            original_element = elements.copy()

        else:
            print('It is not one of the valid options! Returning back to main menu...')
            return

        # Get the user input for the sorting algorithm
        print('\nChoose a sorting algorithm:\n1. Bubble Sort\n2. Merge Sort')
        choice = Utility.enterChoice('Enter a choice: ')

        # Create an instance of the Sort class
        sort = Sort()

        # Perform sorting based on the choice
        if choice == 1:
            sort.bubbleSort(elements)
        elif choice == 2:
            sort.mergeSort(elements)
        else:
            print('It is not one of the valid choices! Returning back to main menu...')
            return

        # Display the results
        print(f'\nOriginal List: {original_element}')
        print(f'Sorted List: {elements}')
        print(f'Number of steps: {sort.steps}')

    # Additional Features 4 (Tzehui)!
    def option9(self):
        print('\nWelcome to the Graph Features')
        print("This feature is to help you to explore graph features interactively. Visualize and analyze graphs with different layouts and algorithms.\n")
        Utility.userInput()

        # Get user input for the graph data (edge list format)
        edgelist = Utility.userInputNotEmpty('\nEnter the edge list (format: node1,node2,weight; e.g., A,B,2 B,C,1 A,C,3 D,A,4): ')

        # Convert input to a list of tuples (edge, weight)
        edges = [tuple(map(str.strip, edge.split(','))) for edge in edgelist.split() if edge]

        # Create a graph
        g = GraphUtility.createGraph(edges)

        if g is None:
            return  # Exit the option if creating the graph fails

        # Choose whether to find the shortest path
        findShortestPath = Utility.userInputNotEmpty('\nDo you want to find the shortest path? (yes/no): ').lower()

        if findShortestPath == 'yes' or findShortestPath == 'y':
            # Get user input for shortest path
            start_node = Utility.userInputNotEmpty('Enter the start node: ')
            end_node = Utility.userInputNotEmpty('Enter the end node: ')

            GraphUtility.findShortestDistance(g, start_node, end_node)
            
        elif findShortestPath == 'no' or findShortestPath == 'n':
            pass
        else:
            print('It is not one of the valid choices! Returning back to main menu...')

        # Choose whether to visualize the graph
        visualize_graph = Utility.userInputNotEmpty('\nDo you want to visualize the graph? (yes/no): ').lower()

        if visualize_graph == 'yes' or visualize_graph == 'y':
            # Choose plotting options
            print('\nChoose a graph layout:')
            print('1. Normal Graph')
            print('2. Minimum Spanning Tree')
            print('3. Google Page Ranking Algorithm')

            choice = Utility.enterChoice('Enter a choice: ')

            GraphUtility.visualizeGraph(g, edges, choice)

        elif visualize_graph == 'no' or visualize_graph == 'n':
            pass
        else:
            print('It is not one of the valid choices! Returning back to main menu...')


    # Option 10 (EXIT!!!)
    def option10(self):
        print('\nBye, thanks for using ST1507 DSAA: Evaluating & Sorting Assignment Statements')