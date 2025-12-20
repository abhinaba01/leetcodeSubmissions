class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

      

        dp = [0] * (amount+1)
        if amount == 0:
            return 1
        if 0 < amount < min(coins):
            return 0
       
        dp[0] = 1

      
        for coin in coins:
            for i in range(1,amount+1):
                
                if coin <= i:
                    dp[i] += dp[i-coin]
        
        return dp[amount] 
            
          


        