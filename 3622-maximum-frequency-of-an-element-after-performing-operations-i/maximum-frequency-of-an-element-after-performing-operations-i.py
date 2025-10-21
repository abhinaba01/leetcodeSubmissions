from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        n = len(nums)

        cnt = Counter(nums)
        res = float("-inf")


        def findLower(num):
            low,high = 0,n-1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= num:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        def findUpper(num):
            low,high = 0,n-1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= num:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

       
        nums.sort()
        minNum = nums[0]
        maxNum = nums[-1]

        

        for i in range(minNum,maxNum + 1):
            l = findLower(i-k)
            r = findUpper(i+k)
            ans = min(r - l + 1, numOperations+cnt[i])
            res = max(res,ans)
        
        return res


            


        