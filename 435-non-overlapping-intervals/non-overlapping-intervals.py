class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda item: item[1])

        present = float("-inf")
        cnt = 0

        for interval in intervals:
            if interval[0] >= present:
                cnt += 1
                present = interval[1]

        return (len(intervals) - cnt)

        

        
        