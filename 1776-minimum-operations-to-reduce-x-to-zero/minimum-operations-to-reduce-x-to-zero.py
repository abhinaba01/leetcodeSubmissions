class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        
        
        prefixSum = defaultdict(int)
        prefix = 0
        prefixSum[0] = 0
        n = len(nums)
        ans = math.inf
        a = [0] * (n + 1)

        for i in range(n):
            prefix += nums[i]
            prefixSum[prefix] = i + 1
            a[i+1] = prefix

        if prefix < x:
            return -1
        elif prefix == x:
            return n 
        
        sumSubArray = prefix - x
      

        for j in range(n+1):

            rem = a[j] - sumSubArray

            if rem in prefixSum:
           
                ans = min(n - (j - prefixSum[rem]) ,ans)

        
        return ans if ans != math.inf else -1



        