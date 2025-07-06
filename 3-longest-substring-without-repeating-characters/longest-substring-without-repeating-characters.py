class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        s1 ,maxS = "" , 0
        

        for ch in s:
            
            if ch not in s1:
                s1+=ch
               
            else:
                if len(s1) > maxS:
                    maxS = len(s1)
                   
                    
                index = s1.find(ch)
                s1 = s1[index+1:] + ch
                
                

        maxS = max(maxS,len(s1))
        return maxS






        