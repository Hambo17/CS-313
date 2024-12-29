class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    Attributes
    ----------
    max_size : int
        The total capacity of the heap.
    length : int
        The number of elements currently in the heap.
    heap : list
        The underlying list representing the binary heap.

    Methods
    -------
    get_heap()
        Returns the current heap.
    insert(data)
        Inserts a new element into the heap at the bottom, then sorts 
        said item into the list
    peek()
        Returns the maximum value of the heap.
    extract_max()
        Removes and returns the maximum value in the heap.
    sort_in_place()
        Performs heapsort on the heap.
    build_heap()
        Constructs a max-heap from the current heap.
    __heapify(curr_index, list_length)
        Maintains the max-heap property by moving elements down.

    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        Parameters
        ----------
        size : int, optional
            Total capacity of the heap (default is 20).
        data : list, optional
            A list of elements to initialize the heap. If provided, the size 
            parameter is ignored, and the heap is built from this list.

        """

        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size

    def get_heap(self):
        """
        Returns the current heap.

        """
        return self.heap

    def insert(self, data):
        """Insert an element into the heap.

        The element is inserted at the end and then "bubbled up" to 
        maintain the max-heap property.

        Parameters
        ----------
        data : int
            The element to be inserted into the heap.

        Raises
        ------
        IndexError
            If the heap is full and cannot accept any more elements.
        """

        if (self.length < self.max_size): 
            self.heap[self.length] = data
            self.length += 1

            count =  self.length - 1
            while(count != 0):
                parent_index = (count-1 ) //2

                if (self.heap[count] > self.heap[parent_index]):
                    temp = self.heap[parent_index]
                    self.heap[parent_index] = self.heap[count]
                    self.heap[count] = temp
                    count =  parent_index
                else:
                    break
        else:
            raise IndexError("Heap is full")

    def peek(self):
        """
        Return the maximum value in the heap.

        Returns
        -------
        int
            The maximum value in the heap.

        Raises
        ------
        IndexError
            If the heap is empty.
        """
        if self.length > 0:
            return self.heap[0]
        else:
            raise IndexError("Peek from an empty heap")

    def extract_max(self):
        """
        Remove and return the maximum value in the heap.

        The root is swapped with the last element, 
        then removed, and the heap property is restored.

        Returns
        -------
        int
            The maximum value that was removed from the heap.

        Raises
        ------
        KeyError
            If the heap is empty.
        """
        if (self.length) == 0:
            raise KeyError("Heap is empty")
        else:
            last_node = self.length -1
            self.heap[0], self.heap[last_node] = self.heap[last_node], self.heap[0]
            

            result = self.heap[last_node]
            del self.heap[last_node]
            self.length -= 1

            if self.length > 0:
                self.__heapify(0, self.length)
            return result
            
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap


    def sort_in_place(self):
        """
        Perform heapsort in-place.

        The elements in the heap are sorted in ascending order. After this method is called, 
        the heap is no longer valid.
        
        """
        self.build_heap()

        for i in range(self.length -1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]

            self.__heapify(0, i)
        pass


    def __heapify(self, curr_index, list_length = None):
        """
        Maintain the max-heap property by moving elements down the heap.

        This helper function ensures that the subtree rooted at `curr_index`
        satisfies the max-heap property.

        Parameters
        ----------
        curr_index : int
            The index of the current node to heapify.
        list_length : int, optional
            The number of elements in the heap to consider (used during sorting).
        """

        if ((2*curr_index+1) < list_length):
            if ((2*curr_index+2) < list_length):
                temp_index = 0
                if(self.heap[2*curr_index+1] > self.heap[2*curr_index+2]):
                    temp_index = 2*curr_index+1
                else:
                    temp_index = 2*curr_index+2
                if(self.heap[curr_index] < self.heap[temp_index]):
                    self.heap[curr_index], self.heap[temp_index] = self.heap[temp_index], self.heap[curr_index]
                    self.__heapify(temp_index, list_length)
            else:
                temp_index = 2*curr_index+1
                if(self.heap[curr_index] < self.heap[temp_index]):
                    self.heap[curr_index], self.heap[temp_index] = self.heap[temp_index], self.heap[curr_index]
                    self.__heapify(temp_index, list_length)
        pass

    def build_heap(self):
        """
        Build a max-heap from the current list of elements.

        The heap is constructed by calling `__heapify` on all non-leaf nodes, 
        starting from the bottom.
        
        """
        list_length = self.length

        for i in range(list_length // 2 -1, -1, -1):
            self.__heapify(i, list_length)
        pass


    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


def heap_sort(l):
    """The public heap_sort should do the following.
    1. Create a max_heap object using the provided list l
    2. Call sort_in_place method to sort the list "in-place"
    """
    max_heap_obj = max_heap(data=l)
    max_heap_obj.sort_in_place()
    return max_heap_obj.heap


