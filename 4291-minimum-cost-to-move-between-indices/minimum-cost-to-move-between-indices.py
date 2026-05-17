class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        n = len(nums)

        cost = [0] * n
        cost[0] = 1
        cost[n-1] = n - 2

        for i in range(1,n - 1):
            left = abs(nums[i-1] - nums[i]) 
            right = abs(nums[i+1] - nums[i])

            if left <= right:
                cost[i] = i - 1
            else:
                cost[i] = i + 1

        prefix = [0] * (n)
        suffix = [0] * (n)
        for i in range(1,n):

            prefix[i] = prefix[i-1] + ( 1 if cost[i-1] == i else abs(nums[i] - nums[i-1]))

        for i in range(n - 2, - 1, -1):

            suffix[i] = suffix[i+1] + (1 if cost[i+1] == i else abs(nums[i] - nums[i+1]))








        # def f(u,v,s):

        #     if u == v:
        #         return 0
            
            
        #     if cost[u] == u + s:
        #         return 1 + f(u+s,v,s)
        #     else:
        #         return abs(nums[u+s] - nums[u]) + f(u+s,v,s)
          
        print(prefix)
        print(suffix)


        res = []
        for start , end in queries:

            # sign = 1
            # if start > end:
            #     sign = -1

            # val =  f(start,end,sign)
            if end > start:
                val = abs(prefix[end] - prefix[start])
            else:
                val = abs(suffix[end] - suffix[start])




            res.append(val)

        return res
        