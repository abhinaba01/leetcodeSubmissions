class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashNums = {}
        hashNums2 = {}

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]
            if ch1 in hashNums:
                if hashNums[ch1] != ch2:
                    return False
            elif ch2 in hashNums2:
                if hashNums2[ch2] != ch1:
                    return False
            else:
                hashNums[ch1] = ch2
                hashNums2[ch2] = ch1
        return True

     

                        
                

            
        
        