class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(item, 'pushed to stack')

    def pop(self):
        if self.is_empty():
            print('Stack is empty. Can\'t pop elements')
            return
        return self.stack.pop()

    def peek(self):
        """ Method to return the top from stack without removing it  """
        if self.is_empty():
            print('Stack is empty.')
            return
        return self.stack[-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('Peek:', stack.peek())
    print(stack.pop(), 'popped from stack')
    print(stack.pop(), 'popped from stack')
    print(stack.pop(), 'popped from stack')
    stack.pop()
