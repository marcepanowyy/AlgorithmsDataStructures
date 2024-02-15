# Course Schedule II

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
# take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers,
# return any of them. If it is impossible to finish all courses, return an empty array.

from collections import deque

def findOrder(n, prerequisites):

    sortedOrder = []

    if n <= 0:
        return sortedOrder

    # a. Initialize the graph
    inDegree = [0 for _ in range(n)]     # count of incoming edges
    graph = [[] for _ in range(n)]       # adjacency list graph

    # b. Build the graph
    for child, parent in prerequisites:
        graph[parent].append(child)          # put the child into it's parent's list
        inDegree[child] += 1                 # increment child's inDegree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    d = deque([])

    for u, degree in enumerate(inDegree):
        if degree == 0:
            d.append(u)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while d:
        u = d.popleft()
        sortedOrder.append(u)
        for child in graph[u]:  # get the node's children to decrement their in-degrees
            inDegree[child] -= 1
            if inDegree[child] == 0:
                d.append(child)

    # if sortedOrder doesn't contain all numCourses, there is a cyclic dependency between numCourses, therefore, we
    # will not be able to schedule all numCourses
    if len(sortedOrder) != n:
        return []

    return sortedOrder

numCourses1 = 4
prerequisites1 = [[1,0],[2,0],[3,1],[3,2]]

# findOrder(numCourses1, prerequisites1)