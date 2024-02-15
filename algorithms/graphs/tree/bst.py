class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value
        self.left_size = 0
        self.right_size = 0

def insert(T, key):
    W = BNode(key)
    if key < T.value:
        if T.left == None:
            T.left = W
            W.parent = T
        else:
            insert(T.left, key)
    else:
        if T.right == None:
            T.right = W
            W.parent = T
        else:
            insert(T.right, key)

def createTree(keys):
    T = BNode(keys[0])
    for i in range(1, len(keys)):
        insert(T, keys[i])
    return T

def size(p):
    return 0 if p is None else size(p.left) + size(p.right) + 1

def height(p):
    return 0 if p is None else max(height(p.left), height(p.right)) + 1

def find(root, key):
    while root != None:
        if root.value == key:
            return root
        elif key < root.value:
            root = root.left
        else:
            root = root.right

    return None

def find_min(root):
    if not root.left: return root
    return find_min(root.left)

def find_max(root):
    if not root.right: return root
    return find_max(root.right)


def find_predecessor_node(root):                         # poprzednik (najwieksza liczba mniejsza niz zadana)
    if root.left: return find_max(root.left)
    while root.parent:
        if root.parent.right == root:
            return root.parent
        root = root.parent
    return None


def find_successor_node(root):                           # nastepnik (najmniejsza liczba wieksza niz zadana)
    if root.right: return find_min(root.right)
    while root.parent:
        if root.parent.left == root:
            return root.parent
        root = root.parent
    return None


def count_children(tree):
    if tree.left:
        count_children(tree.left)
        tree.left_size = 1 + tree.left.left_size + tree.left.right_size
    if tree.right:
        count_children(tree.right)
        tree.right_size = 1 + tree.right.left_size + tree.right.right_size
    return 0


def find_kth_element(tree, k):

    if k - (tree.left_size + 1) == 0:
        return tree

    elif k - (tree.left_size + 1) > 0:
        return find_kth_element(tree.right, k - (tree.left_size + 1))

    else:
        return find_kth_element(tree.left, k)


def calculate_sum(tree):

    if not tree: return 0
    return tree.value + calculate_sum(tree.left) + calculate_sum(tree.right)


keys1 = [10, 3, 15, 11, 17, -1, -5, 0]
tree1 = createTree(keys1)

keys2 = [21, 15, 37, 5, 40, 20, 7, 13, 25, 8]
tree2 = createTree(keys2)

keys3 = [21, 15, 37, 5, 40, 20, 7, 13, 25, 8, 24, 26]
tree3 = createTree(keys3)

# count_children(tree3)

# for i in range(1, len(keys3)+1):
#     print(i, "'th element = ", find_kth_element(tree3, i).value)

# print(calculate_sum(tree3))


