from heapq import heapify, heappush, heappop, nlargest, nsmallest

if __name__ == '__main__':
    heap = [5, 7, 9, 1, 3]
    heapify(heap)
    print('The heap created:', *heap)
    # returns [1, 3, 9, 7, 5]; note that heap[k] <= heap[2k+1] and heap[k] <= heap[2k+2] for every heap index k
    # Python docs definition: Heaps are arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k,
    # counting elements from zero.
    heappush(heap, 4)
    print('The modified heap after push:', *heap)
    print('The popped and smallest element is:', heappop(heap))
    print('New heap structure:', *heap)
    print('The 2 largest numbers in list are:', nlargest(2, heap))
    print('The 2 smallest numbers in list are:', nsmallest(2, heap))
