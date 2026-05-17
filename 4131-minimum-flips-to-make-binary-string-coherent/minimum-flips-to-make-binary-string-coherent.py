class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        cnt0 = s.count('0')
        cnt1 = n - cnt0

        ans = cnt0

       
        ans = min(ans, max(cnt1 - 1, 0))

        
        keep_boundary_ones = (1 if s[0] == '1' else 0) + (1 if s[-1] == '1' else 0)
        ans = min(ans, max(cnt1 - keep_boundary_ones, 0))

        return ans