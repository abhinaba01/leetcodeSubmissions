class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        parenthesis = {')':'(',']':'[','}':'{'}

        for ch in s:
            if ch in parenthesis:
                if stack and stack[-1] == parenthesis[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if stack:
            return False
        else:
            return True


        