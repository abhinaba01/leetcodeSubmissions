class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        prefix = defaultdict(int)
        ans = float("-inf")
        total =  0

        for num in nums:
            
            total += num
            ans = max(ans,total)

            if total < 0:
                total = 0

        
        return ans

            
        