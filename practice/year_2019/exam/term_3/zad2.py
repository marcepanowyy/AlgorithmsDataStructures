# [2pkt.] Zadanie 2.

# Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai
# i ciągnie się do pozycji bi. Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę
# zaimplementować funkcję tower(A), która wybiera możliwie najdłuższy podciąg klocków taki,
# że spadając tworzą wieżę i żaden klocek nie wystaje poza którykolwiek z wcześniejszych klocków.
# Do funkcji przekazujemy tablicę A zawierającą pozycje klocków ai, bi .Funkcja powinna zwrócić
# maksymalną wysokość wieży jaką można uzyskać w klocków w tablicy A.

# Przykład Dla tablicy A = [(1,4),(0,5),(1,5),(2,6),(2,4)] wynikiem jest 3, natomiast dla
# tablicy A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)] wynikiem jest 2.

def binary_search(arr, val, fn):
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if fn(val, arr[mid_idx]):
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx  # It will never exceed the left side of an array

def longest_seq(arr, fn=lambda a, b: a > b):
    if len(arr) < 2: return len(arr)

    n = len(arr)
    top = []

    for i in range(n):
        j = binary_search(top, arr[i], fn)
        if j == len(top):
            top.append(arr[i])
        else:
            top[j] = arr[i]

    return top


def tower(A: 'array of bricks spans'):
    A = longest_seq(A, lambda curr, prev: curr[0] >= prev[0])
    A = longest_seq(A, lambda curr, prev: curr[1] <= prev[1])
    return len(A)

# ch wie o co cho XD

tower([(1,4),(0,5),(1,5),(2,6),(2,4)])
# print(tower([(0, 10), (1, 9), (2, 7), (3, 5), (4, 14), (5, 15), (15, 17), (15, 16), (15, 16), (4, 5)]))

# runtests(tower)