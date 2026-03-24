class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        

        n = len(graph)

        dist = [[math.inf] * n for _ in range(n)]

        

        for src in range(n):
            dist[src][src] = 0
            for dst in graph[src]:
                dist[src][dst] = 1
                dist[dst][src] = 1

        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

        dp = [[math.inf] * n for _ in range(1 << n)]
        
        for i in range(n):
            dp[1<<i][i] = 0
      

        for mask in range(1 << n):

            for last in range(n):
                if not mask  & (1 << last):
                    continue
                
                for prev in range(n):
                    if prev != last and (mask & (1 << prev)):
                        dp[mask][last] = min(dp[mask][last],dp[mask ^ (1 << last)][prev] + dist[prev][last])

        return min(dp[(1 << n) - 1])
                
