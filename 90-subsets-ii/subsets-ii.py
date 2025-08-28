class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        nums.sort()

        def subsetHelper(i):

            if i >= n:
    
                ans.append(path[:])
                return

            path.append(nums[i])
            subsetHelper(i+1)
            path.pop()

            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            subsetHelper(i+1)
        
        subsetHelper(0)
        return ans

        