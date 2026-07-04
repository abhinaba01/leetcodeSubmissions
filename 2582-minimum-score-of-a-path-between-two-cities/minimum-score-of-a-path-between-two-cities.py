class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        N = n

        adj = [[] for _ in range(N + 1)]
    

        for u , v, edges in roads:
            adj[u].append((v,edges))
            adj[v].append((u,edges))


        visited1 = [False] * (N + 1)
        visited1[1] = True 

        visited2 = [False] * (N + 1)
        visited2[N] = True
        
        def dfs(node,visited):


            for nei , wt in adj[node]:


                if visited[nei]:
                    continue

                visited[nei] = True
                dfs(nei,visited)


        dfs(1,visited1)
        dfs(n,visited2)


        roads.sort(key = lambda x:x[2])
        for u , v , dist in roads:
            if visited1[u] and visited1[v] and visited2[u] and visited2[v]:
                return dist

        



                

            
        