# Pokrycie przedzialami jednostkowymi

# Dany jst zbior punktow X = {x1, ..., xn} na prostej.
# Prosze podac algorytm, ktory znajduje minimalna liczbe przedzialow
# jednostkowych domknietych, potrzebnych do pokrycia wszystkich punktow
# z X. (Przyklad: Jesli X = {0.25, 0.5, 1.6} to potrzeba dwoch przedzialow
# np. [0.2, 1.2] oraz [1.4, 2.4]

def unit_intervals(T):
    n = len(T)
    T.sort()
    intervals = []
    i = 0
    while i < n:
        interval = [T[i], T[i]+1]
        intervals.append(interval)
        while i < n and interval[0] <= T[i] and T[i] <= interval[1]:
            i += 1

    print("required", len(intervals), "unit intervals >>>", intervals)
    return len(intervals)

T = [0.25, 0.5, 1.6]
unit_intervals(T)