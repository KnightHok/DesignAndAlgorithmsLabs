# This problem is pseudopolynomial

# Subproblem - take all the cost that don't equal the current house paint cost and find the minimum

# Relation - dp[i][j] = costs[i][j] + min(dp[i-1][k] for k in range(numOfColors) if k != j)

# Topological Order - From left to right iterating over the houses

# Base - dp[0] = costs[0]

# Original - costToPaint(n)

# Time - O(n * m)

def costToPaint_iter(costs: [int]):

    # the h
    numOfHouses = len(costs)
    numOfColors = len(costs[0])

    
    dp = [[-1] * numOfColors for _ in range(numOfHouses)]
    dp[0] = costs[0]

    for i in range(len(dp)):
        for j in range(numOfColors):
            dp[i][j] = costs[i][j] + min(dp[i-1][k] for k in range(numOfColors) if k != j)

    min_cost = min(dp[numOfHouses-1])

    colors = []
    idxOfLastColor = 0

    # find index of min_cost
    for i in range(numOfColors):
        if dp[numOfHouses-1][i] == min_cost:
            idxOfLastColor = i
            print(i)
    colors.append(idxOfLastColor)

    for i in range(numOfHouses-2, -1, -1):
        found_color = min((dp[i][j], j) for j in range(numOfColors) if j != idxOfLastColor)[1]
        colors.append(found_color)
        # print(found_color)
        idxOfLastColor = found_color
    
    # reverse order
    colors = colors[::-1]

    # print(dp)
    return min_cost, colors

    print(dp)


if __name__ == "__main__":
    costs = [[8, 2, 4], [10, 4, 20], [6, 3, 4], [4, 8, 7]]

    print(costToPaint_iter(costs))