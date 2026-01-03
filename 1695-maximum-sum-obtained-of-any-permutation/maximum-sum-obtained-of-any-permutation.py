class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        diff = defaultdict(int)
        n = len(nums)
        pop = [0] * n
        MOD = 10 ** 9 + 7

        for start ,end in requests:
            diff[start] += 1
            diff[end+1] -= 1

        curr = 0
        for i in range(n):
            curr += diff[i]
            pop[i] += curr
        
        pop.sort()
        nums.sort()
        s = 0

        for i in range(n):
            s = (s + pop[i] * nums[i]) % MOD

        return s

    


        