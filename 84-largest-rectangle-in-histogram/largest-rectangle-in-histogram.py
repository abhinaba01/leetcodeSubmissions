class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        stack = []
        
        NSE = [-1] * n
        PSE = [n] * n

        for i in range(n):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            NSE[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
            
        for i in range(n-1,-1,-1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            PSE[i] = stack[-1] if stack else n
            stack.append(i)

    
        maxArea = 0

        for i in range(n):
            maxArea = max((PSE[i] - NSE[i] - 1) * heights[i], maxArea)
        return maxArea
        
            
        
        