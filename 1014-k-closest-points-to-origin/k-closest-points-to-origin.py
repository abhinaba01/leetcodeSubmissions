class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        ans = []
        res = []

        for x , y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush_max(ans,(dist,(x,y)))

            if len(ans) > k:
                heapq.heappop_max(ans)

        
        for dist , point in ans:
            res.append(point)

        
        return res





        