class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def factorial(k):
            if (k == 1) or (k == 0):
                return 1
            else:
                return k * factorial(k-1)

        a = factorial(m+n - 2) // (factorial(m - 1) * factorial(n - 1))

        return a





        