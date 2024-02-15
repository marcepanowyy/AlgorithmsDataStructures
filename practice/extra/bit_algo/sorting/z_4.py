# Dana jest klasa:

# class Node:
#     val = 0
#     next = None

# reprezentujaca wezel jdnokierunkowego lanyucha odsylaczowego, w kotrym wartosci val poszeglonych wezlow zostaly wygenerowane
# zgodnie z rozkladem jednostajnym na przedziale [a,b]

# standardowy bucketsort tylko na linkliscie


class Node():
    def __init__(self):
        self.next = None
        self.value = None

def tab2list(A):
    head = Node()
    tail = head
    for i in range(len(A)):
        x = Node()
        x.value = A[i]
        tail.next = x
        tail = x
    return head.next

def print_list(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")

def bubble_sort(bucket):
    n = len(bucket)
    for i in range(n):
        for j in range(i + 1, n):
            if bucket[j].get_value < bucket[i].get_value:
                bucket[i], bucket[j] = bucket[j], bucket[i]

def find_lenght(H):
    l = 0
    while H != None:
        l += 1
        H = H.next
    return l

def create_bucket_array(H):
    n = find_lenght(H)
    buckets = [[] for _ in range(n)]
    for node in range(n):
        buckets[int(H.value * n)].append(H)
        H = H.next

    return buckets


def bucket_sort(H):

    buckets = create_bucket_array(H)


    head = Node()
    tail = head

    for bucket in buckets:
        bubble_sort(bucket)
        i = 0
        for elem in bucket:
            tail.next = bucket[i]
            tail = tail.next
            i += 1

    tail.next = None
    return head.next

# T = [0.12, 0.8, 0.44, 0.874, 0.15, 0.42, 0.98, 0.712, 0.628, 0.151, 0.752, 0.28]
# H = tab2list(T)
# print_list(H)

# res = bucket_sort(H)
# print_list(res)


size = 80000


import random
T = [random.randint(1, 100000)/100000 for _ in range(size)]
H = tab2list(T)
# print_list(H)
H = bucket_sort(H)
print_list(H)

