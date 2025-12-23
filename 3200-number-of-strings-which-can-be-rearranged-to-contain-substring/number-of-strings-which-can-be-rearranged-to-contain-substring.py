class Solution:
    def stringCount(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        def p(a, b):
            return pow(a, b, MOD)

        return (
            p(26, n)
            - 3 * p(25, n)
            - n * p(25, n-1)
            + 3 * p(24, n)
            + 2 * n * p(24, n-1)
            - p(23, n)
            - n * p(23, n-1)
        ) % MOD


        