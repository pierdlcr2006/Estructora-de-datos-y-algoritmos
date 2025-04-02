import unittest
from linked_list.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_insert_at_beginning(self):
        self.ll.insert_at_beginning(10)
        self.ll.insert_at_beginning(20)
        self.assertEqual(self.ll.head.get_data(), 20)

    def test_insert_at_end(self):
        self.ll.insert_at_end(30)
        self.ll.insert_at_end(40)
        self.assertEqual(self.ll.head.get_next().get_data(), 40)

    def test_list_length(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.ll.insert_at_end(3)
        self.assertEqual(self.ll.list_length(), 3)

if __name__ == '__main__':
    unittest.main()