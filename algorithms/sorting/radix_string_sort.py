def radix_string_sort(arr):
    max_len = longest_string_length(arr)
    _counting_sort_by_length(arr, max_len)
    temp = [None] * len(arr)
    for col_idx in range(max_len - 1, -1, -1):
        _counting_sort(arr, col_idx, temp)


def _counting_sort_by_length(arr, max_len):
    counts = [0] * (max_len + 1)
    temp = [None] * len(arr)
    for string in arr:
        counts[len(string)] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        counts[len(arr[i])] -= 1
        temp[counts[len(arr[i])]] = arr[i]
    for i in range(len(temp)):
        arr[i] = temp[i]


def _counting_sort(arr, col_idx, temp):
    counts = [0] * 26
    a_code = ord('a')
    i = len(arr) - 1
    while col_idx < len(arr[i]) and i >= 0:
        counts[ord(arr[i][col_idx]) - a_code] += 1
        i -= 1
    prev_to_last_idx = i
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    for i in range(len(arr) - 1, prev_to_last_idx, -1):
        letter_idx = ord(arr[i][col_idx]) - a_code
        temp[prev_to_last_idx + counts[letter_idx]] = arr[i]
        counts[letter_idx] -= 1
    for i in range(prev_to_last_idx + 1, len(temp)):
        arr[i] = temp[i]


def longest_string_length(arr):
    max_len = 0
    for string in arr:
        if len(string) > max_len:
            max_len = len(string)
    return max_len

