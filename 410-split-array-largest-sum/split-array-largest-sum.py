class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        low , high = max(nums) , sum(nums)

        def count(limit):

            cnt = 1 
            total = 0

            for el in nums:
                if total + el > limit:
                    cnt += 1
                    total = 0
                  
                total += el

            return cnt

        while low <= high:
            mid = low + (high - low) // 2
            if count(mid) > k:
                low = mid + 1

            else: 
                high = mid - 1
           

        return low



            

        

        