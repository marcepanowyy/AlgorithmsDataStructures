# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k
# bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# O(nlogn)

from math import ceil

def koko_bananas(piles, h):

    b, e = 1, max(piles)

    while b <= e:
        speed = (b+e)//2
        if check(speed, piles, h):
            e = speed-1
        else:
            b = speed+1

    return b

def check(speed, piles, h):

    actual_time = 0

    for pile in piles:
        actual_time += ceil(pile / speed)

    if actual_time <= h: return True
    return False


piles1 = [3, 6, 7, 11]
h1 = 8
# Expected: 4

piles2 = [30,11,23,4,20]
h2 = 5
# Expected: 30

piles3 = [30,11,23,4,20]
h3 = 6
# Expected: 23

# print(koko_bananas(piles1, h1))
# print(koko_bananas(piles2, h2))
# print(koko_bananas(piles3, h3))


def ceil_(n):
    res = int(n)
    return res if res == n or n < 0 else res+1

def floor_(n):
    res = int(n)
    return res if res == n or n >= 0 else res-1

