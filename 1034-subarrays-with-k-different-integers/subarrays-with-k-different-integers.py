class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(m):

            l , r = 0 , 0
            n = len(nums)
            unique, count = 0 , 0
            freq = {}

            while r < n:

                if freq.get(nums[r],0) == 0:
                    unique += 1
                freq[nums[r]] = freq.get(nums[r],0) + 1
                

                while unique > m:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        unique -= 1
                    l += 1
                
                count += (r - l + 1)
                r += 1
            
            
            return count
        
        return atMost(k) - atMost(k - 1)
