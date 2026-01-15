class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        low , high = 0 , n - 1

        while low <= high:

            mid = low + (high - low ) // 2
            print(mid)
            if nums[mid] == target or (nums[mid] > target and nums[mid - 1] < target):
                return mid
            else:
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

        return low
        
          