class Solution:
    def distinctPoints(self, s: str, k: int) -> int:

        n = len(s)
        coords = set()

        if k == 0 or k == len(s):
            return 1

        i = 0 
        j = k
        bY = 0
        bX = 0
        aY = s[k:].count('U') - s[k:].count('D')
        aX = s[k:].count('R') - s[k:].count('L')
        
        while j <=n:

            coords.add((aX+bX,aY+bY))

            if j == n:
                break
        
            if s[j] == 'U':
                    aY -= 1
            if s[j] == 'D':
                    aY +=1
            if s[j] == 'R':
                    aX -= 1
            if s[j] == 'L':
                    aX += 1

            if s[i] == 'U':
                    bY += 1
            if s[i] == 'D':
                    bY -=1
            if s[i] == 'R':
                    bX += 1
            if s[i] == 'L':
                    bX -= 1

           
            i += 1
            j += 1
        
        return len(coords)

            
                
            
                
                
            
                
        
        
            
                 
            
            
        