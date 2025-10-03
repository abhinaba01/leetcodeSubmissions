class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        merged = []

        for interval in intervals:

            if merged == [] or interval[0] > merged[-1][-1]:
                merged.append([interval[0],interval[1]])
            if interval[0] <= merged[-1][-1]:
                merged[-1][1] = max(interval[1],merged[-1][1])
    
                
        return merged

        