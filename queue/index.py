class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None  # Or raise an exception: raise Exception("Cannot dequeue from an empty queue")
        return self.items.pop(0)

    def is_empty(self):
        return not bool(self.items)

    def peek(self):
        if self.is_empty():
            return None  # Or raise an exception
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def contain(self, item):
        return item in self.items

    def reverse(self):
        self.items.reverse()

    def print(self):  # Consider removing this; __str__ is better
        print(self.items)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.items == other.items
        return False

    def __bool__(self):
        return not self.is_empty()
# Create a queue
my_queue = Queue()

# Enqueue some items
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Print the queue
print(my_queue)  # Output: [10, 20, 30]

# Dequeue an item
dequeued_item = my_queue.dequeue()
print(f"Dequeued: {dequeued_item}")  # Output: Dequeued: 10

# Peek at the front item
print(f"Front item: {my_queue.peek()}")  # Output: Front item: 20

# Check if the queue is empty
print(f"Is empty: {my_queue.is_empty()}")  # Output: Is empty: False

# Get the size of the queue
print(f"Size: {my_queue.size()}")  # Output: Size: 2

#Check if queue contains value
print(f"Contain 20: {my_queue.contain(20)}") #Output: Contain 20: True

#Reverse queue
my_queue.reverse()
print(my_queue) #Output: [30, 20]

#Clear queue
my_queue.clear()
print(my_queue) #Output: []
print(f"Is empty: {my_queue.is_empty()}")  # Output: Is empty: True
