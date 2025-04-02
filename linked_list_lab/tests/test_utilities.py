import unittest
from linked_list.linked_list import LinkedList
from linked_list.utilities import merge_sorted_lists

class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.ll1 = LinkedList()
        self.ll2 = LinkedList()

    def test_merge_sorted_lists(self):
        self.ll1.insert_at_end(1)
        self.ll1.insert_at_end(3)
        self.ll2.insert_at_end(2)
        self.ll2.insert_at_end(4)

        merged = merge_sorted_lists(self.ll1, self.ll2)
        current = merged.head

        result = []
        while current:
            result.append(current.get_data())
            current = current.get_next()

        self.assertEqual(result, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
