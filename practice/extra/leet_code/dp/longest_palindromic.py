# Given a string s, return the longest palindromic substring in s.

def check_odd(w, i, res):
    n = len(w)
    b, e = i, i
    while b >= 0 and e <= n-1 and w[b] == w[e]:
        if e-b+1 > len(res):
            res = w[b:e+1]
        b -= 1
        e += 1
    return res

word = 'abcba'
check_odd(word, 2, '')

def check_even(w, i, res):
    n = len(w)
    b, e = i, i+1
    while b >= 0 and e <= n-1 and w[b] == w[e]:
        if e-b+1 > len(res):
            res = w[b:e+1]
        b -= 1
        e += 1
    return res

def LPD(w):
    n = len(w)
    res = ''
    for i in range(n):
        res = check_odd(w, i, res)
        res = check_even(w, i, res)
    return res

w1 = 'abccba'
w2 = 'senkjuuj'
w3 = 'abbbbsssssdwwewqws'

# print(LPD(w1))
# print(LPD(w2))
# print(LPD(w3))