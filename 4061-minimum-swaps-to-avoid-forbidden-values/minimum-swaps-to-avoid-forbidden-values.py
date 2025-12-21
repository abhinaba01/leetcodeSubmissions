from collections import Counter
class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:

        freq_nums = Counter(nums)
        freq_forb = Counter(forbidden)
        n  = len(nums)
        badIndices = 0
        mismatch = defaultdict(int)

        for num in freq_nums:
            if freq_nums[num] + freq_forb[num] > n:
                return -1
        
        for i in range(n):
            if nums[i] == forbidden[i]:
                badIndices += 1
                mismatch[nums[i]] += 1
        
        f = max(mismatch.values()) if len(mismatch) > 0 else 0 

        return max(f,math.ceil(badIndices / 2))


        
        


      

        