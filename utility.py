# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Imports

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
        # Ask for the user input 
        statement = Utility.userInput('Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n')

        # spilt the var and experession
        var, exp = statement.split('=')  

        if len(var) == 1:
            return var, exp
        else: 
            Utility.userInput('Please key in a statement with 1 variable at the start (eg. a=(1+2))')