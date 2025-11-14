class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixSum = 0
        freq = defaultdict(int)
        freq[0] = 1
        c = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in freq:
                c += freq[prefixSum - k]
            
            freq[prefixSum] += 1
            
            
        return c


       