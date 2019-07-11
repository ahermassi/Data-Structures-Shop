class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join(i for i in self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        """ Popping an element based on Priority  """
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


if __name__ == '__main__':
    priorityQueue = PriorityQueue()
    priorityQueue.insert(12)
    priorityQueue.insert(1)
    priorityQueue.insert(14)
    priorityQueue.insert(7)
    print(*priorityQueue.queue)
    while not priorityQueue.is_empty():
        print(priorityQueue.delete(), )