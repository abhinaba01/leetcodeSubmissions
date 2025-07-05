class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        res = start ^ goal
        cnt = 0

        while res > 0:
            cnt += (res & 1)

            res = res >> 1
        return cnt

            


        