class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = len(nums)

        dp = [1 for _ in range(n)]
        prev = [-1 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        max_len = max(dp)
        max_index = dp.index(max_len)

        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        result.reverse()
        return result


                




        



            


        