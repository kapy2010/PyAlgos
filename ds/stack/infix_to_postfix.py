import os, sys
sys.path.append(os.path.join(os.getcwd()))
from stack import Stack

def infixToPostfix(infixexpr):
    """
    Converts given infix expression to postfix expression
    """
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    postFixList = []
    
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in ALPHABETS or token.isdigit():
            postFixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while opStack.peek() != '(':
                postFixList.append(opStack.pop())
            opStack.pop()
        else:
            while not opStack.isEmpty() and (prec[token] <= prec[opStack.peek()]):
                postFixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postFixList.append(opStack.pop())

    return " ".join(postFixList)


            
        
    
