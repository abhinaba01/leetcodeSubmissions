class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []
        nums.sort()

        for i in range(1 << n):

            ans = []
            valid = True  

            for k in range(n):

                if i & (1 << k):

                    if k > 0 and nums[k] == nums[k - 1] and not (i & (1 << (k - 1))):
                        valid = False
                        break  

                    ans.append(nums[k])

            if valid:
                result.append(ans)

        return result