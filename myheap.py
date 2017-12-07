# Helpers
def swap(array, i1, i2):
    temp = array[i1]
    array[i1] = array[i2]
    array[i2] = temp

class MinHeap(object):
    def __init__(self, array):
        self.heap = list(array)
        MinHeap.minheapify(self.heap)

    @staticmethod
    def minheapify(array):
        # Starting with top top element, swap down with the smaller element
        MinHeap._minheapify_helper(array, 0)

    @staticmethod
    def _minheapify_helper(array, index):
        # Heapify a subtree of array rooted at index
        left = 2 * index + 1
        right = 2 * index + 2
        has_left = left < len(array)
        has_right = right < len(array)
        if has_left:
            MinHeap._minheapify_helper(array, left)
        if has_right:
            MinHeap._minheapify_helper(array, right)

        MinHeap.swap_down(array, index)

    @staticmethod
    def swap_down(array, index):
        left = 2 * index + 1
        right = 2 * index + 2
        has_left = left < len(array)
        has_right = right < len(array)

        if has_left and has_right:
            if array[left] < array[right]:
                if array[left] < array[index]:
                    swap(array, index, left)
                    MinHeap.swap_down(array, left)
            else:
                if array[right] < array[index]:
                    swap(array, index, right)
                    MinHeap.swap_down(array, right)
        elif has_left:
            if array[left] < array[index]:
                swap(array, index, left)
                MinHeap.swap_down(array, left)
        elif has_right:
            if array[right] < array[index]:
                swap(array, index, right)
                MinHeap.swap_down(array, right)

    def take_min(self):
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        MinHeap.swap_down(self.heap, 0)
        return min_item

class MaxHeap(object):
    def __init__(self, array):
        self.heap = list(array)
        maxheapify(self.heap)

    @staticmethod
    def maxheapify(array):
        _maxheapify_helper(array, 0)

    @staticmethod
    def _maxheapify_helper(array, index):
        """Heapifies the subtree rooted at index"""
        left = 2 * index + 1
        right = 2 * index + 2
        has_left = left < len(array)
        has_right = right < len(array)
        if has_left:
            _maxheapify_helper(array, left)
        if has_right:
            _maxheapify_helper(array, right)

        swap_down(array, index)

    @staticmethod
    def swap_down(array, index):
        left = 2 * index + 1
        right = 2 * index + 2
        has_left = left < len(array)
        has_right = right < len(array)
        if has_left and has_right:
            if array[left] > array[right]:
                if array[left] > array[index]:
                    swap(array, left, index)
                    swap_down(array, left)
            else:
                if array[right] > array[index]:
                    swap(array, right, index)
                    swap_down(array, right)
        elif has_left:
            if array[left] > array[index]:
                swap(array, left, index)
                swap_down(array, left)
        elif has_right:
            if array[right] > array[index]:
                swap(array, right, index)
                swap_down(array, right)

    def take_max(self):
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        swap_down(self.heap, 0)
        return max_item

def main():
    array = [1,92,2,134,3,4,303,2,28284,495,1,22,3,9,3]
    print("Original array: %s" % array)
    min_heap = MinHeap(array)
    print("Array after minheap: %s" % array)
#    max_heap = MaxHeap(array)
#    print("Array after maxheap: %s" % array)

    print("Min heap: %s" % min_heap.heap)
#    print("Max heap: %s" % max_heap.heap)

    item = min_heap.take_min()
    print("Min taken: %s, Remaining heap: %s" % (item, min_heap.heap))

 #   item = max_heap.take_max()
 #   print("Max taken: %s, Remaining heap: %s" % (item, max_heap.heap))

if __name__ == "__main__":
    main()
