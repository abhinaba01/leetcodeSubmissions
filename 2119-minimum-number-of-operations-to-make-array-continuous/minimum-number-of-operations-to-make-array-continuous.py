class Solution:
    def minOperations(self, nums: List[int]) -> int:


        new_nums = list(set(nums))

        new_nums.sort()

        diff = len(new_nums) - len(nums)

        n = len(new_nums)

        j = 0
        
        ans = math.inf

        for i in range(n):

            while j < n and (new_nums[j] - new_nums[i]) < len(nums) :
                j += 1

            


            ans = min(ans , len(nums)  - j + i)
        
        return ans 

           







                