class Solution:
    def reverseBits(self, n: int) -> int:

        num = 0
        
        i = 0

        while i < 32:
            d = (n >> i) & 1
            num =  2 * num + d
            i += 1
         
            
            

        return num



       
        