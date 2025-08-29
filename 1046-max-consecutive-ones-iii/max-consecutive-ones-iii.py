class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l,r = 0,0
        n = len(nums)
        max_len = 0
        zeroes = k
        

        while r < n:

            if nums[r] == 0:
                zeroes -= 1
            
            while zeroes < 0:
                if nums[l] == 0:
                    zeroes += 1
                l += 1
            
            max_len = max(max_len,r - l + 1)
            r += 1
        
        return max_len
                
            

            

                   


           





        