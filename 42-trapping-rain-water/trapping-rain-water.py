class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        water = [0] * n

       
            
            
            
        def maxRight(i):
             
            maxNum = max(height[i+1:]) if i < n-1 else 0
            return maxNum

        maxLeft = 0
    
        
        for i in range(n):
            
            water[i] = min(maxLeft,maxRight(i)) - height[i]
            if water[i] < 0:
                water[i] = 0
            maxLeft = max(maxLeft,height[i])

        
        return sum(water)
        


           
                       

        