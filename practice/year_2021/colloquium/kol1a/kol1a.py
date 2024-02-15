# Paweł Konop

from kol1atesty import runtests


def radix_string_sort(arr):
    # Sort strings by lengths (to improve the efficiency of
    # sorting strings by letters)
    max_len = longest_string_length(arr)
    _counting_sort_by_length(arr, max_len)
    # Allocate a temporary array once before sorting
    temp = [None] * len(arr)
    # Sort in a loop by the least significant digit
    for col_idx in range(max_len - 1, -1, -1):
        _counting_sort(arr, col_idx, temp)


def _counting_sort_by_length(arr, max_len):
    # Allocate memory for required temporary arrays
    counts = [0] * (max_len + 1)
    temp = [None] * len(arr)
    # Count strings with the same lengths
    for string in arr:
        counts[len(string)] += 1
    # Modify the counts array to indicate how many strings
    # are of a length not greater than the current string's length
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # Rewrite values to the temp sorted array
    for i in range(len(arr) - 1, -1, -1):
        counts[len(arr[i])] -= 1
        temp[counts[len(arr[i])]] = arr[i]
    # Rewrite sorted values to the initial array
    for i in range(len(temp)):
        arr[i] = temp[i]


def _counting_sort(arr, col_idx, temp):
    # Allocate memory for required temporary arrays
    counts = [0] * 26
    a_code = ord('a')
    # Count letters repetitions
    i = len(arr) - 1
    while col_idx < len(arr[i]) and i >= 0:
        counts[ord(arr[i][col_idx]) - a_code] += 1
        i -= 1
    prev_to_last_idx = i
    # Modify the counts array to indicate how many letters have
    # ascii codes lower than or equal to the current one
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # Rewrite values to the temporary array
    for i in range(len(arr) - 1, prev_to_last_idx, -1):
        letter_idx = ord(arr[i][col_idx]) - a_code
        temp[prev_to_last_idx + counts[letter_idx]] = arr[i]
        counts[letter_idx] -= 1
    # Rewrite sorted strings to the initial array
    for i in range(prev_to_last_idx + 1, len(temp)):
        arr[i] = temp[i]


def longest_string_length(arr):
    max_len = 0
    for string in arr:
        if len(string) > max_len:
            max_len = len(string)
    return max_len


def reverse_word(word):
    s = len(word)
    for i in range(s):
        if ord(word[i]) > ord(word[s-i-1]):
            word = word[::-1]
            break
        elif ord(word[i]) < ord(word[s-i-1]):
            break
    return word

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

def g(T):
    n = len(T)
    for i in range(n):
        T[i] = reverse_word(T[i])
    radix_string_sort(T)
    res = 0
    counter = 1
    for i in range(1, n):
        if T[i] == T[i-1]:
            counter += 1
            res = max(counter, res)
        else:
            counter = 1
    return res

runtests( g, all_tests=True )




