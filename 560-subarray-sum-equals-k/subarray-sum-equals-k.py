class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        N = len(nums)
        
        total = 0
        cnt = 0

        for  i in range(N):
            total += nums[i]
       
            cnt += prefixSum[total - k]
            
            prefixSum[total] += 1

        
      
        return cnt
        

        

        