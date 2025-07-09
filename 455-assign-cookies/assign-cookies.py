class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        
        g.sort()
        s.sort()

        n = len(g)
        m = len(s)

        cnt = 0
        k = -1

        
        
        for i in range(n):

            j = k + 1
            new = cnt

            while j < m:

                if s[j] >= g[i]:
                    cnt += 1
                    k = j
                    s[j] = 0
                    break
                j += 1
            if cnt == new:
                break

        return cnt


        