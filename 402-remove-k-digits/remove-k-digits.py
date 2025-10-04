class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        n = len(num)

        for i in range(n):
            while k > 0 and stack and int(stack[-1]) > int(num[i]):
                stack.pop()
                k -= 1
            
            stack.append(num[i])
        
        while k > 0:
            stack.pop()
            k -= 1
        

        
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
