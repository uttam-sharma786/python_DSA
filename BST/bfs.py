def breadth_first_search(root):
    if root is None:
        return  # You can print a message here if you want
    values = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        values.append(node.key)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return values