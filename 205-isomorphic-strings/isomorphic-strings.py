class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashNums = {}

        for i in range(len(s)):
            ch = s[i]
            if ch in hashNums:
                if hashNums[ch] != t[i]:
                    return False
            else:
                hashNums[ch] = t[i]

        hashNums2 = {}

        for i in range(len(t)):
            ch = t[i]
            if ch in hashNums2:
                if hashNums2[ch] != s[i]:
                    return False
            else:
                hashNums2[ch] = s[i]

        return True

                        
                

            
        
        