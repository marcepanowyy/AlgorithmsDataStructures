from zad7testy import runtests
from random import randint

def create_new(G):

    n = len(G)
    newG = [[] for _ in range(2*n)]

    for i in range(n):

        newG[2*i].append(2*i+1)
        newG[2*i+1].append(2*i)

        for n in G[i][0]:
            if i in G[n][0]:
                newG[2*i].append(2*n)
            else:
                newG[2*i].append(2*n+1)

        for s in G[i][1]:
            if i in G[s][0]:
                newG[2*i+1].append(2*s)
            else:
                newG[2*i+1].append(2*s+1)


    return newG

class Node():
    def __init__(self, id):
        self.id = id
        self.children = []
        self.parents = []

def hamiltionian_cycle(G):

    n = len(G)
    v = randint(0, n-1)

    def recur(root):
        nonlocal v
        if root.id % 2 == 0:
            leaf = Node(root.id+1)
            root.children.append(root.id+1)
            leaf.parents = root.parents + [root.id]
        else:
            leaf = Node(root.id-1)
            root.children.append(root.id-1)
            leaf.parents = root.parents + [root.id]

        root = leaf

        for child in G[root.id]:
            if child not in root.parents:
                leaf = Node(child)
                root.children.append(child)
                leaf.parents = root.parents + [root.id]
                if leaf.id % 2 == 0 and len(leaf.parents) == len(G)-2 and leaf.id+1 in G[v]:
                    return leaf.parents + [leaf.id] + [leaf.id+1]
                elif leaf.id % 2 == 1 and len(leaf.parents) == len(G)-2 and leaf.id-1 in G[v]:
                    return leaf.parents + [leaf.id] + [leaf.id-1]
                elif recur(leaf) != []:
                    return recur(leaf)
        return []

    root = Node(v)
    return recur(root)

testG = [[1,3,7], [0,9], [5,3,4,6], [2,0,5], [2,5,8], [2,3,4], [2,7], [0,6], [4,9], [1,9]]

def modify(res):
    n = len(res)
    sol = []
    for i in range(0, n, 2):
        sol.append(res[i]//2)
    return sol

def droga(G):
    new_G = create_new(G)
    res = hamiltionian_cycle(new_G)
    if res == []: return None
    return modify(res)


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(droga, all_tests = True)

