# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1

# Input: s = "abc"
# Output: 3
# Explanation: Three
# palindromic strings: "a", "b", "c".

# Example 2

# Input: s = "aaa"
# Output: 6
# Explanation: Six
# palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

def get_odd(str):
    odd = []
    n = len(str)
    for i in range(n):
        odd.append(str[i])
        left, right = i-1, i+1
        while left >= 0 and right < n and str[left] == str[right]:
            odd.append(str[left:right+1])
            left -= 1
            right += 1
    return odd

def get_even(str):
    even = []
    n = len(str)
    for i in range(1, n):
        left, right = i-1, i
        while left >= 0 and right < n and str[left] == str[right]:
            even.append(str[left:right+1])
            left -= 1
            right += 1
    return even

def get_solution(str):
    res = []
    res += get_odd(str)
    res += get_even(str)
    return res, len(res)


# str = 'aaaaaabdadadddaa'
# print(get_solution(str))