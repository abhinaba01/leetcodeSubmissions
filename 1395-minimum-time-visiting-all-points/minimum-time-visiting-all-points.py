class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        time = 0
        curr_x = points[0][0]
        curr_y = points[0][1]

        for x , y in points:
            diff_x = abs(x - curr_x)
            diff_y = abs(y - curr_y)

          
          
            time += max(diff_x , diff_y)
            curr_x = x
            curr_y = y

        
        return time
        






            

    
        