# Kopiec min

def insert(T, key):
    T.append(key)
    i = len(T) - 1
    while i > 0 and T[i][1] < T[(i - 1) // 2][1]:
        T[i], T[(i - 1) // 2] = T[(i - 1) // 2], T[i]
        i = (i - 1) // 2
    return T

def heapify(A, n, i):

    l = 2 * i + 1
    r = 2 * i + 2
    m = i

    if l < n and A[l][1] < A[m][1]: m = l
    if r < n and A[r][1] < A[m][1]: m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)

def getOrder(tasks):

    n = len(tasks)
    for i in range(n):
        tasks[i].append(i)
    tasks.sort(key=lambda x: x[0])

    time = tasks[0][0]
    res = []
    heap = []

    i = 0
    while i < n or heap:
        while i < n and tasks[i][0] <= time:
            insert(heap, tasks[i])
            i += 1

        heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
        enqueueT, processingT, index = heap.pop()
        heapify(heap, len(heap) - 1, 0)

        time += processingT
        res.append(index)

    return res


tasks1 = [[1,2],[2,4],[3,2],[4,1]]
# Output: [0,2,3,1]
# res1 = getOrder(tasks1)

tasks2 = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# Output: [4,3,2,0,1]
# res2 = getOrder(tasks2)

tasks3 = [[19, 13], [16, 19], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]]
# Output: [6,1,2,9,4,10,0,11,5,13,3,8,12,7] bledny output :)
res3 = getOrder(tasks3)

# /////////////////////////////////////////////////////////

# Kolejka priorytetowa

from queue import PriorityQueue

def getOrderPriorityQueue(tasks):

    n = len(tasks)
    for i in range(n):
        tasks[i].append(i)
    tasks.sort(key=lambda x: x[0])

    time = tasks[0][0]
    pq = PriorityQueue()
    res = []

    i = 0
    while i < n or not pq.empty():
        while i < n and tasks[i][0] <= time:
            pq.put((tasks[i][1], tasks[i][0], tasks[i][2]))
            i += 1

        processingT, enqueueT, index = pq.get()
        time += processingT
        res.append(index)

    return res

tasks4 = [[1,2],[2,4],[3,2],[4,1]]
# Output: [0,2,3,1]
res4 = getOrderPriorityQueue(tasks4)

tasks5 = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# Output: [4,3,2,0,1]
res5 = getOrderPriorityQueue(tasks5)

tasks6 = [[19, 13], [16, 19], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]]
# Output: [6,1,2,9,4,10,0,11,5,13,3,8,12,7]
res6 = getOrderPriorityQueue(tasks6)
