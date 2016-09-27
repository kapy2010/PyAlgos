import os, sys
sys.path.append(os.path.join(os.getcwd()))
from stack import Stack

def baseConverter(decNumber, base):
    """
    Converts a decimal number to the given base
    """
    DIGITS = "0123456789ABCDEF"
    
    remStack = Stack()

    while decNumber > 0:
        remStack.push(decNumber % base)
        decNumber = decNumber // base

    newString = ""
    while not remStack.isEmpty():
        newString += DIGITS[remStack.pop()]

    return newString

