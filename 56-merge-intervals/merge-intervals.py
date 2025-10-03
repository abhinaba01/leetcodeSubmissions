class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        merged = []

        for start,end in intervals:

            if merged == [] or start> merged[-1][-1]:
                merged.append([start,end])
            if start<= merged[-1][-1]:
                merged[-1][1] = max(end,merged[-1][1])
    
                
        return merged

        