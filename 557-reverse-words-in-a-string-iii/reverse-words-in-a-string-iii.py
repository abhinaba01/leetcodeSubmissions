class Solution:
    def reverseWords(self, s: str) -> str:

        n = len(s)
        rev_s = ""
        word = ""

        for ch in s:
            if ch == " ":
                rev_s += word[::-1]
                word = ""
                rev_s += ch
            else:
                word += ch
            
        rev_s += word[::-1]
        return rev_s
            

                
        