# SRTBOT

# Subproblem - Using a substrings approach G(i, j, p) where i <= j and p 
# is me

# Relation - if V = current value then
#  G(i, j, me) = max{
#                   V1 + G(i+1, j, you),
#                   V1 + G(i, j+1, you)
#   }
#   G(i, j, you) = min{
#                   G(i+1, j, me),
#                   G(i, j+1, me)
#   }

# Toplogical Order - Increasing length of substrings

# Base Case - If I get the last coin
# G(i, i, me) = 1
# If you get the last coin
# G(i, i, you) = 0

# Order
#   if n = 
#   X(0, n, )
# if my total <= 21 && greater than dealer
def max_rounds(deck):
    n = len(deck)

    dp = [[-1] * 22 for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n-1, -1, -1):
        for j in range(22)


    return max_rounds

if __name__ == "__main__":
    print(max_rounds([1, 1, 1, 8, 10, 3, 5, 3, 2, 4, 2]))
