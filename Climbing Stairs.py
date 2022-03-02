# You are climbing stairs and you can advance 1 to k steps at a time.
# The destination is n steps up.

def climbStairs(n, k):
    def ways(step):
        # base case
        if step <= 1: return 1
        
        if dp[step] == 0:
            dp[step] = sum(ways(step - i) for i in range(1, min(k, step) + 1))
        
        return dp[step]

    dp = [0] * (n+1)
    return ways(n)

# test case
print(climbStairs(4,2))
