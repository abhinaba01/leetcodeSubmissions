class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

       

       
        l = 0
        
        nums.sort()
        n = len(nums)

        cnt = 0
        prev = nums[0]
        ans = 1
        for r in range(1,n):

            cnt += (nums[r] - prev) * (r - l)
            prev = nums[r]

            while cnt > k and l < n:
                cnt -= (nums[r] - nums[l])
                l += 1

            
            ans = max(ans , r - l + 1 )

        return ans






            
    