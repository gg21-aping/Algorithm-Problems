# From n choose k.
# example: C(8,6) = 8! / (6! * (8-6)!) = 28

# recursive: time  = space = O(n * max(k, n-k))
def recursive(n, k):
    # base case
    # C(n,0) == C(n,n) == 1
    if k > n: return 0
    if k == n or k == 0: return 1
    # recursive call 
    # C(n, k) = C(n-1, k-1) + C(n-1, k)
    return recursive(n-1, k-1) + recursive(n-1, k)

# top-down memoization dp: time O(max(n, n-k)), space O(n*k)
def memoization(n, k):
    memo = [[-1 for x in range(k+1)] for y in range(n+1)]
    def dp(n, k):
        # base case
        if memo[n][k] != -1: return memo[n][k]
        if k == 0 or k == n:
            memo[n][k] = 1
            return memo[n][k]
        
        memo[n][k] = dp(n-1, k) + dp(n-1, k-1)
        return memo[n][k]
    return dp(n, k)


# test case
print(recursive(8, 6))
print(memoization(8, 6))