class Solution:
    def countAndSay(self, n: int) -> str:

        
       
        if n == 1:
            return "1"
        
        s = self.countAndSay(n-1)
        cnt = 0
        ans = ""
        stack = []
        for i in range(len(s)):
            ch = s[i]

            if not stack:
                stack.append(ch)
                cnt += 1

            else:
                if stack[-1] == ch:
                    stack.append(ch)
                    cnt += 1
                elif stack[-1] != ch:
                    ans = ans + str(cnt) + stack[-1]
                    while stack:
                        stack.pop()
                        
                    stack.append(ch)
                    cnt = 1

        ans = ans + str(cnt) + stack[-1]
        return ans

   
        
                



        

      