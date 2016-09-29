import os, sys
sys.path.append(os.path.join(os.getcwd()))
from stack import Stack

def postfixEval(postfixExpr):
    DIGITS = "0123456789"
    tokenList = postfixExpr.split()
    operandStack = Stack()

    for token in tokenList:
        if token in DIGITS:
            operandStack.push(int(token))
        else:
            secondOperand = operandStack.pop()
            firstOperand = operandStack.pop()
            operandStack.push(doMath(token, firstOperand, secondOperand))

    return operandStack.pop()


def doMath(op, firstOperand, secondOperand):
    if op == "*":
        return firstOperand * secondOperand
    elif op == "/":
        return firstOperand / secondOperand
    elif op == "+":
        return firstOperand + secondOperand
    elif op == "-":
        return firstOperand - secondOperand
