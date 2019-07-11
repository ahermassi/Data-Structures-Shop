class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None  # front stores the front node
        self.rear = None  # rear stores the last node

    def is_empty(self):
        return not self.front

    def enqueue(self, data):
        node = QueueNode(data)
        if not self.rear:
            self.front = node
            self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            return
        node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return node.data


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    print('Dequeued item is ', queue.dequeue())