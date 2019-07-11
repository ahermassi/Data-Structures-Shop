class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, key):
    if key < root.data and root.left:
        return search(root.left, key)
    if key > root.data and root.right:
        return search(root.right, key)
    return key == root.data


def insert(root, key):
    if not root:
        root = Node(key)
    elif key <= root.data:
        if not root.left:
            root.left = Node(key)
        else:
            insert(root.left, key)
    elif key > root.data:
        if not root.right:
            root.right = Node(key)
        else:
            insert(root.right, key)


def delete(root, key):
    if not root:
        print('Tree is empty.')
        return root
    if root.data == key:  # If key is same as root's key, then this is the node to be deleted
        # Node with only one child or no child
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        else:
            # Node with two children: Get the smallest in the right subtree
            temp = min_value_node(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)  # Delete that minimum node to avoid redundancy
            return root
    elif key < root.data:  # If the key to be deleted is smaller than the root's key then it lies in left subtree
        root.left = delete(root.left, key)
    else:
        root.right = delete(root.right, key)



def min_value_node(root):
    min_node = root
    while min_node.left:
        min_node = min_node.left
    return min_node


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
    binary_tree = Node(5)
    insert(binary_tree, 3)
    insert(binary_tree, 2)
    insert(binary_tree, 4)
    insert(binary_tree, 7)
    insert(binary_tree, 6)
    insert(binary_tree, 8)
    inorder(binary_tree)
    binary_tree = delete(binary_tree, 2)
    print('\nDeleted 2. Inorder traversal of the modified tree:', end=' ')
    inorder(binary_tree)
    binary_tree = delete(binary_tree, 3)
    print('\nDeleted 3. Inorder traversal of the modified tree:', end=' ')
    inorder(binary_tree)
    binary_tree = delete(binary_tree, 5)
    print('\nDeleted 5. Inorder traversal of the modified tree:', end=' ')
    inorder(binary_tree)

