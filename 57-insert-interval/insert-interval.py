class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        merged = newInterval
        before = []
        after = []
        for start,end in intervals:
            if end < newInterval[0]:
                before.append([start,end])
            elif start > newInterval[1]:
                after.append([start,end])
            else:
                merged[0] = min(start,merged[0])
                merged[1] = max(end,merged[1])
        
        newArray = before + [merged] + after

        return newArray

        

        