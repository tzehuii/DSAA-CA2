# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Imports
from utility import Utility
from parseTree import parseTree


class Menu:

    # Intialise self to run the few programs when called
    def __init__(self):
        self.statement_storage = {}
        self.variable_values = {}
        self.printOutline()
        self.selection()

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
        print('\t 6. Additional (Jace)')
        print('\t 7. Additional (Jace)')
        print('\t 8. Additional (Tzehui)')
        print('\t 9. Additional (Tzehui)')
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
        sorted_statements = sorted(self.statement_storage.items(), key=lambda x: x[0])

        while True:
            # Store the current variable values to check for changes later
            current_values = self.variable_values.copy()

            # Iterate through sorted statements
            for var, exp in sorted_statements:
                if var not in self.variable_values:
                    
                    tree = parseTree(exp, self.variable_values)
                    new_value = tree.result

                    if new_value is not None:
                        self.variable_values[var] = new_value

            # Check for changes in variable values
            if current_values == self.variable_values:
                break
        
        # Print the format
        print('\nCURRENT ASSIGNMENTS:')
        print('*' * 20)

        # Print the final sorted statements
        for var, exp in sorted_statements:
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
        if self.sorted_statements is None:
            print("Sorted statements are not available. Please run option 4 first.")
            return

        # Pass self.variable_values to Utility.validateOutFile
        outputFile = Utility.validateOutFile("Please enter output file", self.sorted_statements, self.variable_values)
        print(f"Output file '{outputFile}' created successfully.")

    # Option 10
    def option10(self):
        print('\nBye, thanks for using ST1507 DSAA: Evaluating & Sorting Assignment Statements')