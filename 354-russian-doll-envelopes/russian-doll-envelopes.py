class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        n = len(envelopes)

        if not envelopes:
            return 0
        
        LIS = []
        for w , h in envelopes:
            idx = bisect.bisect_left(LIS, h)
            if idx == len(LIS):
                LIS.append(h)
            else:
                LIS[idx] = h
                
        return len(LIS)

        
            






        