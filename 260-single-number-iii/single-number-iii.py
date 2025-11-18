class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        res = []

        xor = 0
        for num in nums:
            xor ^= num
        
        rightmost_set_bit = xor & (-xor)

        xor1, xor2 = 0, 0
        for num in nums:
            if (num & rightmost_set_bit) == rightmost_set_bit:
                xor1 ^= num
            else:
                xor2 ^= num
        
        res.extend([xor1,xor2])
        return res
            