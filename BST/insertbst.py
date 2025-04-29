class BST_Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = BST_Node(key)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, node, new_node): # node -> root 
        if new_node.key < node.key:
            if node.left is None:
                node.left = new_node
            else:
                self._insert_node(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert_node(node.right, new_node)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)
bst = BST()
print(bst.insert(10))
print(bst.insert(5))
print(bst.insert(15))
print(bst.insert(3))
print(bst.insert(7))


bst.inorder(bst.root)