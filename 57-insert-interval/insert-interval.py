class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        res = []
        n = len(intervals)
        placed = False
        

        for start , end in intervals:
            if end < newInterval[0]:
                res.append([start,end])
            elif start > newInterval[1]:
                if not placed:
                    res.append(newInterval)
                    placed = True
                res.append([start,end])
            else:
                newInterval[0] = min(newInterval[0],start)
                newInterval[1] = max(newInterval[1],end)

        if not placed:
            res.append(newInterval)


        return res

        
            