# SORTOWANIE STABLINE nlogn

# iter mergesort

def merge_sort(arr):
    n = len(arr)
    curr_len = 1
    while curr_len < n - 1:
        left = 0
        while left < n - 1:
            mid = min(left + curr_len - 1, n - 1)
            if left + 2 * curr_len - 1 < n - 1:
                right = left + 2 * curr_len - 1
            else:
                right = n - 1
            merge(arr, left, mid, right)
            left += curr_len * 2
        curr_len *= 2
    return arr


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    l_arr = [0] * n1
    r_arr = [0] * n2
    for i in range(0, n1):
        l_arr[i] = arr[left + i]
    for i in range(0, n2):
        r_arr[i] = arr[mid + i + 1]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if l_arr[i] > r_arr[j]:
            arr[k] = r_arr[j]
            j += 1
        else:
            arr[k] = l_arr[i]
            i += 1
        k += 1

    while i < n1:
        arr[k] = l_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r_arr[j]
        j += 1
        k += 1

# T = [1, 12, 42, 19, 24, 59, 23, 1, 5]
# merge_sort(T)
# print(T)

##########################################

# rekur mergesort

def mergesort(arr):
    n = len(arr)
    tmp_arr = [0 for _ in range(n)]
    return merge_sort_algo(arr, tmp_arr, 0, n - 1)


def merge_sort_algo(arr, tmp_arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_algo(arr, tmp_arr, left, mid)
        merge_sort_algo(arr, tmp_arr, mid + 1, right)
        merge(arr, tmp_arr, left, mid, right)
    return arr


def merge(arr, tmp_arr, left, mid, right):
    i = k = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp_arr[k] = arr[i]
            i += 1
        else:
            tmp_arr[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        tmp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        tmp_arr[k] = arr[j]
        j += 1
        k += 1

    for q in range(left, right + 1):
        arr[q] = tmp_arr[q]



T = [6,15,14,3,7,2]
mergesort(T)

###############################################

# recur mergesort

def merge_sort(t, tmp, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(t, tmp, l, mid)
        merge_sort(t, tmp, mid + 1, r)
        i = k = l
        j = mid + 1
        while i <= mid and j <= r:
            if t[i] <= t[j]:
                tmp[k] = t[i]
                i += 1
            else:
                tmp[k] = t[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = t[i]
            i += 1
            k += 1
        while j <= r:
            tmp[k] = t[j]
            j += 1
            k += 1
        for q in range(l, r + 1):
            t[q] = tmp[q]
    return t

def mergesort(t):
    n = len(t)
    tmp = [[0] for _ in range(n)]
    return merge_sort(t, tmp, 0, n - 1)


# T = [6,15,14,3,8,2]
# mergesort(T)
# print(T)