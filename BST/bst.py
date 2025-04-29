class BST_Node:
    def __init__(self, key):  # Fixed: Added key parameter
        self.key = key        # Fixed: Uses parameter instead of undefined 'Key'
        self.left = None
        self.right = None

class BST:                    # Fixed: Made proper class (was function before)
    def __init__(self):
        self.root = None      # Fixed: Proper initialization

# Create tree
my_tree = BST()

# Create nodes
my_tree.root = BST_Node(10)
my_tree.root.left = BST_Node(5)
my_tree.root.right = BST_Node(15)

print(my_tree)
