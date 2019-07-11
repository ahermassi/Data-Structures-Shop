class QueueNode:
    def __init__(self):
        self.data = None
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None


def enqueue(q, value):
    node = QueueNode()
    node.data = value
    if not q.front:
        q.front = node
    else:
        q.rear.next = node
    q.rear = node
    q.rear.next = q.front


def dequeue(q):
    if not q.front:
        print('Queue is empty. Can\'t dequeue any element')
        return '-9999999999'
    if q.front == q.rear:  # If this is the last node to be dequeued
        temp = q.front
        q.front = None
        q.rear = None
        return temp.data
    temp = q.front
    q.front = q.front.next
    q.rear.next = q.front
    return temp.data

def display(q):
    if not q.front:
        print('Queue is empty. No elements to display')
        return
    temp = q.front
    print('Elements in the circular queue:', end=' ')
    while temp.next != q.front:
        print(temp.data, end=' ')
        temp = temp.next
    print(temp.data)  # This statement is to catch: 1) the last item, or 2) the front if the queue contains only 1 item


if __name__ == '__main__':
    q = CircularQueue()

    # Inserting elements in Circular Queue
    enqueue(q, 14)
    enqueue(q, 22)
    enqueue(q, 6)

    display(q)

    print('Deleted value =', dequeue(q))
    print('Deleted value =', dequeue(q))

    # Remaining elements in Circular Queue
    display(q)

    enqueue(q, 9)
    enqueue(q, 20)
    display(q)


