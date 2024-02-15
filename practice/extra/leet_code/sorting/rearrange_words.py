# Given a sentence text (A sentence is a string of space-separated words) in the following format:
#
# First letter is in upper case.
# Each word in text are separated by a single space.
# Your task is to rearrange the words in text such that all words are rearranged in an increasing order of
# their lengths. If two words have the same length, arrange them in their original order.
#
# Return the new text following the format shown above.


def heapify(T, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and T[m][1] < T[l][1]: m = l
    if r < n and T[m][1] < T[r][1]: m = r
    if m != i:
        T[m], T[i] = T[i], T[m]
        heapify(T, n, m)

def parent(i):
    return (i-1)//2

def buildheap(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, n, i)

def modify(text):
    arr = text.split()
    n = len(arr)
    for word in arr:
        for letter in word:
            letter = letter.lower()

    return arr

def rearrange(text):
    T = modify(text)
    n = len(T)
    for i in range(n):
        T[i] = (T[i], len(T[i]))
    buildheap(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)
    res = ''
    for i in range(n):
        res += T[i][0]
        res += ' '
    return res

text = "To be or not to be"

# print(rearrange(text))