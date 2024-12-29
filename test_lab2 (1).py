import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

    def test_2_pq_insertfull(self):
        print("\n")
        pq = pqueue.pqueue(3)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        with self.assertRaises(IndexError):
            pq.insert(4)

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

    def test_2_pq_peek_empty_queue(self):
        print("print the maximum value of an empty queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        with self.assertRaises(IndexError):
            pq.peek()

class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

    def test_extract_empty_queue(self):
        print("\n")
        pq = pqueue.pqueue(5)
        with self.assertRaises(KeyError):
            pq.extract_max()
        print("\n")

    def test_insert_and_extract_max(self):
        print("Test inserting multiple elements and extracting max multiple times")
        print("\n")
        max_heap = mheap.max_heap(size=10)
        elements_to_insert = [15, 3, 17, 8, 20, 1, 25]
        for element in elements_to_insert:
            max_heap.insert(element)
        
        extracted_elements = []
        while max_heap.length > 0:
            extracted_elements.append(max_heap.extract_max())

        self.assertEqual(extracted_elements, sorted(elements_to_insert, reverse=True))
        print("\n")

        
class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")
    
    def test_heap_sort_duplicates(self):
        print("Test heap sort with a list that contains a duplicate.")
        print("\n")
        
        sort_list = [5, 1, 3, 1, 5, 2]
        sorted_list = mheap.heap_sort(sort_list)

        self.assertEqual(sorted_list, [1, 1, 2, 3, 5, 5])
        print("\n")

    def test_sorted_heap(self):
        print("Test heap sort with an already sorted list")
        print("\n") 
        sort_list = [1, 2, 3, 4, 5]
        mheap.heap_sort(sort_list)

        self.assertEqual(sort_list, [1, 2, 3, 4, 5])
        print("\n")


    
    
if __name__ == '__main__':
    unittest.main()