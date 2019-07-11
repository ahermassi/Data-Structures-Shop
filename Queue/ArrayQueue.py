class Queue:
    def __init__(self, capacity):
        self.size = 0
        self.front = 0
        self.rear = capacity - 1  # Rear value is the index of last enqueued item
        self.queue = [None] * capacity
        self.capacity = capacity

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        ''' This operation adds a new node after rear and moves rear to the next node '''
        if self.is_full():
            print('Queue is full. Can\'t enqueue any element')
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
        print(data, 'enqueued to queue.')

    def dequeue(self):
        ''' This operation removes the front node and moves front to the next node '''
        if self.is_empty():
            print('Queue is empty. Can\'t dequeue any element')
            return
        value = self.queue[self.front]
        self.front  = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def queue_front(self):
        if self.is_empty():
            print('Queue is empty.')
        print('Front item is', self.queue[self.front])

    def queue_rear(self):
        if self.is_empty():
            print('Queue is empty.')
        print('Rear item is', self.queue[self.rear])


if __name__ == '__main__':
    queue = Queue(30)

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    print(queue.dequeue(), 'dequeued from queue')
    queue.queue_front()
    queue.queue_rear()

