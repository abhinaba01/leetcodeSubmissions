class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

       

        def atMost(limit):

            odd = 0
            l = 0
            n = len(nums)
            count = 0

            for r in range(n):
                if nums[r] % 2 != 0:
                    odd += 1
                
                while odd > limit:
                    if nums[l] % 2 != 0:
                        odd -= 1
                    
                    l += 1

                count += (r - l + 1)

            
            return count

        return atMost(k) - atMost(k-1)
        