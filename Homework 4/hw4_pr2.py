# Subproblem 
# For a given house i, find the minimum cost to paint the first i houses.

# Recurrence
# dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
# dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
# dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

# Topological Order
# From left to right

# Base
# The base case is when there is only one house.
# In this case, the minimum cost is the cost of painting that house with each color.

# Original Probelm
# minCostTD(costs)

# Time
# O(n)


def minCostTD(costs):
    dp = [0, 0, 0]
    
    for i in range(len(costs)):
        dp0 = costs[i][0] + min(dp[1], dp[2])
        dp1 = costs[i][1] + min(dp[0], dp[2])
        dp2 = costs[i][2] + min(dp[0], dp[1])
        dp = [dp0, dp1, dp2]
        
        
    return min(dp)

def minCostBU(costs):
    n = len(costs)
    if n == 0:
        return 0

    dp = [[0] * 3 for _ in range(n)]

    dp[0] = costs[0]

    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

    return min(dp[n-1])

if __name__ == "__main__":
    costs = [[17, 2, 17], [8, 4, 10], [6, 3, 19], [4, 8, 12]]
    print(f"Top-Down: {minCostTD(costs)}")
    print(f"Bottom-Up: {minCostBU(costs)}")