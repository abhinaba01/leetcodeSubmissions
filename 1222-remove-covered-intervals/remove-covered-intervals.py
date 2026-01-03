class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: (x[0],-x[1]))
        n = len(intervals)
        cnt = 0
        prev = -math.inf

        for start , end in intervals:
            if end <= prev:
                cnt += 1
            else:
                prev = end

        return n - cnt
        

      

       
        