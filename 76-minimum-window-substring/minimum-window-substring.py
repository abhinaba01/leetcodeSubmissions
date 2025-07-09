class Solution:
    def minWindow(self, s: str, t: str) -> str:

        m = len(s)
        n = len(t)

        if m < n:
            return ""

        freqT = {}

        for ch in t:
            freqT[ch] = freqT.get(ch,0) + 1


        def isOk(dict1):
            for ch in freqT:
                if ch not in dict1:
                    return False 
                
                if dict1[ch] < freqT[ch]:
                    return False
            
            return True

        

        l,r = 0,0
        ans = ""
        freq = {}
        minLen = float("inf")
        while r < m:
            
            freq[s[r]] = freq.get(s[r],0) + 1

            while isOk(freq):

                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    ans = s[l:r+1]
                
                freq[s[l]] -= 1
                
                l += 1
            
            r += 1

        return ans
            


        



        
        