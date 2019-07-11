from collections import deque

if __name__ == '__main__':
    de = deque([1, 2, 3])
    print('The deque:', end=' ')
    print(*de)

    de.append(4)
    print('The deque after appending to the right:', *de)

    de.appendleft(6)
    print('The deque after appending to the left:', *de)

    de.append(3)
    print('The deque after appending to the right:', *de)
    print('The number 3 first appeared in position', de.index(3))

    de.insert(4, 5)
    print('The deque after inserting 5 at 5th position:', *de)

    print('The count of 3 in deque is:', de.count(3))

    de.remove(3)
    print('The deque after deleting first occurrence of 3:', *de)

    de.pop()
    print('The deque after popping from the right:', *de)

    de.popleft()
    print('The deque after popping from the left:', *de)

    de.extend([4,5,6])
    print('The deque after extending at right:', *de)

    de.extendleft([7,8,9])
    print('The deque after extending at left:', *de)

    de.reverse()
    print('The deque after reversing:', *de)