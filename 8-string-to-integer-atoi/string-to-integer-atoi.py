class Solution:
    def myAtoi(self, s: str) -> int:

        sign , num = 1 , 0

        if len(s) == 0:
            return 0

        s = s.strip()

        if len(s) == 0:
            return 0

        if s[0] == "-":
            s = s[1:]
            sign = -1
        elif s[0] == "+":
            s = s[1:]
            
       


        if len(s) == 0:
            return 0
        for ch in s:
            if not ch.isdigit():
                break
            d = int(ch)
            
            num = num*10 + d

        num *= sign

       

        if num > (2 ** 31) - 1:
            num = 2 ** 31 - 1
        elif num < -(2 ** 31):
            num = -(2 ** 31)

        return num
        