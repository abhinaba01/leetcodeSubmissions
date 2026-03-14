class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        L1 = len(word1)
        L2 = len(word2)

        merged = []
        i , j = 0 , 0

        while i < L1 or j < L2:
            if word1[i:] > word2[j:]:
                merged.append(word1[i])
                i += 1
            else:
                merged.append(word2[j])
                j += 1

        return "".join(merged)       