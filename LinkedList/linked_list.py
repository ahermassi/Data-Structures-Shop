class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
        node.next = self.head
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
        temp.next = node

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
        temp.next = node

    def insert_at_position(self, position, data):
        """ Method to insert a new node at a given position """
        node = Node(data)
        if not self.head:
            self.head = node
            return
        if position == 1:
            node.next = self.head
            self.head = node
            return
        temp = self.head
        for _ in range(1, position - 1):
            if not temp:
                print('Index out of bound')
                return
            temp = temp.next
        node.next = temp.next
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

    def delete_node_at_start(self):
        """ Method to delete head of linked list """
        if not self.head:
            print('List already empty.')
            return
        self.head = self.head.next

    def delete_node_at_end(self):
        """ Method to delete the tail """
        if not self.head:
            print('List already empty')
            return
        temp = self.head
        while temp.next:
            if not temp.next.next:
                break
            temp = temp.next
        temp.next = None

    def delete_node(self, key):
        """ Method to delete the first occurrence of key """
        if not self.head:
            print('List is empty. No item to delete')
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == key:
                break
            temp = temp.next
        temp.next = temp.next.next

    def delete_node_position(self, position):
        """ Method to delete the node at a given position """
        if not self.head:
            print('List is empty. No item to delete')
            return
        if position == 1:
            self.head = self.head.next
            return
        temp = self.head
        count = 1
        while temp and count < position - 1:
            count += 1
            temp = temp.next
        if not temp:
            print('Node doesn\'t exist')
            return
        temp.next = temp.next.next

    def get_count(self):
        """ Method to count the number of nodes """
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, x):
        """ Method to check whether the value x is present in the linked list """
        temp = self.head
        while temp:
            if temp.data == x:
                return True
            temp = temp.next
        return False

    def search_recursive(self, llist, key):
        """ Recursive method to check whether the value x is present in the linked list """
        if not llist:
            return False
        if llist.data == key:
            return True
        return self.search_recursive(llist.next, key)