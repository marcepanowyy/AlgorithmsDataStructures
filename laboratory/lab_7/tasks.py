# Wybor zadan z terminami

# Mamy dany zbior zadan T = {t1, ..., tn} Kazde zadanie ti dodatkowo posiada

# (a) termin wykonania d(ti) (liczba naturalna)
# (b) zysk g(ti) za wykonanie w terminie (liczba naturalna)

# Wykonanie kazdego zadania trwa jednostke czasu. Jesli zadanie ti zostanie
# wykonane przed przekroczeniem swojego terminu d(ti) to dostajemy za nie
# nagrode g(ti) (pierwsze wybrane zadanie jest wykonywane w chwili 0, drugie
# w chwili 1, trzecie w chwili 2, itd).

# Prosze podac algorytm, ktory znajduje podzbior zadan, ktore mozna
# wykonac w terminie i ktory prowadzi do maksymalnego zysku. Prosze uzasadnic
# poprawnosc algorytmu


# Abdul Bari krulem

# each index in S represents unit time interval, e.g. index 0 is time from 0 to 1
# T[i] = (deadline_i, profit_i) then (deadline_i, profit_i, index)

def tasks(T):
    n = len(T)
    max_time = 0
    for i in range(n):
        max_time = max(max_time, T[i][0])
        T[i] = (T[i][0], T[i][1], i)
    T.sort(key=lambda x: x[1], reverse=True)
    S = [None] * max_time
    total_profit = 0
    for i in range(n):
        deadline, profit, index = T[i]
        while deadline-1 >= 0:
            if S[deadline-1] == None:
                S[deadline-1] = (T[i])
                total_profit += T[i][1]
                break
            else:
                deadline -= 1

    print("tasks in order:")
    for i in range(max_time):
        if S[i] != None:
            print("task with", S[i][2], "index,", S[i][1], "profit and", S[i][0], "deadline")
    print("--------------------------")
    print("Total profit:", total_profit)
    return total_profit


T1 = [(5, 8), (2, 2), (3, 3), (1, 1), (2, 4), (3, 8), (5, 1000), (5, 1000), (5, 1000), (5, 1000)]
T2 = [(2, 20), (2, 15), (1, 10), (3, 5), (3, 1)]

# tasks(T1)
# tasks(T2)
