import heapq

if __name__ == '__main__':
    l = [5, 7, 9, 1, 3]
    heapq.heapify(l)
    print('The heap created:', *l)