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
    # delete the first node
    def delete_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    #delete the last node 
    def delete_last_node(self):
        if not self.head:
            return  # nothing to delete if list is empty

        if not self.head.next:
            self.head = None  # if there is only one node
            return

        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
            
    # linked list delete a node with given (value)
    def deleteByKey(self, key):
        if not self.head:
            print("List is empty")
            return
        
        # Check if the head node is the one to be deleted
        if self.head.data == key:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
        
        print("No node found with key:", key)
    
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    
    def traverse(self):
        current = self.head
        traverse_list = []  # Renamed to avoid confusion with the method name
        while current:
            traverse_list.append(current.data)  # Convert data to string for joining
            current = current.next  # Move to the next node
        print(" -> ".join(traverse_list))  # Corrected join syntax

    
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
    
    linked_list.insert_at_start(1)
    

    # print("Before deleting the last node:")
    # linked_list.print_list()

    # linked_list.delete_last_node()

    # print("After deleting the last node:")
    # linked_list.print_list()
    
# // delete last node (second last node)

# LinkedList.prototype.delete_last_node = function(){
#     if(!this.head )
#     return    // nothing to delete if list is empty
# }
# if(this.head.next){
#     this.head = null // if there is only one node
#     return 
# }
#  while(secondlast.next.next){
#      secondlast = secondlast.next
#  }
#   let secondlast = head
#   secondlast.next = null
  
  
# linkedList.prototype.delete.ByKey = function(key){
#     if(!this.head){
#         console.log("list is empty")
#         return
#     }
#     if(this.head.data === key){
#         this.head = this.head.next
#         return 
#     }
#     let current = this.head
#     while(current.next == null){
#         if(current.next.data === key)
#         current.next = current.next.next
#         return 
#     }
#     current = current.next
# }
# console.log("No node found with key:",key)


# // search operation

# LinkedList.prototype.search = function(key){
#     let current = this.head
#     # current.data === key
#     while(current){
#         if(current.data === key){
#             return true 
#         }
#         return False
#     }
# }


# // traverse
# LinkedList.prototype.printlist = function(){
#     let current = this.head
#     let listValuse =[]
#       while(current){
#           listValuse.push(current.data) // add data to list
#           current = current.next // move to next node
#       }
# # }