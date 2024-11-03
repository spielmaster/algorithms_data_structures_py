import unittest
from src import heaps

class TestMinHeap(unittest.TestCase):

    items = [2, 4, 8, 9, 7]
    min_heap = heaps.MinHeap(items)

    def test_get_indices(self):

        self.assertEqual(self.min_heap.get_left_child_index(0), 1)
        self.assertEqual(self.min_heap.get_right_child_index(0), 2)

        self.assertEqual(self.min_heap.get_parent_index(1), 0)
        self.assertEqual(self.min_heap.get_parent_index(2), 0)

    def test_has(self):

        self.assertEqual(self.min_heap.has_left_child(0), True)
        self.assertEqual(self.min_heap.has_right_child(0), True)


        self.assertEqual(self.min_heap.has_left_child(4), False)
        self.assertEqual(self.min_heap.has_right_child(4), False)

        self.assertEqual(self.min_heap.has_parent(4), True)
        self.assertEqual(self.min_heap.has_parent(0), False)

    def test_get_items(self):

        self.assertEqual(self.min_heap.get_left_child_item(0), 4)
        self.assertEqual(self.min_heap.get_right_child_item(0), 8)
        
        self.assertEqual(self.min_heap.get_parent_item(1), 2)
        self.assertEqual(self.min_heap.get_parent_item(2), 2)

        self.assertEqual(self.min_heap.get_parent_item(0), None)
        self.assertEqual(self.min_heap.get_left_child_item(4), None)
        self.assertEqual(self.min_heap.get_right_child_item(4), None)
        
        self.assertEqual(self.min_heap.peek(), 2)
        


    def test_modify_heap(self):

        self.min_heap.add(1)
        self.assertListEqual(self.min_heap.items, [1, 4, 2, 9, 7, 8])

        self.assertEqual(self.min_heap.poll(), 1)
        self.assertListEqual(self.min_heap.items, [2, 4, 8, 9, 7] )
