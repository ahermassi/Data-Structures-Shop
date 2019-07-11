class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        if not temp:
            print('List is empty')
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def push(self, data):
        """ Method to insert a new node at the beginning """
        node = Node(data)
        if not self.head:
            self.head = node
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_after(self, node_to_insert_after, data):
        """ Method to insert a new node after the given node """
        node = Node(data)
        temp = self.head
        while temp:
            if temp.data == node_to_insert_after:
                break
            temp = temp.next
        if not temp:
            print('Item does not exist')
            return
        node.next = temp.next
        node.prev = temp
        temp.next = node
        if node.next:  # Change previous of new node's next node
            node.next.prev = node

    def insert_before(self, node_to_insert_before, data):
        """ Method to insert a new node after the given node """
        node = Node(data)
        temp = self.head
        if temp.data == node_to_insert_before:
            node.next = temp
            self.head = node
            return
        while temp.next:
            if temp.next.data == node_to_insert_before:
                break
            temp = temp.next
        if not temp.next:
            print('Item doesn\t exist')
            return
        node.next = temp.next
        node.prev = temp
        temp.next = node

    def append(self, data):
        """ Method to append a new node at the end """
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.prev = temp  # Make last node as previous of new node

    def delete_node(self, key):
        """ Method to delete the first occurrence of key """
        if not self.head:
            print('List is empty. No item to delete')
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        temp = self.head
        while temp:
            if temp.data == key:
                break
            temp = temp.next
        temp.prev.next = temp.next

    def delete_node_position(self, position):
        """ Method to delete the node at a given position """
        if not self.head:
            print('List is empty. No item to delete')
            return
        if position == 1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(1, position):
            if not temp:
                print('Index out of bound')
                return
            temp = temp.next
        temp.prev.next = temp.next

    def get_count(self):
        """ Method to count the number of nodes """
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
