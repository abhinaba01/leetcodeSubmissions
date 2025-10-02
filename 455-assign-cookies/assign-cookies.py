class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        count = 0
       
        ng = len(g)
        ns = len(s)

        i = 0
        j = 0

        while i < ng and j < ns:
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return count




       

        