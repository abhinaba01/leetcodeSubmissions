class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        LOG = math.ceil(math.log2(n)) + 1
        
        adj = [[] for _ in range(n+2)]

        depth = [0] * (n+2)
        freq = defaultdict(lambda: [0] * 27)

        dp = [[-1] * LOG for _ in range(n+1)]
      
        
        
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])


    

        def dfs(node,parent):
           
            
               
            dp[node][0] = parent
            
            for j in range(1,LOG):
                if dp[node][j-1] != -1:
                    dp[node][j] = dp[dp[node][j-1]][j-1]

            

            for child,weight in adj[node]:
                if child == parent:
                    continue
                freq[child] = freq[node][:]
                freq[child][weight] += 1
                depth[child] = depth[node] + 1
                dfs(child,node)

        dfs(0,-1)

        def lca(p,q):

            if depth[p] < depth[q]:
                p,q = q,p

            diff = depth[p] - depth[q]

            for i in range(LOG):
                if diff & ( 1<< i):
                    p = dp[p][i]

                if p == q:
                    return p

            for i in range(LOG - 1 ,-1 , -1):
                if dp[p][i] != -1 and dp[p][i] != dp[q][i]:
                    p = dp[p][i]
                    q = dp[q][i]

            return dp[p][0]

        def solve(u,v):

            k = lca(u,v)
            ne = depth[u] + depth[v] - 2 * depth[k]
            res = [0] * 27


            for i in range(1,27):
                res[i] = freq[u][i] + freq[v][i] - 2 * freq[k][i]

            return ne - max(res[1:])

            
        ans = []
        for a,b in queries:
            ans.append(solve(a,b))

        return ans


        