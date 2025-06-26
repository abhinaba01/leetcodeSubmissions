class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
                count = max(count,len(stack))
               
            elif ch == ')':
                stack.pop()

        return count
        
        