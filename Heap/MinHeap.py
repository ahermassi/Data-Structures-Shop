from heapq import heappush, heappop, heapify


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert_key(self, key):
        heappush(self.heap, key)

    def decrease_key(self, i, new_val):
        """ Decrease value of key at index 'i' to new_val
        If the decreased key value of a node is greater than the parent of the node, then we don’t need to do anything.
        Otherwise, we need to traverse up to fix the violated heap property. """
        self.heap[i] = new_val
        while i != 0 and self.heap[i] < self.heap[self.parent(i)]:  # If parent is greater than new child,
            # then the min heap condition is violated
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def extract_min(self):
        return heappop(self.heap)

    def delete_key(self, i):
        """ Delete key at index i
        We replace the key to be deleted with minum infinite by calling decreaseKey(). After decreaseKey(), the minus
        infinite value must reach root, so we call extractMin() to remove the key."""
        self.decrease_key(i, float('-inf'))
        self.extract_min()

    def get_min(self):
        return self.heap[0]


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert_key(3)
    heap.insert_key(2)
    heap.insert_key(1)
    heap.insert_key(15)
    heap.insert_key(5)
    heap.insert_key(4)
    heap.insert_key(45)

    print('Heap:', *heap.heap)
    print('Extracting (popping) min:', heap.extract_min())
    print('Heap:', *heap.heap)
    heap.decrease_key(2, 1)
    print('Decreased heap[2] to 1 ..')
    print('Heap min:', heap.get_min())

