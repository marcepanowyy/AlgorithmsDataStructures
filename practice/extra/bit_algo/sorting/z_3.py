# Dana jest tablica z n liczbami calkowitymi. Zawiera ona duzo powtorzen
# co wiecej zaldwie Ologn liczb jest unikatowe. Napisz algorytm, ktory
# w czasie O(nlog(logn)) posortuje taka tablice

# implementacja tablicy o dlugosci sufit logn
# wypelniamy nonami

import math
from math import *

def sort(T):
    n = len(T)
    T = [None] * (ceil(math.log(n)))

def index(tab, val): #zwraca indeks w tablicy pod ktorym znajduje sie val

def insert(tab):

def find(tab, val):  # return bool
# czy dany element jest w tablicy


def sort(T):
    P = []
    for i in T:
        if not find(P, i):
            insert(P, i)

    licznik = [0 for i in P]
    for i in T:
        licznik[index(P, i)] += 1

    # for i in range(1, len(licznik)):
    #     licznik[i] += licznik[i-1]
    iter =0
    for i in range(len(P)):
        while licznik[i] != 0:
            licznik[i] -=1
            T[iter] = P[i]
            iter += 1
    return T




