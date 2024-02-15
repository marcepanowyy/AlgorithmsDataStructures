# Given the head of a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced bst.

# For this problem, a height-balanced binary tree is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.

# O(n)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tab_to_list(arr):
    head = ListNode(arr[0])
    tail = head
    n = len(arr)
    for i in range(1, n):
        new_node = ListNode(arr[i])
        tail.next = new_node
        tail = tail.next
    return head

# find root - srodkowa wartosc

def find_mid(head):

    double = head
    single = head
    prev = head

    while double != None and double.next != None:   # single skacze pojedynczo, double podwojnie
        prev = single
        single = single.next
        double = double.next.next

    if prev != None:
        prev.next = None

    return single

def create_tree(head):

    if head == None: return None

    mid = find_mid(head)
    root = TreeNode(mid.val)

    if head == mid: return root

    root.left = create_tree(head)
    root.right = create_tree(mid.next)
    return root



arr1 = [-10, -3, 0, 5, 9]
arr2 = [1, 15, 22, 108]
arr3 = [10]

list1 = tab_to_list(arr1)
list3 = tab_to_list(arr3)

# tree = create_tree(list1)
