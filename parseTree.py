# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Imports
from stack import Stack
from binaryTree import BinaryTree
from tokenization import Tokenization

class parseTree:
    def __init__(self, tree):
        self.evaluate(tree)


    # This tokenisation only look at the spaces in between
    def buildParseTree(exp):
        # take out the tokensiation 
        tokens = exp.split() # look at the spaces 
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
            elif t in ['+', '-', '*', '/']:
                currentTree.setKey(t)
                currentTree.insertRight('?') 
                stack.push(currentTree)
                currentTree = currentTree.getRightTree() 
                
            # RULE 3: If token is number, set key of the current node 
            # to that number and return to parent
            elif t not in ['+', '-', '*', '/', ')'] : 
                currentTree.setKey(int(t)) #integer (cause it to not work with float)
                parent = stack.pop()
                currentTree = parent
                
            # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree
    
    # !!! need to settle 
    def evaluate(self, tree):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        
        if leftTree != None and rightTree != None: 
            if op == '+':
                return self.evaluate(leftTree) + self.evaluate(rightTree)
            elif op == '-':
                return self.evaluate(leftTree) - self.evaluate(rightTree)
            elif op == '*':
                return self.evaluate(leftTree) * self.evaluate(rightTree)
            elif op == '/':
                return self.evaluate(leftTree) / self.evaluate(rightTree)
        else:
            return tree.getKey()
        
        # divide by 0 will make it crash so need to take care of it to ensure it doesnt crash (in assignment)
    