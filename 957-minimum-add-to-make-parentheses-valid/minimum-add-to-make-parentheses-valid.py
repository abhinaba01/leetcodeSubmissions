class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    stack.append(ch)
                else:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(ch)

        return len(stack)

        


        