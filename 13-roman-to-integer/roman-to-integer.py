class Solution:
    def romanToInt(self, s: str) -> int:

        n = len(s)
        ans = 0
        for i in range(n):

           
            right = s[i+1] if i + 1 < n else " "
            if s[i] == "I":
                if right in "VX":
                   ans -= 1
                else:
                    ans += 1
                  

            elif s[i] == "V":
                ans += 5
            elif s[i] == "X":
                if right in "LC":
                    ans -= 10
                else:
                    ans += 10
            elif s[i] == 'L':
                ans += 50
            elif s[i] == "C":
                if right in "DM":
                    ans -= 100
                else:
                    ans += 100
            elif s[i] == "D":
                ans += 500
            elif s[i] == "M":
                ans += 1000

        return ans
            


            
            
        