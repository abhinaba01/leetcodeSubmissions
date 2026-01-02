class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda x:x[1])

        cnt = 1
        prev = points[0][1]

        for start,end in points:
            if start > prev:
                cnt += 1
                prev = end
           
        return cnt
            
            

       

       


      

        