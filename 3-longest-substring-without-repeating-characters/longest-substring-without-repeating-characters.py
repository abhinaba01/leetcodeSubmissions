class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l , r = 0 , 0
        ans = 0

        freq = defaultdict(int)

        n = len(s)
        
        for r in range(n):

            freq[s[r]] += 1

            while freq[s[r]] == 2:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans , r - l + 1)

        
        return ans


        