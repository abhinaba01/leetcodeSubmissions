class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l,r = 0,0
        freq = {}
        max_freq = 0
        maxLen = 0
        n = len(s)
        
        while r < n:
            ch = s[r]
            freq[ch] = freq.get(ch,0) + 1

            max_freq = max(max_freq,freq[ch])

            
            if (r - l + 1) - max_freq > k:
                ch = s[l]
                freq[ch] -= 1
                l += 1
                max_freq = 0
                for values in freq.values():
                    max_freq = max(max_freq,values)
            
            maxLen = max(maxLen,r - l + 1)
            
            r += 1
        
        return maxLen
        

                    



            

        