class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        count = 0

        i = len(g) - 1
        j = len(s) - 1

        while i >= 0 and j >= 0:
            if g[i] <= s[j]:
                j -= 1
                count += 1
            i -= 1

        return count

        