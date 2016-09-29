import os, sys
sys.path.append(os.path.join(os.getcwd()))
from dequeue import Dequeue

def palchecker(aString):
    dequeue = Dequeue()

    for ch in aString:
        dequeue.addFront(ch)

    stillEqual = True
    
    while dequeue.size() > 1 and stillEqual:
        if dequeue.removeFront() != dequeue.removeRear():
            stillEqual = False

    return stillEqual
