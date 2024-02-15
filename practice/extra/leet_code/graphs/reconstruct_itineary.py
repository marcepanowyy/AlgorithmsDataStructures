# Reconstruct Itinerary

# You are given a list of airline tickets where tickets[i] = [from, to] represent the departure and the
# arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical
# order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

def create_graph(tickets):

    graph = {}

    for src, dest in tickets:
        if src in graph:
            graph[src].append(dest)
        else:
            graph[src] = [dest]

    for src, dests in graph.items():
        dests.sort(reverse=True)

    return graph

def reconstruct(graph, start):

    path = []

    def dfs(u):
        if u in graph:
            while graph[u]:
                v = graph[u].pop()
                dfs(v)
        path.append(u)

    dfs(start)
    return path[::-1]

def find_itinerary(tickets):

    graph = create_graph(tickets)
    path = reconstruct(graph, 'JFK')
    return path

tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Expected: ["JFK","MUC","LHR","SFO","SJC"]

tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Expected: ["JFK","ATL","JFK","SFO","ATL","SFO"]

# print(find_itinerary(tickets1))
# print(find_itinerary(tickets2))