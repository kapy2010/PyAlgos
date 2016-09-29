import os, sys
sys.path.append(os.path.join(os.getcwd()))
from stack import Stack

def postfixEval(postfixExpr):
    tokenList = postfixExpr.split()
    operandStack = Stack()

    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            secondOperand = operandStack.pop()
            firstOperand = operandStack.pop()
            result = doMath(token, firstOperand, secondOperand)
            operandStack.push(result)

    return operandStack.pop()


def doMath(op, firstOperand, secondOperand):
    if op == "**":
        return firstOperand ** secondOperand
    elif op == "*":
        return firstOperand * secondOperand
    elif op == "/":
        return firstOperand / secondOperand
    elif op == "+":
        return firstOperand + secondOperand
    elif op == "-":
        return firstOperand - secondOperand
