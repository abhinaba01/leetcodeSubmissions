class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:


        P = 911383322
        MOD = 10 ** 18 + 3

        res = []

        n = len(nums)
        m = len(pattern)

        cnt = 0

        h = 0
        
        h1 = 0


        POW = pow(P,m - 1,MOD)


        for i in range(m):
            
            h1 = (h1 * P + pattern[i])  % MOD 

        for i in range(1,m+1):

            if nums[i] > nums[i-1]:
                var = 1
            elif nums[i] == nums[i-1]:
                var = 0
            else:
                var = -1 

            h = (h * P + var)  % MOD 

        if h == h1:
            cnt += 1



        for i in range(m+1,n):
            
            if nums[i-m] > nums[i-m-1]:
                x = 1
            
            if nums[i-m] == nums[i-m-1]:
                x = 0
            
            if nums[i-m] < nums[i-m-1]:
                x = -1
            
                

            h = (h - x * POW) % MOD



            if nums[i] > nums[i-1]:
                var = 1
            elif nums[i] == nums[i-1]:
                var = 0
            else:
                var = -1 

            h = (h * P + var)  % MOD 
            

            if h == h1:
                cnt += 1

            
        
        return cnt




                



        
        