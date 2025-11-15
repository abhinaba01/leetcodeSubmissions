class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)

        prefixSum = 0
        maxSum = float("-inf")

        for i in range(n):
            prefixSum += nums[i]
            maxSum = max(maxSum,prefixSum)
            if prefixSum < 0:
                prefixSum = 0
           
        
        return maxSum
            

        


        

        