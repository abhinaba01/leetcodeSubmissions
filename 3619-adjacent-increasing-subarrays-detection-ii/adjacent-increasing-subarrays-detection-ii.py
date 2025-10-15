class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        n = len(nums)

        inc = [1] * n

        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                inc[i] = inc[i+1] + 1
            

        def findLargestK(k):
        
            for i in range(n-2*k+1):

                if inc[i] >= k and inc[i+k] >= k:
                    return True
                
            return False
        


        low,high = 1,n//2
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if findLargestK(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

               




        