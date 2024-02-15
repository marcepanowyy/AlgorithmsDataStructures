# takie jak zad.1 na kolosie II 2020/2021

# Paweł Konop

from zad4testy import runtests

# knapsack z ograniczeniami

# f(building, cost) - maksymalna liczba studentow, ktore moga mieszkac w budynku
# od 0 do 'i', ktore na siebie nie nachodza i kosztuja najwyzej 'cost'

# prev(i) - pierwszy budynek przed i, nie nachodzacy na niego
# students(i) - liczba studentow, ktora bedzie zamieszkiwac i-ty budynek

# (nlogn + n^2)

def find_prev(T, i):
    b = 0
    e = i
    while b <= e:
        mid = (b+e)//2
        if T[mid][2] >= T[i][1]:
            e = mid-1
        else:
            b = mid+1
    return e

# prev(i) - nr indeksu budynku przed budynkiem i, ktory na niego nie nachodzi nlogn

def prev(T):
    n = len(T)
    prevs = []
    for i in range(n):
        prevs.append(find_prev(T, i))
    return prevs

def get_solution(F, T, building, cost, prevs):
    if building < 0: return []
    if building == 0:
        if cost >= T[0][3]: return [T[0][4]]
        return []
    if cost >= T[building][3] and F[building][cost] == F[prevs[building]][cost - T[building][3]] + students(T, building):
        x = F[building][cost]
        y = F[prevs[building]][cost - T[building][3]]
        z = students(T, building)
        return get_solution(F, T, prevs[building], cost-T[building][3], prevs) + [T[building][4]]
    return get_solution(F, T, building-1, cost, prevs)

def students(T, i):
    return T[i][0] * (T[i][2] - T[i][1])

def select_buildings(T, p):
    n = len(T)
    for i in range(n):
        T[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)

    T.sort(key=lambda x: x[2])
    prevs = prev(T)

    F = [[0] * (p+1) for _ in range(n)]
    for cost in range(T[0][3], p+1):
        F[0][cost] = students(T, 0)

    for building in range(1, n):
        for cost in range(1, p+1):
            F[building][cost] = F[building-1][cost]
            if cost >= T[building][3]:
                F[building][cost] = max(F[building][cost], students(T, building) + F[prevs[building]][cost-T[building][3]])

    total = F[n-1][p]

    actual_cost = p
    while F[n-1][actual_cost-1] == total:  # interesuje nas najmniejszy koszt
        actual_cost -= 1

    res = get_solution(F, T, n-1, actual_cost, prevs)
    res.sort()

    return res

runtests(select_buildings)

