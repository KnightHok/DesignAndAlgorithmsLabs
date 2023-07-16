# Subproblem 
# Determine the maximum number of rounds the player can win.

# Recurrence
# dp[i] = 1 + max(dp[i+1], dp[i+2])

# Topological Order
# Starting from the last round and moving towards the first round.

# Base
# The base case is when the last round is reached and there are fewer than 5 cards
# remaining in the deck. In this case, the maximum number of rounds the player can
# win is 0, as a new round cannot be played.

# Original Problem
# Find the maximum number of rounds the player can win in the game 21,
# given a deck of n cards with a known order.

# Time
# O(n)


def minCostForPainting(costs):
    n = len(costs)
        

if __name__ == "__main__":
    costs = [[17, 2, 17], [8, 4, 10], [6, 3, 19], [4, 8, 12]]
    min_cost = minCost(costs)
    print(min_cost)





