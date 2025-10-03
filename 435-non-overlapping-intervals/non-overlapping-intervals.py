class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        
        intervals.sort(key=lambda x: x[1])
        
        merged = []
        count = 0
        
        for interval in intervals:

            if not merged or merged[-1][1] <= interval[0]:
                merged.append(interval)
            else:
              count += 1
        return count

        
        