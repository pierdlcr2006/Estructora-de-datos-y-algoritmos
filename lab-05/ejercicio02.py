class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]  # Initialize the queue with the root node
    
    while queue:
        node = queue.pop(0)  # Dequeue the front node
        result.append(node.value)  # Process the current node
        
        if node.left:  # Enqueue left child if it exists
            queue.append(node.left)
        if node.right:  # Enqueue right child if it exists
            queue.append(node.right)
    
    return result

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(level_order_traversal(root)) # Perform level-order traversal
