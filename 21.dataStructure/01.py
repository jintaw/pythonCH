class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(seft):
        return seft.items == []
    
    def push(self , item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    
    def size(self):
        return len(self.items)
    


stack = Stack()
lists = [1,2,3,4,5]

for c , list in enumerate(lists):
    stack.push(list)

reverse = []
while stack.size():
    reverse.append(stack.pop())

print(reverse)
