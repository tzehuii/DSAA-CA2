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
        self.printOutline()
        # Utility.userInput()
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
        print('\t 6. Additional (individual)')
        print('\t 7. Additional (individual)')
        print('\t 8. Exit')

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
            elif choice ==8:
                self.option8()
                return
            else:
                print("Invalid operation. Please try again and enter the correct choices.")

            print()

    # Option 1
    def option1(self):
        statement = Utility.userInput('Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n')

        # spilt the var and experession
        var, exp = statement.split('=')  

        # Modifying existing assignment statement 
        if var in  self.statement_storage:
            self.statement_storage[var] = exp
        else:
            # Store the variables and expression in a dictionary 
            self.statement_storage[var] = exp

    # do we need to validate and ensure that the variable is 1 char?? for option 1

    # Option 2
    # def option2(self):
    #     print('CURRENT ASSIGNMENTS:')
    #     print('*'*20)

    #     for var, exp in self.statement_storage():
    #         evaluated_exp = parseTree.evaluate({var: exp})
    #         if exp is not None:
    #             print(f'{var}={exp}-->{evaluated_exp}\n')
    #         else:
    #             print(f'{var}={exp}-->None\n')

        



    # Option 3
    def option3(self):
        exp = '( 2 + ( 4 * 5 ) )'
        tree = parseTree.buildParseTree(exp)
        parser_instance = parseTree(tree)
        print(f'The expression: {exp} evaluates to: {parser_instance.evaluate(tree)}')

    # Option 8
    def option8(self):
        print('\nBye, thanks for using ST1507 DSAA: Evaluating & Sorting Assignment Statements')