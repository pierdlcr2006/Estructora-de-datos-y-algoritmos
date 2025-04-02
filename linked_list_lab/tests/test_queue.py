import unittest
from queue.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_enqueue(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.assertEqual(self.q.size(), 2)

    def test_dequeue(self):
        self.q.enqueue(30)
        self.q.enqueue(40)
        self.q.dequeue()
        self.assertEqual(self.q.peek(), 40)

    def test_is_empty(self):
        self.assertTrue(self.q.is_empty())
        self.q.enqueue(50)
        self.assertFalse(self.q.is_empty())

if __name__ == '__main__':
    unittest.main()
