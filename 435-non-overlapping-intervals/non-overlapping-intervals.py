class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:x[1])
        L = len(intervals)

        prev = intervals[0][1]
        cnt = 1
        for start,end in intervals:
            if start >= prev:
                cnt += 1
                prev = end
        
        return L - cnt

            


        