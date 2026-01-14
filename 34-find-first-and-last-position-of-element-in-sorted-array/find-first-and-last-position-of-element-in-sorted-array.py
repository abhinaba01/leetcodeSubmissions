class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
            

        
        left = high + 1
       
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
            

        
        right = low - 1
     

        if left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]

           
           
       





        
            
                

            
        