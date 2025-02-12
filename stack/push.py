# Adding value
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
            
stack = Stack()

print(stack.push(1))
stack.push(2)
stack.push(3)
    
# append() method is used to add item to the end of the list
# in python , the end of the list acts as the top of the stack
# so the new item is added to the top of the stack
# the time complexity of the push operation is O(1)
# because the append() method has a constant time complexity



