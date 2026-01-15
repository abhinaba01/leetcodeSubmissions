class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return 0

        low , high = 0 , n - 1


        while low <= high:
            
            mid = low + (high - low) // 2
            print(low,mid,high)
            before = -math.inf if mid <= 0 else nums[mid - 1]
            after = -math.inf if mid >= n - 1 else nums[mid + 1]
            if before < nums[mid] and nums[mid] > after:
                return mid
            else:
                if before <= nums[mid] <= after:
                    low = mid + 1
                else:
                    high = mid - 1

            
        
    

        