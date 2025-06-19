test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        # Initialize empty heap storage
        self.heap = []

    def is_empty(self):
        # Return True if heap has no elements
        return len(self.heap) == 0

    def size(self):
        # Return number of elements in heap
        return len(self.heap)

    def peek(self):
        # Return minimum element without removing it
        if self.is_empty():
            return None
        return min(self.heap)  # For simplicity, use min since we're not maintaining heap properties yet

def test_1_1():
    # 1.1.1 Empty heap initialization
    heap = MinHeap()
    record_test("1.1.1 Empty heap initialization", heap.is_empty() == True)
    
    # 1.1.2 Size tracking
    heap.heap = [1, 3, 2]  # Simulate adding elements
    record_test("1.1.2 Size tracking", heap.size() == 3)
    
    # 1.1.3 Peek functionality
    record_test("1.1.3 Peek functionality", heap.peek() == 1)
    
    # 1.1.4 Empty heap edge case
    empty_heap = MinHeap()
    record_test("1.1.4 Empty heap edge case", empty_heap.peek() is None)
    
    # 1.1.5 Type validation
    record_test("1.1.5 Type validation", isinstance(heap.is_empty(), bool))

# 🚀 Run tests
test_1_1()

# 📋 Summary
for r in test_results:
    print(r)