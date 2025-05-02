class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node, key):
        if node is None:
            return node

        # Traverse left/right subtree
        if key < node.key:
            node.left = self._delete_node(node.left, key)
        elif key > node.key:
            node.right = self._delete_node(node.right, key)
        else:
            # Node found - handle deletion cases
            if node.left is None and node.right is None:  # No children
                return None
            elif node.left is None:  # Only right child
                return node.right
            elif node.right is None:  # Only left child
                return node.left
            else:  # Two children
                temp = self._find_min_node(node.right)
                node.key = temp.key
                node.right = self._delete_node(node.right, temp.key)
        
        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current




# Node Class: Represents tree nodes with key, left, and right attributes

# Three Deletion Cases:

# Leaf Node: Simply remove by returning None

# Single Child: Replace node with its only child

# Two Children:

# Find minimum node in right subtree

# Copy its value to current node

# Delete the minimum node from right subtree

# Recursive Implementation: Cleanly handles subtree modifications

# Helper Methods: _find_min_node locates the inorder successor