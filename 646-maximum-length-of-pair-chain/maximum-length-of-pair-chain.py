class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key = lambda x:x[1])
    	
        cnt = 1
        prev = pairs[0][1]
        for start ,end in pairs:
            if start > prev:
                cnt += 1
                prev = end
        return cnt

        