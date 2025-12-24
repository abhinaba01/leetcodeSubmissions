class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        days = defaultdict(list)

        n = len(jobDifficulty)


        if n < d:
            return -1

        @cache
        def rec(i,j,curr_max):

            if i == n:
                if j == d:
                    return curr_max
                if j != d:
                    return float("inf")

          

            curr_max = max(curr_max,jobDifficulty[i])
            return min(rec(i+1,j,curr_max),curr_max + rec(i+1,j+1,0))
        
        return rec(0,0,0)

        



           