# Given the root of a binary search tree, return a balanced binary search tree with the same node values.
# If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# O(n)
# zajebiscie dziala es

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_mid(head):

    double = head
    single = head
    prev = head

    while double != None and double.right != None:   # single skacze pojedynczo, double podwojnie
        prev = single
        single = single.right
        double = double.right.right

    if prev != None:
        prev.right = None

    return single

def create_tree(head):

    if head == None: return None

    mid = find_mid(head)
    root = TreeNode(mid.val)

    if head == mid: return root

    root.left = create_tree(head)
    root.right = create_tree(mid.right)
    return root


def balance_bst(root):

    node_arr = []

    def in_order(node):
        if not node: return
        in_order(node.left)
        node_arr.append(node)
        in_order(node.right)

    in_order(root)
    n = len(node_arr)

    for i in range(1, n):
        node_arr[i-1].right = node_arr[i]

    node_arr[n-1].right = None

    return create_tree(node_arr[0])


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)

A.right = B
B.right = C
C.right = D

root1 = balance_bst(A)



a = TreeNode(1)
b = TreeNode(-1)
c = TreeNode(15)
d = TreeNode(0)
e = TreeNode(20)
f = TreeNode(17)
g = TreeNode(16)

a.left = b
a.right = c
b.right = d
c.right = e
e.left = f
f.left = g

root2 = balance_bst(a)
