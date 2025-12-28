class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        LOG = 20
        MOD = 10 ** 9 + 7
        n = len(edges)
        dp = [[-1] * LOG for _ in range(n+2)]

        adj = [[] for _ in range(n+2)]
        depth = [0] * (n +2)
        num = [0] * (n)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def dfs(node,parent):

            dp[node][0] = parent
            for j in range(1,LOG):
                if dp[node][j-1] != -1:
                    dp[node][j] = dp[dp[node][j-1]][j-1]

            for child in adj[node]:
                if child == parent:
                    continue
                depth[child] = depth[node] + 1
                dfs(child,node)

        dfs(1,-1)
        
        def lca(p,q):

            if depth[p] < depth[q]:
                p,q = q,p
            
            diff = depth[p] - depth[q]

            for j in range(LOG):
                if diff & (1 << j):
                    p = dp[p][j]

                if p == q:
                    return p

       
            for j in range(LOG - 1, -1, -1):
                if dp[p][j] != -1 and dp[p][j] != dp[q][j]:
                    p = dp[p][j]
                    q = dp[q][j]

        
            return dp[p][0]

        
        def binpow(a, b):
            result = 1
            while b > 0:
                if b & 1:          
                    result *= a
                a = (a *  a )% MOD
                b >>= 1            
            return result % MOD

        res = []

        for u,v in queries:
            if u == v:
                res.append(0)

            else:
                numEdges = depth[u] + depth[v] - 2 * depth[lca(u,v)]
                res.append(binpow(2,numEdges - 1))

        return res

            
        



            
            
          

                

            
                
                
            





        