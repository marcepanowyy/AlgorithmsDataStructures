# Spadajace klocki

# Kazdy klocek to przedzial postaci [a, b]. Dany jest ciag klockow
# [a1, b1], ..., [an, bn]. Klocki spadaja na os liczbowa w kolejnosci
# podanej w ciagu. Prosze zaimplementowac algorytm, ktory oblicza
# ile klockow nalezy usunac z listy tak, zeby kazdy kolejny spadajacy
# klocek miescil sie w calosci w tam, ktory spadl tuz przed nim.

# O(n**2)

def can_stack(brick1, brick2):          # brick2 on brick1
    if brick1[0] <= brick2[0] and brick1[1] >= brick2[1]:
        return True
    return False

def falling_bricks(T):
    n = len(T)
    B = [1] * n                         # kazdy klocem ma wysokosc 1
    res = [[] for _ in range(n)]
    for i in range(n):
        res[i].append(i)
    for i in range(n):
        for j in range(i+1, n):
            brick1 = T[i]
            brick2 = T[j]
            if can_stack(brick1, brick2):
                B[j] = max(B[j], B[i]+1)
                res[i].append(j)

    length = 0
    for i in range(n):
        if length < len(res[i]):
            length = len(res[i])
            max_idx = i

    print("gotta delete", n-length, "bricks")
    print("max height:", length)
    print("brick indexes tower:", res[max_idx])
    return n-length

T1 = [(0,4), (3,10), (4,7), (5,7), (1,2), (6,7)]
T2 = [(1,5), (2,7), (3,4)]
falling_bricks(T2)