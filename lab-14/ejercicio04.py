test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []  # Initialize the heap as an empty list

    def delete_min(self):
        if not self.heap:
            return None  # Return None if the heap is empty

        # 1.4.2: Single element deletion
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element exists, remove and return it

        # Replace root with last element
        min_elem = self.heap[0]  # Store the current minimum element (the root)
        self.heap[0] = self.heap.pop()  # Replace root with the last element and remove the last
        self._heapify_down(0)  # Restore the heap property by percolating down from the root
        return min_elem  # Return the removed minimum element

    def _heapify_down(self, index):
        while self._has_left_child(index):  # While the current node has a left child
            smaller_child_index = self._left_child_index(index)  # Assume left child is the smaller one
            
            # If there is a right child and it's smaller than the left child, update the index
            if self._has_right_child(index) and self.heap[self._right_child_index(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self._right_child_index(index)
            
            # If current node is smaller than or equal to the smallest child, the heap property is valid
            if self.heap[index] <= self.heap[smaller_child_index]:
                break
            else:
                # Swap current node with the smaller child and continue
                self.heap[index], self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]
                index = smaller_child_index  # Move down to the child's index

    def _left_child_index(self, index):
        return 2 * index + 1  # Calculate index of the left child

    def _right_child_index(self, index):
        return 2 * index + 2  # Calculate index of the right child

    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)  # Check if left child exists

    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)  # Check if right child exists

    def size(self):
        return len(self.heap)  # Return the number of elements in the heap

def test_1_4():
    heap = MinHeap()
    
    # 1.4.1 Empty heap deletion
    result = heap.delete_min()
    record_test("1.4.1 Empty heap deletion", result is None)
    
    # 1.4.2 Single element deletion
    heap.heap = [5]
    result = heap.delete_min()
    record_test("1.4.2 Single element deletion", result == 5 and heap.size() == 0)
    
    # 1.4.3 Multiple deletions
    heap.heap = [1, 3, 2, 7, 4]
    first = heap.delete_min()
    second = heap.delete_min()
    record_test("1.4.3 Multiple deletions", first == 1 and second == 2)
    
    # 1.4.4 Heap property maintenance
    heap.heap = [1, 3, 2, 7, 4, 5]
    heap.delete_min()
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        and heap.heap[i] <= heap.heap[2*i+2] if 2*i+2 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.4.4 Heap property maintenance", valid_heap)
    
    # 1.4.5 Size tracking
    initial_size = heap.size()
    heap.delete_min()
    record_test("1.4.5 Size tracking", heap.size() == initial_size - 1)

# 🚀 Run tests
test_1_4()

# 📋 Summary
for r in test_results:
    print(r)