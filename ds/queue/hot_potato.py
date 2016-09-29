import os, sys
sys.path.append(os.path.join(os.getcwd()))
from queue import Queue

def hotPotato(namelist, num):
    queue = Queue()
    
    for name in namelist:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
    
