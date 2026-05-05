class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        n = len(stones)

        if (n - 1) % (k - 1) != 0:
            return -1

        
        cost = defaultdict(int)
        cost[-1] = 0
        total = 0

        for i in range(n):
            total += stones[i]
            cost[i] = total


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
                    ans += (cost[j] - cost[i - 1])

              

            dp[i][j] = ans
            return dp[i][j]

        return merge(0,n - 1)


        

            
