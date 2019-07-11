from queue import Queue

if __name__ == '__main__':

    q = Queue(20)
    q.put(5)
    q.put(9)
    q.put(1)
    q.put(7)
    print('Queue size:', q.qsize())
    print('Queue full:', q.full())
    q.put(9)
    q.put(10)
    for _ in range(q.qsize()):
        print(q.get())
    print('Queue empty:', q.empty())

