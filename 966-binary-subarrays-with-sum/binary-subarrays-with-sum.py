class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def atMost(k):

            if k < 0:
                return 0   # no subarrays can have sum <= -1

            l,r = 0,0
            n = len(nums)
            count = 0

            target = 0

            while r < n:

                target += nums[r]
                while target > k:
                    target -= nums[l]
                    l += 1
                
                count  += (r-l+1)
                
                r += 1
            return count
            
        return atMost(goal) - atMost(goal - 1)

       