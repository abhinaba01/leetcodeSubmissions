class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        squares.sort(key = lambda x:x[1])\

        high = -math.inf
        low = math.inf

        for x,y,l in squares:
            high = max(y + l,high)
            low = min(y,low )

     

        eps = 1e-5

     

      

        def area(y0):

            bottom = 0
            top = 0

            for x,y,l in squares:

              
                if y <= y0 <= y + l:
                    bottom += (y0 - y) * l 
                    top +=  (y+l - y0) * l
                elif y + l <= y0:
                    bottom += l * l
                elif y0 <= y:
                    top += l * l

          
            ans = bottom - top
            return ans
        



        while (high - low) > eps:
            mid = (low + high)/2
            res = area(mid)
         
            
            if res < 0:
                low = mid 
            else:
                high = mid
            

        

        return (low + high) / 2

        
        
        

        

        
        
        