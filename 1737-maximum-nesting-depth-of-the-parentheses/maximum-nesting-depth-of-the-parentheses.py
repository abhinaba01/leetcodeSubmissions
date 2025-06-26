class Solution:
    def maxDepth(self, s: str) -> int:
        

        count , maxCount = 0 , 0

        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                maxCount = maxCount if maxCount > count else count
                count -= 1
        
        return maxCount
        
        