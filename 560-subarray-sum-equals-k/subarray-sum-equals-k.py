class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixSum = {}
        n = len(nums)
        prefixSum[0] = 1
        preSum = 0
        count = 0

        for i in range(n):
            preSum += nums[i]

            if preSum - k in prefixSum:
                count += prefixSum[preSum - k]
            
            prefixSum[preSum] = prefixSum.get(preSum,0) + 1
        return count

       

        