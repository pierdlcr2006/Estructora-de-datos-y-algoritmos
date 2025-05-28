class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert a value into the BST"""
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)
    
    def build_from_list(self, values):
        """Build BST from a list of values"""
        for val in values:
            self.insert(val)
    
    def range_query(self, min_val, max_val):
        """🎯 Find all values in BST within given range"""
        result = []
        
        def inorder_range(node):
            if not node:
                return
            
            # Only traverse left subtree if current value > min_val
            if node.val > min_val:
                inorder_range(node.left)
            
            # Add current value if it lies within the range
            if min_val <= node.val <= max_val:
                result.append(node.val)
            
            # Only traverse right subtree if current value < max_val
            if node.val < max_val:
                inorder_range(node.right)
        
        inorder_range(self.root)
        return result
    
    def find_lca(self, val1, val2):
        """🧬 Find lowest common ancestor of two values in the BST"""
        current = self.root
        
        while current:
            # If both values are smaller than current → go left
            if val1 < current.val and val2 < current.val:
                current = current.left
            # If both values are larger than current → go right
            elif val1 > current.val and val2 > current.val:
                current = current.right
            # If they diverge or one equals current, current node is the LCA
            else:
                return current.val
        
        return None  # This shouldn't happen if both values exist in the BST

# 🧪 Test cases
def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print("🧪 Test 1:", bst1.range_query(5, 10) == [5, 7, 9])  # ✅
    
    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print("🧪 Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])  # 🌐
    
    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print("🧪 Test 3:", bst3.range_query(1, 5) == [])  # 📭
    
    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print("🧪 Test 4:", bst4.range_query(10, 20) == [15])  # 🌱
    
    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print("🧪 Test 5:", bst5.range_query(10, 20) == [10, 15, 20])  # 🔗

def test_find_lca():
    bst1 = BinarySearchTree()
    bst1.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 1:", bst1.find_lca(2, 8) == 6)  # 🌲 Root is LCA
    
    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 2:", bst2.find_lca(0, 4) == 2)  # 📚 Subtree LCA
    
    bst3 = BinarySearchTree()
    bst3.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 3:", bst3.find_lca(2, 3) == 2)  # 🔗 Ancestor node
    
    bst4 = BinarySearchTree()
    bst4.build_from_list([5, 3, 7])
    print("🧪 Test 4:", bst4.find_lca(5, 5) == 5)  # 🎯 Same node
    
    bst5 = BinarySearchTree()
    bst5.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 5:", bst5.find_lca(1, 3) == 2)  # 🌿 Leaf node LCA

# 🚀 Run all tests
print("=== Range Query Tests ===")
test_range_query()
print("\n=== LCA Tests ===")
test_find_lca()