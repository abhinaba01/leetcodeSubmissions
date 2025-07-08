class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefixSum = {}
        sum = 0
        cnt = 0

        prefixSum[0] = 1

        for i in range(len(nums)):
            sum += nums[i]

            rem = sum - goal

            if rem in prefixSum:
                cnt += prefixSum[rem]

            prefixSum[sum] = prefixSum.get(sum,0) + 1
        return cnt
        


    
       
        