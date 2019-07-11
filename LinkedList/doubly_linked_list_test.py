from doubly_linked_list import Node, DoublyLinkedList

if __name__ == '__main__':
    llist = DoublyLinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(4)

    llist.head.next = second
    second.next = third

    llist.print_list()

    llist.insert_after(2, 3)
    print('\nInserting 3 after 2 ..')
    llist.print_list()

    llist.append(5)
    print('\nAppending 5 ..')
    llist.print_list()

    llist.insert_before(2, 0)
    print('\nInserting 0 before 2 ..')
    llist.print_list()

    llist.delete_node_position(4)
    print('\nDeleting node at position 4 ..')
    llist.print_list()

    print('\nCount:', llist.get_count())

    llist.delete_node(4)
    print('\nDeleting 4 ..')
    llist.print_list()