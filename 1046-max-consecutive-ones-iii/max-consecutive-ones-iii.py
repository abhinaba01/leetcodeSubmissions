class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l,r = 0,0
        maxLen = 0
        zeroes = 0
        

        while r < len(nums):
            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1

            if zeroes <= k:
                maxLen = max(maxLen,r - l + 1)
            r += 1
                


        return maxLen





            
        

        
       
    
            




    
        