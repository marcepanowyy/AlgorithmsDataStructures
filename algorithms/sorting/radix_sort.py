# Sortowanie pozycyjne
# przydaje sie przy sortowaniu slow

# kra   kra   kil   art
# art   ati   kit   ati
# kot-> kil-> kot-> kil
# kit   art   kra   kit
# ati   kot   art   kot
# kil   kit   ati   kra

from random import randint

def radix_sort(arr):
    maximum = max(arr)
    div = 1
    while maximum // div != 0:
        counting_sort(arr, div)
        div *= 10
    return arr

def counting_sort(arr, div):
    n = len(arr)
    c_arr = [0] * 10
    output = [0] * n

    for i in range(n):
        index = (arr[i] // div) % 10
        c_arr[index] += 1

    for i in range(1, 10):
        c_arr[i] += c_arr[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // div) % 10
        output[c_arr[index] - 1] = arr[i]
        c_arr[index] -= 1

    for i in range(n):
        arr[i] = output[i]

T = [1, 52, 599, 24, 511, 42]
radix_sort(T)
# print(T)



