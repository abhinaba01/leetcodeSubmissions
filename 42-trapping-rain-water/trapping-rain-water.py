class Solution:
    def trap(self, height: List[int]) -> int:

        
        n = len(height)
       

        right = [0] * n
        left = [0] * n
 
        maxRight = 0
        maxLeft = 0
        water = 0

        for i in range(n-1 ,-1 ,-1):
            maxRight = max(height[i],maxRight)
            right[i] = maxRight

            l = n - 1 - i
            maxLeft = max(height[l],maxLeft)
            left[l] = maxLeft


        for i in range(n):

            water += max(min(left[i],right[i]) - height[i],0)
        
        return water

        



        


       
            
    