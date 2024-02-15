# Unique Binary Search Trees

# Given an integer n, return the number of structurally unique bst's (binary search trees)
# which has exactly n nodes of unique values from 1 to n.

def unique_BST(n):

    # numTree[4] = numTree[0] * numTree[3] (czworka korzeniem, po lewej 0 nodow, po prawej moga byc 3) +
    #              numTree[1] * numTree[2] (po lewej 1 node, po prawej 2) +
    #              numTree[2] * numTree[1] +
    #              numTree[3] * numTree[0]

    # 0 node = 1 tree
    # 1 node = 1 tree

    numTree = [1] * n

    for node in range(2, n+1):
        total = 0
        for root in range(1, node+1):
            left = root - 1
            right = node - root
            total += numTree[left] * numTree[right]
        numTree[node] = total

    return numTree[n]


# drugi sposob matematyczny O(1) XD

from math import factorial

def unique(n):
    return factorial(2*n) // (factorial(n+1) * factorial(n))
