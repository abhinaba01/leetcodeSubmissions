class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        
        prefix = [0] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]

        
        def cost(i,j):
            return prefix[j+1] - prefix[i]
        


        dp = [[-1] * n for _ in range(n)]

        
        def merge(i,j):

            if i == j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            ans = float("inf")


            for x in range(i,j,k-1):

                ans = min(ans , merge(i,x) + merge(x+1,j))

            if (j -i ) % (k - 1) == 0:
                    ans += cost(i,j)

              

            dp[i][j] = ans
            return dp[i][j]

        return merge(0,n - 1)


        

            
