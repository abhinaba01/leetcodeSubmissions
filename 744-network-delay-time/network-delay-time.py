class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        delay = [float("inf")] * (n+1)
        delay[k] = 0

        for i in range(n-1):
            tmpTime = delay.copy()
            for src,dest,t in  times:
                if delay[src] == float("inf"):
                    continue
                if delay[src] + t < tmpTime[dest]:
                    tmpTime[dest] = delay[src] + t
            delay = tmpTime

       
        ans = max(delay[1:])
        
        return -1 if ans == float("inf") else ans
                
        