# XD nigdy nie sadzilem ze bede to implementowac

# Education 4u hamiltioniam circuit problem using backtracking

class Node():
    def __init__(self, id):
        self.id = id
        self.children = []
        self.parents = []


def hamiltionian_cycle(G):

    def recur(root):
        for child in G[root.id]:
            if child not in root.parents:
                leaf = Node(child)
                root.children.append(child)
                leaf.parents = root.parents + [root.id]
                if len(leaf.parents) == len(G)-1 and leaf.id in G[0]:
                    return leaf.parents + [leaf.id]
                elif recur(leaf) != []:
                    return recur(leaf)
        return []

    n = len(G)
    root = Node(0)
    cycle = recur(root)
    if len(cycle) != n: return False
    return cycle

G1 = [[1,2,3], [0,2,5], [0,1,3,4], [0,2,4], [2,3,5], [1,4]]

# print(hamiltionian_cycle(G1))

G2 = [[1,4], [0,2], [1,3,4], [2,5,6], [0,2,7], [3,6,7], [3,5], [4,5]]

# print(hamiltionian_cycle(G2))


