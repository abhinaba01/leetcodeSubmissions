class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        nums.sort()

        diff = nums[-1] - nums[0]

        n = len(nums)


        def f(val):

            cnt = 0

            l = 0

            for r in range(n):

                while nums[r] - nums[l] > val:
                    l += 1

                
                cnt += (r - l)


               

            
            return cnt >= k



            



        low , high = 0 , diff

        ans = -1

        while low <= high:
            mid = low + (high - low) // 2
            if f(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        

        

        