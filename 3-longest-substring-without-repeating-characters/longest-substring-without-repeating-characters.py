class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        s1 = ""
        cnt = 0

        
        
        maxS = float("-inf")

        for ch in s:
            
            if ch not in s1:
                s1+=ch
                cnt +=1
            else:
                if cnt > maxS:
                    maxS = cnt
                    maxS1 = s1
                    
                index = s1.find(ch)
                
                cnt = len(s1) - (index)
                s1 = s1[index+1:] + ch
                
                

        maxS = max(maxS,cnt)
        return maxS






        