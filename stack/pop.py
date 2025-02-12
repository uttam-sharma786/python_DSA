def pop():
    self.items.pop()

# pop() method is used to remove and return the last item from the list
# python , the end of the list acts as the top of the stack
# the last item is removed from the top of the stack
# time complexity of the pop operation is O(1)
# because the pop() method has a constant time complexity

# it imporved by adding error handling

def pop(self):
    if self.is_empty():
        raise IndexError("stack is empty")
    return self.items.pop()

