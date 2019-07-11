class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(temp, key):
    """ Do iterative level order traversal of the given tree using queue, until we find an empty place """
    q = list()
    q.append(temp)
    while len(q):
        temp = q.pop(0)
        if not temp.left:
            temp.left = Node(key)
            break
        q.append(temp.left)
        if not temp.right:
            temp.right = Node(key)
            break
        q.append(temp.right)


def level_order(root):
    if not root:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        print(temp.data, end=' ')
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)


def inorder(root):
    """ Left - Root - Right traversal """
    if not root:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


def preorder(root):
    """ Root - Left - Right traversal """
    if not root:
        return
    print(root.data, end=' ')
    inorder(root.left)
    inorder(root.right)


def postorder(root):
    """ Left - Right - Root traversal """
    if not root:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print('Inorder traversal before insertion:', end=' ')
    inorder(root)
    insert(root, 12)
    print('\nInorder traversal after insertion:', end=' ')
    inorder(root)
    print('\nPreorder traversal after insertion:', end=' ')
    preorder(root)
    print('\nPostorder traversal after insertion:', end=' ')
    postorder(root)
    print('\nLevel order (breadth first) traversal after insertion:', end=' ')
    level_order(root)
