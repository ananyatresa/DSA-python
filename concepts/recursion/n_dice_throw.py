#  DP approach using a DP table to track the count of sum for each n at each target.
#  DP - cols are 0 to target + 1  and rows are 0 to n + 1
# here target and n range from to n+1 and target+1 . (+1 - To have a base row for calculating previous)
def dice_throw(n, k, target):
    MOD = 10**9 + 7
    dp = [[0] * target + 1 for _ in range(n)]
    dp[0][0] = 1 # for 0 dice to get 0 sum, there is no way so its set to 1

    for d in range(1,n+1):
        for t in range(1, target +1):
            for i in range(1, k+1):
                if t-i >=0:
                    dp[d][t] = (dp[d][t] + dp[d-1][t-i]) % MOD

    return dp[n][target]