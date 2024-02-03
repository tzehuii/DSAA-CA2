# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Imports
import string 
from tokenization import Tokenization

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

# -------------------------------------Validate--------------------------------------
        
    # # for option 1 !!
    # def validateVarName():
    #     while True: 
    #         try: 
    #             # Ask for the user input 
    #             statement = Utility.userInput('Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n')

    #             # spilt the var and experession
    #             var, exp = statement.split('=', 1)  

    #             # Remove spaces from var and exp and check each character
    #             var = var.strip()
    #             cleaned_exp = exp.replace(" ", "")

    #             if len(var) == 1:
                    
    #                 # Check for incomplete statements
    #                 if exp.endswith(('+','-','*','/')):
    #                     print('Invalid incomplete statement. Please enter a complete assignment.')
    #                     Utility.validateVarName()

    #                 elif len(exp) == 0:
    #                     print('Invalid incomplete statement. Please enter a complete assignment.')
    #                     Utility.validateVarName()

    #                 # Check for valid brackets
    #                 elif not Utility.checkBrackets(exp):
    #                     print("Invalid bracket usage. Please check your brackets.")
    #                     Utility.validateVarName()

    #                 # return var, exp 

    #                 # Ensure that the expression contains at least one pair of brackets
    #                 elif '(' not in exp or ')' not in exp:
    #                     print("Invalid expression. Please include at least one pair of brackets.")
    #                     Utility.validateVarName()

    #                 return var, exp 
                
    #             else: 
    #                 Utility.userInput('Please key in a statement with 1 variable at the start (eg. a=(1+2))')

    #         except ValueError:
    #             print('Invalid input. Please enter a valid statement.')


    def validateVarName(): # edited
        while True: 
            try: 
                # Ask for the user input 
                statement = Utility.userInput('Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n')

                # spilt the var and experession
                var, exp = statement.split('=', 1)  

                # Remove spaces from var and exp and check each character
                var = var.strip()
                cleaned_exp = exp.replace(" ", "")

                if var.isalpha() and len(var) >= 1:  # Check if var contains only alphabets and has more than or equal to one letter
                    
                    # Check for incomplete statements without any of the following operators
                    if not any(op in exp for op in ['+', '-', '*', '/', '**']):
                        print('Invalid statement. Please include at least one of the operators: +, -, *, /, **')
                        Utility.validateVarName()

                    # Check for incomplete statements
                    if exp.endswith(('+','-','*','/','**')):
                        print('Invalid incomplete statement. Please enter a complete assignment.')
                        Utility.validateVarName()

                    elif len(exp) == 0:
                        print('Invalid incomplete statement. Please enter a complete assignment.')
                        Utility.validateVarName()

                    # Check for valid brackets
                    elif not Utility.checkBrackets(exp):
                        print("Invalid bracket usage. Please check your brackets.")
                        Utility.validateVarName()

                    # Ensure that the expression contains at least one pair of brackets
                    elif '(' not in exp or ')' not in exp:
                        print("Invalid expression. Please include at least one pair of brackets.")
                        Utility.validateVarName()

                    return var, exp 
                
                else: 
                    Utility.userInput('Please key in a statement with 1 variable at the start (eg. a=(1+2))')

            except ValueError:
                print('Invalid input. Please enter a valid statement.')



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


