# longest increasing subsequence using binary search nlogn

def bin_search1(T, res_arr, b, e, value):
    if T[res_arr[0]] > value: return 0
    if T[res_arr[b]] < value and T[res_arr[b+1]] > value:
        return b+1
    mid = (b+e)//2
    if T[res_arr[mid]] > value:
        return bin_search1(T, res_arr, b, mid-1, value)
    else:
        return bin_search1(T, res_arr, mid, e, value)

def get_solution1(T, parents, i):
    if parents[i] == -1: return [T[i]]
    return [T[i]] + get_solution1(T, parents, parents[i])

def my_lis(T):
    n = len(T)
    res = []
    parents = [-1] * n
    res.append(0)
    res_pointer = 0
    for i in range(1, n):
        if T[i] > T[res[res_pointer]]:
            res.append(i)
            res_pointer += 1
            parents[i] = res[res_pointer-1]
        else:
            x = bin_search1(T, res, 0, len(res)-1, T[i])
            res[x] = i
            if x == 0: continue
            else: parents[i] = res[x-1]

    return(get_solution1(T, parents, res[len(res)-1])[::-1])


T = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10, 100, -10, -20]
# print(lis(T))

# albo inny lis nlogn

from bisect import bisect_left

def lis(arr):

    longest, res = [], []

    for x in arr:
        if not res or longest[-1] < x:
            longest.append(x)
            res.append(len(longest))
        else:
            idx = bisect_left(longest, x)
            longest[idx] = x
            res.append(idx + 1)

    return longest, res

def find_lis(arr):
    return lis(arr)

def find_lds(arr):

    longest, res = lis(arr[::-1])
    return longest[::-1], res[::-1]


nums = [9, 8, 1, 7, 6, 5, 4, 3, 2, 1]

# print(*find_lis(nums), sep='\n')
# print("")
# print(*find_lds(nums), sep='\n')

