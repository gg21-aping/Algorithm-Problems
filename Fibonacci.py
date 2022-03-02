# time complexity O(n), space complexity O(n)
def cache(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = cache(n-1) + cache(n-2)
    return memo[n]

# time complexity O(n), space complexity O(1)
def bottomUp(n):
    if n <= 1: return n
    prepre, pre = 0, 1
    for i in range(1, n):
        f = prepre + pre
        prepre, pre = pre, f
    return pre

# test case
# 1, 1, 2, 3, 5
print(cache(5))
print(bottomUp(5))
