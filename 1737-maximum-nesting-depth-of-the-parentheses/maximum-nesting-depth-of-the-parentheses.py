class Solution:
    def maxDepth(self, s: str) -> int:
        # count = 0
        # stack = []
        # for ch in s:
        #     if ch == '(':
        #         stack.append(ch)
        #         count = max(count,len(stack))
               
        #     elif ch == ')':
        #         stack.pop()

        # return count

        count , maxCount = 0 , 0

        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                maxCount = maxCount if maxCount > count else count
                count -= 1
        
        return maxCount
        
        