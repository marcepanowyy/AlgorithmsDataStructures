# [2pkt.] Zadanie 3.
# Szablon rozwiązania: zad3.py
# Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
# zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
# funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
# z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
# zawsze prawidłowa.)
# Przykład Dla tablicy
# A = [1,100, 5, 100, 1, 5, 1, 5]
# wartością wywołania longest incomplete(A, 3) powinno być 4 (ciąg 1, 5, 1, 5 z końca tablicy).


def Longestincomplete(A, k):
    n = len(A)
    max = 0
    C = []

    for i in range(n):
        if A[i] not in C:
            C += [A[i]]

    for num in range(k):
        c = 0
        for i in range(n):
            if A[i] == C[num]:
                c = 0
            else:
                c += 1

            if c > max:
                max = c

    return max

T = [1, 100, 5, 100, 1, 5, 1, 5]
print(Longestincomplete(T, 3))


# ROZW MATIEGO

def binary_search_first(arr: 'sorted sequence', el: 'searched element') -> int:
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if el > arr[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx if left_idx < len(arr) and arr[left_idx] == el else -1


def insert_element(arr, val: 'inserted value'):
    arr.append(val)
    # Move all elements that are greater than a value inserted to the right
    idx = len(arr) - 1
    while idx > 0 and arr[idx - 1] > val:
        arr[idx] = arr[idx - 1]
        idx -= 1
    # Place our value on the final position
    arr[idx] = val


def longest_incomplete(A, k):
    if k < 2: return 0

    # Find all unique values
    U = []
    for val in A:
        i = binary_search_first(U, val)
        if i < 0:
            insert_element(U, val)

    # Using two pointers, look for the longest incomplete subsequence
    i = j = 0
    C = [0] * k

    # Find first subsequence of k - 1 unique elements
    remaining = k
    while i < len(A) and remaining:
        idx = binary_search_first(U, A[i])
        if not C[idx]:
            remaining -= 1
        C[idx] += 1
        i += 1

    # Move the window of k - 1 unique elements
    max_len = i - 1
    while i < len(A):
        if not remaining:
            idx = binary_search_first(U, A[j])
            C[idx] -= 1
            if not C[idx]:
                remaining += 1
            j += 1
        else:
            idx = binary_search_first(U, A[i])
            if not C[idx]:
                remaining -= 1
                max_len = max(max_len, i - j)
            C[idx] += 1
            i += 1

    return max_len
