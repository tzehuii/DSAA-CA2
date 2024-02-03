# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Imports
import string 
import os

class Utility:
 
# -------------------------------------Inputs--------------------------------------

    # Get the user input for intgers
    def enterChoice(prompt):
        while True:
            try:
                choice = int(Utility.userInput(prompt))
                return choice 
            
            # only hapens when ans given is not an integer
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
    
    # Get the user input if not it just waits for the users reply 
    def userInput(prompt = None):
        if prompt == None:
            enter = input('Press enter key, to continue...')
            return enter
        else:
            return input(prompt)
        
# -------------------------------------Getters--------------------------------------

    # Get and ensure that file path is valid and not empty
    def getFile(filePathPrompt):
        while True:
            filePath = Utility.userInput(filePathPrompt)

            if Utility.__validateFilePath(filePath):
                return filePath
            else:
                print('Invalid input. Please enter a valid file path.')
        
# -------------------------Commonly used (basic) functioms--------------------------

    # Read the content of the file
    def readFile(filePath): 
        with open(filePath, 'r') as file:
            return file.read()

    # Write the output to a new file
    def writeFile(filePath, content):
        with open(filePath, 'w') as file:
            return file.write(content)        
    
    # Ensure that the output file path is in the folder
    def outputFilePathinFolder(folderName, fileName):
        return os.path.join(folderName, fileName)
    
    def processAssignmentStatements(content, statement_storage):
        # Split the content into lines
        lines = content.split('\n')

        # Process each line (assignment statement)
        for line in lines:
            # Remove leading and trailing whitespaces
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Update the dictionary to store the assignment statements
            var, exp = line.split('=')
            statement_storage[var] = exp

# -------------------------------------Validate--------------------------------------
    
    def validateVarName(): # edited
        while True: 
            try: 
                # Ask for the user input 
                statement = Utility.userInput('Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n')

                # spilt the var and experession
                var, exp = statement.split('=', 1)  

                # Remove spaces from var and exp and check each character
                var = var.strip()
                exp = exp.strip()
                # cleaned_exp = exp.replace(" ", "")

                if var.isalpha() and len(var) >= 1:  # Check if var contains only alphabets and has more than or equal to one letter
                                        # Check if exp is not empty
                    if exp:
                    
                        # Check for incomplete statements without any of the following operators
                        if not any(op in exp for op in ['+', '-', '*', '/', '**']):
                            print('Invalid statement. Please include at least one of the operators: +, -, *, /, **')
                            continue

                        # Check for incomplete statements
                        if exp.endswith(('+','-','*','/','**')):
                            print('Invalid incomplete statement. Please enter a complete assignment.')
                            continue

                        # shld be not needed
                        # elif len(exp) == 0:
                        #     print('Invalid incomplete statement. Please enter a complete assignment.')
                        #     continue

                        # Check for valid brackets
                        elif not Utility.checkBrackets(exp):
                            print("Invalid bracket usage. Please check your brackets.")
                            continue

                        # Ensure that the expression contains at least one pair of brackets
                        elif '(' not in exp or ')' not in exp:
                            print("Invalid expression. Please include at least one pair of brackets.")
                            continue

                        return var, exp 
                
                    else:
                        print('Invalid incomplete statement. Please enter a complete assignment.')
                else:
                    print('Please key in a statement with 1 variable at the start (e.g., a=(1+2))')
                    
            except ValueError:
                print('Invalid input. Please enter a valid statement.')

    # validate the input
    def validateVariable(prompt):
        while True:
            try:
                # Ask for the user input
                var = Utility.userInput(prompt)

                if var == None:
                    print('Please key in a varaible to use this option')
                    Utility.validateVariable()
                elif var.isnumeric:
                    print('Please key in letter/letters to use this option')
                    Utility.validateVariable()
                elif len(var) == 1:
                    return var
                            
            except ValueError:
                print('Invalid input. Please enter a valid statement.')

    # Validate the file path 
    def __validateFilePath(filePath):
        try:
            with open(filePath, 'r'):
                pass  # Just open and immediately close the file to check if it exists
            return True
        except FileNotFoundError:
            return False
        except OSError:
            return False 

    # Check the brackets 
    def checkBrackets(expression):
        stack = []
        left_bracket = '('
        right_bracket = ')'   

        for char in expression:
            if char == left_bracket:
                stack.append(char)
            elif char == right_bracket:
                if not stack or stack.pop() != left_bracket:
                    return False

        return not stack  # Stack should be empty if brackets are balanced
    


