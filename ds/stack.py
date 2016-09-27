class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

s = Stack()

print s.isEmpty()
s.push(4)
s.push('Car')
print s.peek()
print s.size()
print s.pop()
print s.pop()
print s.size()

