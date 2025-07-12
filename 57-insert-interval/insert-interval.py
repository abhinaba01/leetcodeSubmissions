class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        before = []
        merged = []
        
        after = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                before.append(interval)
            elif interval[0] > newInterval[1]:
                after.append(interval)
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])

        merged = before + [newInterval] + after

        return merged

        
                

            
           

        