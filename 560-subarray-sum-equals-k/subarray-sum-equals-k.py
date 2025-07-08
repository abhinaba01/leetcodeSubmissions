class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum , sum ,count= {},0,0
        prefixSum[0] = 1
        for i in range(len(nums)):
            sum+=nums[i]
            rem = sum - k
            if  rem in prefixSum:
                count+=prefixSum[rem]

            prefixSum[sum] = prefixSum.get(sum, 0) + 1
        return count
               

        