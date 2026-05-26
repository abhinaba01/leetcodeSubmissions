class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
       
        depth = [0] * n

        for u , v in connections:
            adj[u].append(v)
            adj[v].append(u)


        def dfs(node,parent):

            

            
            for nei in adj[node]:
                if nei == parent:
                    continue
                depth[nei] = depth[node] + 1
                dfs(nei,node)

        dfs(0,-1)
       
        cnt = 0
        for u , v in connections:

            if depth[u] - depth[v] < 0:
                cnt += 1

        return cnt

            

        
        

        


        
        

        
        
        