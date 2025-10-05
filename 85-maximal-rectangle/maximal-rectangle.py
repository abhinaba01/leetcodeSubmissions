class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        height = [0] * cols
       

        def calculateMaxArea(arr):

            n = len(arr)

            nse = [n] * n
            pse = [-1] * n

            stack = []

            for i in range(n):

                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                
                pse[i] = stack[-1] if stack else -1
                stack.append(i)
            
            stack = []

            for i in range(n-1,-1,-1):

                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                
                nse[i] = stack[-1] if stack else n
                stack.append(i)
            
            maxArea = 0
            for i in range(n):
                area = arr[i] * (nse[i] - pse[i] - 1)
                maxArea = max(maxArea,area)
            
            return maxArea
        
        maxArea = 0
        for r in range(rows):
        
            for c in  range(cols):
                if matrix[r][c] == "1":
                    height[c] += 1
                else:
                    height[c] = 0
                
          
        
            area = calculateMaxArea(height)
            maxArea = max(maxArea,area)

        return maxArea

        


            

            
        