class Solution:

    

    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        l , r = 0 , 0
        max_len = 0
        

        hashMap = {}

        while r < n:

            ch = s[r]
            hashMap[ch] = hashMap.get(ch,0) + 1
            while hashMap[ch] > 1:
                hashMap[s[l]] -= 1
                l+= 1
                
            max_len = max(max_len, r - l + 1)
            r += 1
           
        
        return max_len

            

            
            



        