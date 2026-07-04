class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        N = n

        adj = [[] for _ in range(N + 1)]
    

        for u , v, edges in roads:
            adj[u].append((v,edges))
            adj[v].append((u,edges))


        visited = [False] * (N + 1)
        visited[1] = True 

        INF = 10 ** 18
        ans = INF

        def dfs(node):

            nonlocal ans

            for nei , wt in adj[node]:

                ans = min(ans , wt)


                if visited[nei]:
                    continue

                visited[nei] = True
                dfs(nei)


        dfs(1)

        return ans
   


     



                

            
        