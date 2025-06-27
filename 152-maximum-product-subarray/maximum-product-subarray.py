class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProd = float("-inf")
        n = len(nums)
        pref , suff = 1 , 1
        for i in range(n):
          

            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1

            pref = pref * nums[i]
            suff = suff * nums[n-1-i]
            maxProd = max(maxProd,max(pref,suff))

        return maxProd

        