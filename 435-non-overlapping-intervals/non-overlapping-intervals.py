class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda item: item[1])

        n = len(intervals)

        prev_end = 0
        keep = 1

        for i in range(1,n):
            if intervals[i][0] >= intervals[prev_end][1]:
                keep += 1
                prev_end = i

        return (n - keep)

        

        
        