# Consider a 2-D map with a horizontal river passing through its center. There are n cities on the southern
# bank with x-coordinates a(1) … a(n) and n cities on the northern bank with x-coordinates b(1) … b(n).
# You want to connect as many north-south pairs of cities as possible with bridges such that no two bridges cross.
# When connecting cities, you can only connect city a(i) on the northern bank to city b(i) on the southern bank.
# Maximum number of bridges that can be built to connect north-south pairs with the aforementioned constraints.

# Examples:

# Input: 6 4 2 1
#        2 3 6 5
# Output: Maximum number of bridges = 2

def can_extend(b1, b2):
    if b1[0] < b2[0] and b1[1] < b2[1]: return True
    return False

def bridges(A, B):
    n = len(A)
    C = []
    for i in range(n):
        C.append([A[i], B[i]])

    C.sort(key=lambda x: x[1])
    C.sort(key=lambda x: x[0])

    T = [1] * n
    for i in range(n):
        for j in range(i):
            if can_extend(C[j], C[i]) and T[i] < T[j] + 1:
                T[i] = T[j] + 1

    # print(max(T))
    return max(T)

A1 = [6, 4, 2, 1]
B1 = [2, 3, 6, 5]

A2 = [8, 1, 4, 3, 5, 2, 6, 7]
B2 = [1, 2, 3, 4, 5, 6, 7, 8]

# bridges(A1, B1)
# bridges(A2, B2)