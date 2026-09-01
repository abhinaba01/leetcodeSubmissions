class Solution:
    def sumDecoded(self, nums: list[int]) -> int:

        n = len(nums)
        MOD = 10 ** 9 + 7
        total = 0

        for i in range(n):
            num = nums[i]

            width = num % 10
            d = floor(nums[i] / 10)

            s = str(d)

            x = int(s[:width])
            y = int(s[width:])

            total += pow(x ,y , MOD)


        return total % MOD


        




        
        