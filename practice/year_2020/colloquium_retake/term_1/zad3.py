# Dyrektor działu handlowego pewnej firmy odbywa podróż służbową z miasta A do miasta B. lecture pewnych
# punktach zaplanowanej trasy znajdują się stacje benzynowe. Niestety, ze względu na problemy
# z dostawami surowca, stacje limitują objętość paliwa, którą może zatankować pojedynczy klient.
# Co więcej, z powodu modyfikacji zmierzających do zwiększenia głośności i mocy silnika, samochód
# dyrektora spala aż 1 litr paliwa na 1 kilometr trasy. Dyrektor się spieszy - musi więc tak
# zaplanować podróż, by zatrzymać się na jak najmniejszej liczbie stacji. Jest to o tyle niełatwe, że
# każda stacja ma własny limit litrów paliwa, które można na niej zatankować. Dodatkową przeszkodą
# jest fakt, że w celu zmniejszenia masy pojazdu zmodyfikowano w nim zbiornik paliwa, który obecnie
# mieści jedynie q litrów benzyny. Zaproponuj i zaimplementuj algorytm wskazujący na których stacjach
# dyrektor powinien tankować paliwo (tak, by tankować możliwie najmniejszą liczbę razy). Algorytm
# powinien być możliwie jak najszybszy i zużywać jak najmniej pamięci. Uzasadnij jego poprawność
# i oszacuj złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:

# def iamlate(T, V, q, l):
#     ...

# która przyjmuje:

# 1. Tablicę liczb naturalnych T z pozycjami stacji benzynowych, wyrażonymi jako kilometry od
# początku trasy. Pierwsza stacja znajduje się na początku trasy, t.j. T[0] = 0. Kolejne stacje
# umieszczone są w T w kolejności odleglości od początku trasy.

# 2. Tablicę dodatnich liczb naturalnych V zawierającą limity paliwa, które może zatankować
# pojedynczy klient. Tak więc V[i] to liczba litrów paliwa, którą można zatankować na stacji
# w pozycji T[i]. Na danej stacji można tankować tylko raz.

# 3. Dodatnią liczbę naturalną q będącą pojemnością baku samochodu (liczba litrów paliwa, które
# mieszczą się w baku). Zakładamy, że przed pierwszym tankowaniem w baku nie ma paliwa.

# 4. Dodatnią liczbę naturalną l będącą długością trasy w kilometrach.

# Funkcja powinna zwrócić listę numerów stacji, na których należy tankować paliwo (w kolejności
# tankowania). Jeśli warunki zadania uniemożliwiają dotarcie do celu, funkcja powinna zwrócić pustą
# listę. Stacje numerujemy od 0. Stacja na początku trasy stanowi część rozwiązania.

# Przyklad. Dla danych:

# T = [0, 1, 2]
# V = [2, 1, 5]
# q = 2
# l = 4

# wynikiem jest np. lista [0, 2]

# wszystko spk, ale get solution nie napisalem XD

def iamlate(T, V, q, l):

    T.append(l)
    V.append(0)

    n = len(T)
    dp = [[float("inf")] * n for _ in range(q+1)]
    parents = [[-1] * n for _ in range(q+1)]
    dp[min(V[0], q)][0] = 1

    for i in range(n):
        for fuel in range(q+1):
            if dp[fuel][i] != float("inf"):
                for j in range(i+1, n):
                    if fuel - (T[j] - T[i]) >= 0:
                        fuel_left = fuel - (T[j] - T[i])
                        if dp[fuel_left + V[j]][j] > dp[fuel][i] + 1:
                            dp[fuel_left + V[j]][j] = dp[fuel][i] + 1
                            parents[fuel_left + V[j]][j] = i

                    else: break

    times = float("inf")
    for i in range(q+1):
        if dp[i][n-1] < times:
            times = dp[i][n-1]
            actual_fuel = i

    times -= 1

    # def get_solution(i, fuel_left):
    #     if i == 0: return [0]
    #     curr_idx = i
    #     next_idx = parents[fuel_left][i]
    #     fuel_left = T[i] - T[parents[fuel_left][i]] - V[parents[fuel_left][i]]
    #     return [next_idx] + get_solution(next_idx, fuel_left)
    # res = get_solution(n-1, actual_fuel)

    # print(*parents, sep="\n")


from zad3testy import runtests

# runtests(iamlate)

# T =  [0, 5, 10]
# V =  [10, 5, 20]
# q =  100
# l =  35

# print(iamlate(T, V, q, l))