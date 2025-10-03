class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        b5 = 0
        b10 = 0
        b20 = 0
        i = 0

        while i < len(bills):
            if bills[i] == 5:
                b5 += 1
            if bills[i] == 10:
                b10 += 1
                b5 -= 1
            if bills[i] == 20:
                b20 += 1
                if b10 > 0:
                    b10 -= 1
                    b5 -= 1
                else:
                    b5 -= 3
            
            if b5 < 0 or b10 < 0 or b20 < 0:
                return False
            
            i += 1
        
        return True


               
            
        