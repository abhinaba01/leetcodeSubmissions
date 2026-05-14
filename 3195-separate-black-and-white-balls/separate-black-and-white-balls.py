class Solution:
    def minimumSteps(self, s: str) -> int:

    
        target_index = 0

        n = len(s)
        cnt = 0

        for i in range(n):
            if s[i] == "0":
                cnt += (i - target_index)

                target_index += 1

        
        return cnt