class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def push(self, data):
        """ Pushing to the stack is equivalent to inserting at the front """
        node = StackNode(data)
        node.next = self.head
        self.head = node
        print(data, 'pushed to the stack')

    def pop(self):
        """ Popping from the stack is equivalent to removing the head and returning it """
        if self.is_empty():
            print('Stack is empty. Can\'t pop elements')
            return
        node = self.head
        self.head = self.head.next
        return node.data

    def peek(self):
        if self.is_empty():
            print('Stack is empty.')
            return
        return self.head.data


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('Peek:', stack.peek())
    print(stack.pop(), 'popped from stack')
    print('Peek:', stack.peek())
    print(stack.pop(), 'popped from stack')
    print('Peek:', stack.peek())
    print(stack.pop(), 'popped from stack')
    stack.pop()