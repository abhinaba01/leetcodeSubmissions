class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        r = 0
        n = len(bills)
      
        a,b,c = 0,0,0
      
        while r < n:
            bill = bills[r]

            if bill == 20:
                
                if a >= 1 and b >= 1:
                    a -= 1
                    b -= 1
                
                elif a >= 3:
                    a -= 3
                else:
                    return False
                c += 1

            if bill == 10:
                if a >= 1:
                    a -= 1
                else:
                    return False
                b += 1

            if bill == 5:
                a += 1             
            
            r += 1
        return True

            
        
