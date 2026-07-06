class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:

        ans = []
        total = 0
        res = 0

        for i , num in enumerate(nums):
            s1 = str(num)
            d_range = int(max(s1)) - int(min(s1))
            res = max(res , d_range)
            ans.append(d_range)

        
        for i in range(len(nums)):
            if ans[i] == res:
                total += nums[i]

        return total

        

        


        