class Node:
    # Create a Node with prev and next , data pointer
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next


# create a linkeList 
class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
# Insert at start in doubly list
    def insert_at_start(self,data):
        new_node = Node(data) # create new node instance
    # case1 (Empty list case)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

    # case2 
        else:
            new_node.next = self.head   #Connect new node to existing head
            self.head.prev = new_node     # connect existing head back to new node 
            self.head = new_node      # update head reference
        
if __name__ == "__main__":
    dll = doublyLinkedList()
    dll.insert_at_start(10)
    dll.insert_at_start(20)
    dll.insert_at_start(30)
    dll.insert_at_start(40)
    
    # verify connection
    print(dll.head.data)
    print(dll.tail.data)
    


        