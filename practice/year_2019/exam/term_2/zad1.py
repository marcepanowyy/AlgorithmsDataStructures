# [2pkt.] Zadanie 1.

# Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
# większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
# energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
# szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
# (wartość przekąki dodaje się do aktualnej energii Zbigniewa).

# Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
# len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie.
# Funkcja powinna z wrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
# n-1 lub −1 jeśli nie jest to możliwe.

# Warto rozważyć funkcję f(i, y) zwracającą minimalną liczbę skoków potrzebną by
# dotrzeć do liczby i mając w zapasie dokładnie y jednostek energii.
# Przykład. Dla tablicy A = [2,2,1,0,0,0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1
# na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4,5,2,4,1,2,1,0] wynikiem jest 2
# (Zbigniew skacze z 0 na 3 i z 3 na 7, kończąc z jedną jednostką energii).

from zad1testy import runtests

# O(n*sum(A))

def zbigniew1(A):

    n = len(A)
    max_e = sum(A)+1
    min_jumps = [[float("inf")] * n for _ in range(max_e)]
    min_jumps[A[0]][0] = 0

    for i in range(n):
        for e in range(1, max_e):
            if min_jumps[e][i] != float("inf"):
                pointer = i + 1
                while pointer < n and e - (pointer-i) >= 0:
                    curr_energy = e + A[pointer] - (pointer-i)
                    min_jumps[curr_energy][pointer] = min(min_jumps[curr_energy][pointer], min_jumps[e][i]+1)
                    pointer += 1


    jumps = float("inf")
    for i in range(max_e):
        jumps = min(jumps, min_jumps[i][n-1])
    return jumps

T = [4,5,2,4,1,2,1,0]
zbigniew1(T)
# runtests(zbigniew1)


# albo algorytm zachlanny nlogn z kolejka (podobnie do zadania z ropa Z3 K2 2020/2021)

# albo

from math import inf

def zbigniew(A):
    count = 0
    for i in range(len(A)):
        count += A[i]
    DP = [[inf] * (count + 1) for _ in range(len(A))]
    DP[0][A[0]] = 0
    for i in range(len(A)):
        for j in range(count):
            if DP[i][j] != inf:
                k = i + 1
                while k < len(A) and j >= k - i:
                    index = i + j + A[k] - k
                    DP[k][index] = min(DP[k][index], DP[i][j] + 1)
                    k += 1
    return min(DP[-1])
