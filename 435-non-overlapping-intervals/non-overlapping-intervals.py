class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda item: item[1])

        prev_end = float("-inf")
        keep = 0

        for interval in intervals:
            if interval[0] >= prev_end:
                keep += 1
                prev_end = interval[1]

        return (len(intervals) - keep)

        

        
        