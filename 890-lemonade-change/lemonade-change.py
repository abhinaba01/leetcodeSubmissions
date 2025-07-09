class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        r = 0
        n = len(bills)
      
        count = {5:0,10:0}
      
        while r < n:
            bill = bills[r]

            if bill == 20:
                
                if count[5] >= 1 and count[10] >= 1:
                    count[5] -= 1
                    count[10] -= 1
                
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
                

            if bill == 10:
                if count[5] >= 1:
                    count[5] -= 1
                else:
                    return False
                count[10] += 1

            if bill == 5:
                count[5] += 1             
            
            r += 1
        return True

            
        
