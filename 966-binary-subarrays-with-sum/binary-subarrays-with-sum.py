class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        n = len(nums)



        def atMost(k):

            l = 0
            total = 0
            count = 0

            for r in range(n):

                total += nums[r]
                while total > k and l <= r:
                    total -= nums[l]
                    l += 1
                
                count += (r - l + 1)

            return count

            
     
        return atMost(goal) - atMost(goal - 1)



            



            

        