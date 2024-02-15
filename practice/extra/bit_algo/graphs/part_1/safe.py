# Dostales sejf, ktory odblokowuje sie czterocyfrowym PINem (0000-9999). Pod wyswietlaczem
# znajduje sie kilka przyciskow z liczbami od 1 do 9999 - przykladowo (13, 223, 782, 3902).
# Sejf ten dziaa inaczej niz normalny. Wcisniecie przycisku z liczba powoduje dodanie liczby
# z przycisku do liczby na wyswietlaczu. Jezeli suma jest wieksza niz 9999, to pierwsza cyfra
# zostaje obcieta.

# Jest tobie znany pin oraz cyfry, ktore sa aktualnie wyswietlane. Znajdz najkrotsza sekwencje
# nacisniec przyciskow, ktora pozwoli ci odblokowac sejf. Jezeli taka sekwencja nie istnieje,
# zwroc None

from collections import deque

def safe(PIN, curr_num, numbers):

    d = deque([])
    visited = [False] * 1000
    parents = [None] * 1000
    distance = [float("inf")] * 1000
    values = [-1] * 1000


    d.append(curr_num)
    distance[curr_num] = 0
    visited[curr_num] = True

    while d:
        u = d.popleft()
        for n in numbers:
            v = (u + n) % 1000
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parents[v] = u
                values[v] = n
                d.append(v)



        if visited[PIN] == True:
            return distance[PIN]

    return None

PIN = 555
curr_num = 455
numbers = [942, 999]
# print(safe(PIN, curr_num, numbers))