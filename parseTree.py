# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Imports
from stack import Stack
from binaryTree import BinaryTree
from tokenization import Tokenization
import string

class parseTree():
    def __init__(self, exp, var_storage_statement=None):
        self.exp = exp 
        self.tree = self.buildParseTree(exp)
        self.result = self.evaluate(self.tree, var_storage_statement)

    # This tokenisation only look at the spaces in between
    def buildParseTree(self, exp):
        # take out the tokensiation 
        tokens = Tokenization.tokenize(exp) # look at the spaces 
        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree)
        
        currentTree = tree 
        
        for t in tokens: 
            # RULE 1: If token is '(' add a new node as left child 
            # and descend into that node
            if t == '(':
                currentTree.insertLeft('?') 
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree() 

            # RULE 2: If token is operator set key of current node 
            # to that operator and add a new node as right child 
            # and descend into that node
            elif t in ['+', '-', '*', '/','**']:
                currentTree.setKey(t)
                currentTree.insertRight('?') 
                stack.push(currentTree)
                currentTree = currentTree.getRightTree() 


            # # RULE 3: If token is variable / float, set key of the current node 
            # elif t not in ['+', '-', '*', '/', ')','**']:
            #     if t.isalpha():
            #         currentTree.setKey(t)
            #     else:
            #         currentTree.setKey(float(t))
                
            # # RULE 4: If token is number, set key of the current node 
            # # to that number and return to parent
            # elif t not in ['+', '-', '*', '/', ')'] : 
            #     currentTree.setKey(int(t)) 
            #     parent = stack.pop()
            #     currentTree = parent
                

            # work with the other variables in the statement (if any)
            elif t.isalpha():
                currentTree.setKey(str(t))
                parent = stack.pop()
                currentTree = parent
                
            # RULE 3: If token is number, set key of the current node # change this so that it accepts a variable as an input oso !!
            # to that number and return to parent
            elif t not in ['+', '-', '*', '/', '**',')'] : 
                try:
                    currentTree.setKey(int(t))  # Try to convert to integer
                except ValueError:
                    currentTree.setKey(float(t))  # If conversion fails, use float
                parent = stack.pop()
                currentTree = parent
                
                
            # RULE 5: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree
    

   # Recursively evaluate the parse tree 
    def evaluate(self, tree, var_storage_statement):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        
        # evaluate base on the pemdas rule
        if leftTree is not None and rightTree is not None: 

            leftValue = self.evaluate(leftTree, var_storage_statement)
            rightValue = self.evaluate(rightTree, var_storage_statement)

            # Check if either operand is a string (alphabet)
            if isinstance(leftValue, str) or isinstance(rightValue, str):
                # If so, return None
                return None
            
            # Replace variable names with their values
            if isinstance(leftValue, str) and leftValue in var_storage_statement:
                # print("HERE1")
                leftValue = var_storage_statement[leftValue]

            if isinstance(rightValue, str) and rightValue in var_storage_statement:
                # print("HERE2")
                rightValue = var_storage_statement[rightValue]
            
            if op == '+':
                try:
                    return leftValue + rightValue
                except TypeError:
                    pass
            elif op == '-':
                try:
                    return leftValue - rightValue
                except TypeError:
                    pass
            elif op == '*':
                try:
                    return leftValue * rightValue
                except TypeError:
                    pass
            elif op == '/':
                try:
                    return leftValue / rightValue
                except ZeroDivisionError:
                    pass
                except TypeError:
                    pass
            elif op == '**':
                return leftValue ** rightValue
        
        else:
            # If the current node is a variable, return its value from the dictionary
            if tree.getKey() in var_storage_statement:
                return var_storage_statement[tree.getKey()]
            else:
                return tree.getKey()
    
        
# # reference for pemdas

#     def pemdas(self):
#         return self._pemdas_recursive(self.tree)

#     def _pemdas_recursive(self, tree):
#         if tree is not None:

#             # isinstance(object, type) 
#             if isinstance(tree.getKey(), float):
#                 return tree.getKey()

#             operator = tree.getKey()

#             # Evaluate left and right subtrees based on PEMDAS rules
#             if operator == '**':
#                 left_value = self._pemdas_recursive(tree.getLeftTree())
#                 right_value = self._pemdas_recursive(tree.getRightTree())
#                 return left_value ** right_value
#             elif operator in ['*', '/']:
#                 left_value = self._pemdas_recursive(tree.getLeftTree())
#                 right_value = self._pemdas_recursive(tree.getRightTree())
#                 if operator == '*':
#                     return left_value * right_value
#                 elif operator == '/':
#                     return left_value / right_value
#             elif operator in ['+', '-']:
#                 left_value = self._pemdas_recursive(tree.getLeftTree())
#                 right_value = self._pemdas_recursive(tree.getRightTree())
#                 if operator == '+':
#                     return left_value + right_value
#                 elif operator == '-':
#                     return left_value - right_value

#             # If it's a variable or a number, return its value
#             return self._get_variable_value(operator, left_value, right_value)
    