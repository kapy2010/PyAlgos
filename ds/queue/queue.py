class Queue():
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def size(self):
        return len(self.items)

    def dequeue(self):
        return self.items.pop()


