from linked_list import LinkedList, Node

if __name__ == '__main__':
    llist = LinkedList()

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

    llist.delete_node(3)
    print('\nDeleting 3 ..')
    llist.print_list()

    llist.delete_node_position(4)
    print('\nDeleting node at position 4 ..')
    llist.print_list()

    print('\nCount:', llist.get_count())
    llist.print_list()

    print('\n')
    print('Item 2 found' if llist.search(2) else 'Item 2 not found')
    print('Item 7 found' if llist.search(7) else 'Item 7 not found')

    print('\n')
    print('Item 2 found (recursive)' if llist.search_recursive(llist.head, 2) else 'Item 2 not found (recursive)')
    print('Item 7 found (recursive)' if llist.search_recursive(llist.head, 7) else 'Item 7 not found (recursive)')

    llist.insert_before(4, 0)
    print('\nInserting 0 before 2 ..')
    llist.print_list()

    llist.insert_at_position(3, 3)
    print('\nInserting 3 at position 3 ..')
    llist.print_list()

    llist.delete_node_at_end()
    print('\nDeleting the tail ..')
    llist.print_list()
