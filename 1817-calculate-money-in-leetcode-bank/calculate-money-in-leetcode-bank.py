class Solution:
    def totalMoney(self, n: int) -> int:

        weeks = n // 7
        days = n % 7

        totalMoney = (weeks * 28) + 7 * ((weeks-1) * weeks // 2)

        start = weeks + 1

        for i in range(days):
            totalMoney += (start + i)
        
        return totalMoney

        
        