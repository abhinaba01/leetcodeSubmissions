class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = float("-inf")
        n = len(nums)
        pref = 1
        suff = 1
        maxProd = float("-inf")
        for i in range(n):
          

            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1

            pref = pref * nums[i]
            suff = suff * nums[n-1-i]
            maxProd = max(maxProd,max(pref,suff))

        return maxProd

        