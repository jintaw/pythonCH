class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self , item):
        self.items.insert(0 , item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

a_queue = Queue()

print(a_queue.is_empty())

for i in range(50):
    a_queue.enqueue(i)

while a_queue.size():
    print(a_queue.dequeue())

print()

print(a_queue.size())
