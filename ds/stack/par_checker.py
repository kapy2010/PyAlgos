import os, sys
sys.path.append(os.path.join(os.getcwd()))
from stack import Stack

def parChecker(symbolString):
    """
    Simple balanced symbol checker

    Returns true if opening parenthesis balance closing parenthesis
    otherwise false
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False




