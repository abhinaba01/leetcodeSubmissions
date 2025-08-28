class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def subsetHelper(i):

            if i >= n:
                if sorted(path) not in ans:
                   ans.append(sorted(path[:]))
                return

            subsetHelper(i+1)
            path.append(nums[i])
            subsetHelper(i+1)
            path.pop()
        
        subsetHelper(0)
        return ans

        