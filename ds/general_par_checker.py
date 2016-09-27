import os, sys
sys.path.append(os.path.join(os.getcwd()))
from stack import Stack

def parChecker(symbolString):
    """
    General balanced symbols checker

    Returns true if opening symbols balance closing symbols
    otherwise false
    symbols = (), [], {}
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '[{(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(openSymbol, closeSymbol):
    opens = "[{("
    closers = "]})"
    return opens.index(openSymbol) == closers.index(closeSymbol)





