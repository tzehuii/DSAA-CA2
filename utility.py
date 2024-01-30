# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Imports
import string 

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
    def validateVarName():
        while True: 
            try: 
                # Ask for the user input 
                statement = Utility.userInput('Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n')

                # spilt the var and experession
                var, exp = statement.split('=', 1)  

                # Remove spaces from var and exp and check each character
                var = var.strip()
                cleaned_exp = exp.replace(" ", "")

                if len(var) == 1:
                    
                    # Check for incomplete statements
                    # if cleaned_exp.strip().endswith(('+','-','*','/','')):
                    #     print('Invalid incomplete statement. Please enter a complete assignment.')
                    #     Utility.validateVarName()

                    for char in cleaned_exp:
                        # if not number or have operators (ask them to retype the statement)
                        if not char.isdigit() and char not in ['(','+','-','/','*',')']: 
                            print(f"At least one character in {exp} is not numeric or not an operator")
                            Utility.validateVarName()

                        # if not in letters or have operators (ask them to retype the statement)
                        elif not char.isalpha() and char not in ['(','+','-','/','*',')'] and not char.isdigit():
                            print(f'{char} is not defined!')
                            Utility.validateVarName()
                    return var, exp 
                
                else: 
                    Utility.userInput('Please key in a statement with 1 variable at the start (eg. a=(1+2))')
            except ValueError:
                print('Invalid input. Please enter a valid statement.')