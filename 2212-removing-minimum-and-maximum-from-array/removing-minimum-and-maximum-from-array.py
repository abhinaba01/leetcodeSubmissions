class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n  = len(nums)

        max_idx = nums.index(max(nums))
        min_idx = nums.index(min(nums))

        l , r = 0 , 0

        if max_idx > min_idx:
            l , r = min_idx , max_idx
        
        else:

            l , r = max_idx , min_idx

        
        r = n -  r
        l = l + 1

        ans = min(l + r , n - r + 1 , n - l + 1)
        return ans
        