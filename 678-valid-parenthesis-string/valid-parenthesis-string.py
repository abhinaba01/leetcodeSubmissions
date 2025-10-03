class Solution:
    def checkValidString(self, s: str) -> bool:

        s_list = []
        low = 0
        high = 0

        for i in range(len(s)):
            if s[i] == "(":
                low += 1
                high += 1
            elif s[i] == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            low = max(low,0)
            if high < 0:
                return False
        if low > 0:
            return False
        return True

        