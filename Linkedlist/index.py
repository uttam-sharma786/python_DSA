class Node:
    # Create a node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self, data):
        # Case 1: Take data and convert into node
        new_node = Node(data)
        
        # Case 2: Check if list is empty
        if self.head is None:
            self.head = new_node
        # Case 3: Add node at start by adjusting links
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_end(self, data):
        # Case 1: Take data and convert into node
        new_node = Node(data)
        
        # Case 2: Check if list is empty
        if self.head is None:
            self.head = new_node
            return
        
    def insert_at_possition(self, prevNode, data):
        if prevNode is None:
            print("Previous node not be null")
            return
        
        # create a new node with the prevised data
        new_node = Node(data, prev_node.next)
        
        # Update the next reference of the previous node to point to the new node
        
        prev_node.next = new_node


        
        # Case 3: Traverse to last node
        current = self.head
        while current.next:
            current = current.next
        
        # Case 4: Add node at end
        current.next = new_node
    
    def display(self):
        # Add display method to verify the list
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

# Example usage
if __name__ == "__main__":
    # Create a new linked list
    linked_list = LinkedList()
    
    # Insert at start
    linked_list.insert_at_start(10)  # List: 10
    linked_list.insert_at_start(20)  # List: 20 -> 10
    
    # Insert at end
    linked_list.insert_at_end(30)    # List: 20 -> 10 -> 30
    
    # Display the list
    linked_list.display()