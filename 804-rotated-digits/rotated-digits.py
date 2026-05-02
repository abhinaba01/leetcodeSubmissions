class Solution:
    def rotatedDigits(self, n: int) -> int:

        

        def countGoodIntegers(num):

            flag = False

            for digit in str(num):
                if digit in "347":
                    return 0
                if digit in "2569":
                    flag = True
            if flag:
                return 1
            return 0
        
        total = 0
        for i in range(1,n+1):
            total += countGoodIntegers(i)

        return total