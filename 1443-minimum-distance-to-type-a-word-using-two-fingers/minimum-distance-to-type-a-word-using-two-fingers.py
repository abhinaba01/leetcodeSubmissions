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
        def rec(i, pos1, pos2):

            if i == n:
                return 0

            return min(rec(i+1,i,pos2) + dist(i,pos1) , rec(i+1,pos1,i) + dist(i,pos2))
        
        return rec(0,None,None)

        
       

            



            


            



            