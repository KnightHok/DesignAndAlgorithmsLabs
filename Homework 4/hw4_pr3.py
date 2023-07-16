# Subproblem 
# find the size of the largest square that can be formed at that position,
# considering only α's

# Recurrence
# dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1, if matrix[i][j] == 'α'
# dp[i][j] = 0, if matrix[i][j] == 'ω'

# Topological Order
# The topological order for solving the subproblems is from left to right and top
# to bottom, iterating through the positions in the matrix row by row

# Base
# The base case is when the position (i, j) is at the first row or the first column.
# In this case, the size of the largest square at that position will be 1 if it
# contains α and 0 if it contains ω.

# Original Probelm
# largestAlphaArea(costs)

# Time
# O(n * m)

def largestAlphaSquareArea(matrix):
    n = len(matrix)
    if n == 0:
        return 0
    m = len(matrix[0])

    dp = [[0] * m for _ in range(n)]

    # Initialize the first row and first column
    for i in range(n):
        dp[i][0] = int(matrix[i][0] == 'α')
    for j in range(m):
        dp[0][j] = int(matrix[0][j] == 'α')

    max_area = max(dp[0])  # Initialize the maximum area

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 'α':
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_area = max(max_area, dp[i][j])

    return max_area ** 2


if __name__ == "__main__":
    matrix =  [["a","w","a","w","w"], ["a","w","a","a","a"],
["a","a","a","a","a"], ["a","w","w","a","w"]]
    
    print(largestAlphaSquareArea(matrix))
    