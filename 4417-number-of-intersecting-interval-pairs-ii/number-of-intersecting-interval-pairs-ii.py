class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:

        intervals.sort(key = lambda x : x[0])
        n = len(intervals)
        cnt = 0

        for i in range(n):

            start , end = intervals[i][0], intervals[i][1]

            idx = bisect.bisect_right(intervals, end , key=lambda x: x[0])
            cnt += (idx - i - 1)


        return cnt

           
            
        