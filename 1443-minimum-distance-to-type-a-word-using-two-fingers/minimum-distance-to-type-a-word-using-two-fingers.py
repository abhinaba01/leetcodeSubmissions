class Solution:
    def minimumDistance(self, word: str) -> int:

        n = len(word)

        def dist(u , v):

            if  v == None:
                return 0 

            r1 , c1 = (ord(word[u]) - 65) // 6 , (ord(word[u]) - 65) % 6 
            r2 , c2 = (ord(word[v]) - 65) // 6 , (ord(word[v]) - 65) % 6

            return abs(r1 - r2) + abs(c1 - c2) 
        
        @cache
        def rec(i,pos):

            if i == n-1:
                return 0

            return min(rec(i+1,pos) + dist(i+1,i) , rec(i+1,i) + dist(i+1,pos))
        
        return rec(0,None)

        
       

            



            


            



            