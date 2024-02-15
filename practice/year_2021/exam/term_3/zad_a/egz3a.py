# Paweł Konop

# algorytm zachłanny
# w poniższym algorytmie dodaje do tablicy krotkę zawierającą informację (punkt, typ punktu - poczatek/koniec)
# nastepnie sortuje te punkty rosnąco
# później przeglądam tablicę
# jesli trafiam na początek, zwiększam licznik a jeśli na koniec, to zmniejszam
# za każdym razem aktualizuje maksimum osiągnięte przez licznik po danej operacji

# O(nlogn)


from egz3atesty import runtests


def snow(T, I):
    res = []
    for start, end in I:
        res.append([start, 0])
        res.append([end, 1])

    res.sort(key = lambda x: x[0])
    cnt = 0
    maxi = 0

    for i, type in res:
        if type == 0: cnt += 1
        else: cnt -= 1
        maxi = max(maxi, cnt)
    return maxi

runtests( snow, all_tests = True )

