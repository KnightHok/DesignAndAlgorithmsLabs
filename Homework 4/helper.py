def top_down(cards):
    n = len(cards)
    memo = [[-1 for _ in range(n)] for _ in range(n)]
    return recursive(cards, 0, n-1, memo)

def recursive(cards, start, end, memo):
    if start > end:
        return 0
    
    if memo[start][end] != -1:
        return memo[start][end]
    
    # Dealer draws two cards
    dealer_sum = cards[start] + cards[start + 1]
    
    # Player draws two cards
    player_sum1 = cards[start + 2] + cards[start + 3]
    
    # Player draws additional card
    if start + 4 <= end:
        player_sum2 = cards[start + 2] + cards[start + 3] + cards[start + 4]
        player_draw = recursive(cards, start + 5, end, memo)
    else:
        player_sum2 = player_sum1
        player_draw = 0
    
    # Compare the sums
    if player_sum1 <= 21 and player_sum1 > dealer_sum:
        win_round1 = 1 + recursive(cards, start + 4, end, memo)
    else:
        win_round1 = 0
    
    if player_sum2 <= 21 and player_sum2 > dealer_sum:
        win_round2 = 1 + player_draw
    else:
        win_round2 = 0
    
    # Store the maximum number of rounds won in the memo
    memo[start][end] = max(win_round1, win_round2)
    
    return memo[start][end]

def minCost(costs):
    dp = [0, 0, 0]
    
    for i in range(len(costs)):
        dp0 = costs[i][0] + min(dp[1], dp[2])
        dp1 = costs[i][1] + min(dp[0], dp[2])
        dp2 = costs[i][2] + min(dp[0], dp[1])
        dp = [dp0, dp1, dp2]
        
    return min(dp)



if __name__ == "__main__":
    print(top_down([1, 1, 1, 8, 10, 3, 5, 3, 2, 4, 2]))