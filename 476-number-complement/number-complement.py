class Solution:
    def findComplement(self, num: int) -> int:
        
        l = num.bit_length()
        mask = (1 << l) - 1
        return num ^ mask