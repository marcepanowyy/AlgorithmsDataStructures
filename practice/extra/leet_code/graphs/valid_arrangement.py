# Valid Arrangement of Pairs

# You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi].
# An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

# Return any valid arrangement of pairs.

# Note: The inputs will be generated such that there exists a valid arrangement of pairs.

from collections import defaultdict

def valid_arr(pairs):

    G = defaultdict(list)
    din = defaultdict(int)
    dout = defaultdict(int)

    for u, v in pairs:
        G[u].append(v)                           # creating a neigbour list
        dout[u] += 1                             # indegree of end is incremented
        din[v] += 1                              # outdegree of start is incremented

    start = pairs[0][0]                          # initialized the start to first pair start
    for u in G:
        if din[u] + 1 == dout[u]:                # finding the start node(hierholzer)
            start = u
    route = []

    def dfs(u):
        while G[u]:
            v = G[u].pop()
            dfs(v)
        route.append(u)

    dfs(start)
    route.reverse()

    return [[route[i], route[i + 1]] for i in range(len(route) - 1)]

pairs1 = [[5,1],[4,5],[11,9],[9,4]]

# print(valid_arr(pairs1))