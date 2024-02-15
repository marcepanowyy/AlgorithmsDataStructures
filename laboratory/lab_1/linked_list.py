# Implementacja wstawianie Node'a do posortowanej
# listy jednokierunkowej

class Node:
    def __init__(self):
        self.next = None
        self.value = None

def insert_to_node(node, L):
    start = L
    while L.next != None and L.next.get_value < node.get_value:
        L = L.next

    node.next = L.next
    L.next = node


# Implementacja wypisywanie listy jednokierunkowej

def print_List(L):
    if L is not None:
        print(L.get_value, end=" ")
        print_List(L.next)
    else:
        print()

# L = Node()
# nnode = Node()
# nnode.value = 2
# L.next = nnode
# nn = Node()
# nn.value = 5
# nnode.next = nn
# print_List(L)
# a = Node()
# a.value = 1
# insert_to_node(a, L)
# print_List(L)
# b = Node()
# b.value = 3
# insert_to_node(b, L)
# print_List(L)
# c = Node()
# c.value = 7
# insert_to_node(c, L)
# print_List(L)

# Implementacja usuwania z listy jednokierunkowej
# najwiekszej liczby

def delMax(L):
    m = L.next
    m_prev = L
    prev = L
    L=L.next

    while prev.next != None:
        if prev.next.get_value > m.get_value:
            m_prev = prev
            m = prev.next
        prev = prev.next

    m_prev.next = m.next
    return L

# Funkcja odwracajaca kolejnosc wezlow w liscie

def reverse(L):
    if L is None:
        return

    prev = None
    nxt = L.next

    while L:
        L.next = prev
        prev = L
        L = nxt
        if nxt != None:
            nxt = nxt.next

    return prev