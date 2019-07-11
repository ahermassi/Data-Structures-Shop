""" For better understanding, please draw the circular queue as a pie. """


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear == self.size - 1 and self.front == 0) or self.rear == self.front - 1:
            # 1st condition: for size = 8, front = 0 and rear = 7; queue full for the first time (default fullness
            # setting)
            # 2nd condition: for size = 8, rear = 5 and front = 6 (example); queue full for nth time
            print('Queue is full. Can\'t enqueue any element.')
        elif self.front == -1:  # Condition for empty queue
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = data
        else:
            self.rear  = (self.rear + 1) % self.size
            # For size = 8, if rear = 7 then next position is (7+1) % 8 = 0 -> full queue detected
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print('Queue is empty. Can\'t dequeue any element')
        elif self.front == self.rear:  # Condition for only 1 element. Be careful: not always front = rear = 0
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if self.front == -1:
            print('Queue is empty. No elements to display')
        elif self.rear >= self.front:
            print('Elements in the circular queue are:', end=' ')
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=' ')
            print()
        else:
            print('Elements in the circular queue are:', end=' ')
            for i in range(self.front, self.size):
                print(self.queue[i], end=' ')
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=' ')
            print()


if __name__ == '__main__':
    circularQueue = CircularQueue(5)
    circularQueue.enqueue(14)
    circularQueue.enqueue(22)
    circularQueue.enqueue(13)
    circularQueue.enqueue(-6)
    circularQueue.display()
    print('Deleted value = ', circularQueue.dequeue())
    print('Deleted value = ', circularQueue.dequeue())
    circularQueue.display()
    circularQueue.enqueue(9)
    circularQueue.enqueue(20)
    circularQueue.enqueue(5)
    circularQueue.display()





