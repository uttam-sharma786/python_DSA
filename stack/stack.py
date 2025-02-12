class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
    def clear(self):
        self.items = []
        
    def contain(self, item):
        return item in self.items
        
    def reverse(self):
        self.items.reverse()
        
    def print(self):
        print(self.items)
        
    def __str__(self):
        return str(self.items)

# Create a new stack
stack = Stack()

# Push some items
stack.push(1)
stack.push(2)
stack.push(3)

# Print the stack
print("Stack:", stack)  # Output: Stack: [1, 2, 3]

# Check size
print("Size:", stack.size())  # Output: Size: 3

# Peek at top element
print("Top element:", stack.peek())  # Output: Top element: 3

# Check if contains element
print("Contains 2:", stack.contain(2))  # Output: Contains 2: True
print("Contains 5:", stack.contain(5))  # Output: Contains 5: False

# Pop elements
print("Popped:", stack.pop())  # Output: Popped: 3
print("Stack after pop:", stack)  # Output: Stack: [1, 2]

# Reverse the stack
stack.reverse()
print("Reversed stack:", stack)  # Output: Reversed stack: [2, 1]

# Check if empty
print("Is empty:", stack.is_empty())  # Output: Is empty: False

# Clear the stack
stack.clear()
print("After clear:", stack)  # Output: After clear: []
print("Is empty:", stack.is_empty())  # Output: Is empty: True