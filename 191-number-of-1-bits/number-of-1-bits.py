class Solution:
    def hammingWeight(self, n: int) -> int:
        

        cnt = 0
        i = 0
        l = n.bit_length()

        while i != l:
            
            cnt += (n >> i) & 1
            i += 1
          
            
        return cnt
        