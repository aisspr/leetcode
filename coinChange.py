def coinChange(self, coins: List[int], amount: int) -> int:
    #val of each pos is the min num of coins to get to the target which is the index of dp
    dp = [amount+1]*(amount+1)  #+1 because 0 indexing
    dp[0] = 0

    for i in range(1, amount+1): 
        for coin in coins: 
            if coin <= i: 
                dp[i] = min(dp[i], 1+dp[i-coin])
    return dp[amount] if dp[amount] != amount+1 else -1