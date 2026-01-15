class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        low = 1 
        high =  sum(nums)

        def check(divisor):

            ans = 0

            for num in nums:
                ans += math.ceil(num / divisor)

            return ans
        

        while low <= high:
            mid = (low + high) // 2
            if check(mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low

        