class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        nums,z = sorted(nums),Counter(nums)
        return max(max(min(bisect_right(nums,v+k)-bisect_left(nums,v-k)-z[v],numOperations)+z[v],
            min(bisect_right(nums,v+2*k)-i,numOperations)) for i,v in enumerate(nums))




        