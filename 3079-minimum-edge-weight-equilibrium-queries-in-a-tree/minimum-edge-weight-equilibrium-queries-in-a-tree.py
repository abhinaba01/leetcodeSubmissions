class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        
        graph = [[]  for _ in range(n)]

        depth = [-1] * n

        dp = [[-1] * 20 for _ in range(n)]

        freq = [[0] * 27 for _ in range(n)]

        for u , v , w in edges:

            graph[u].append((v,w))
            graph[v].append((u,w))

    

        def dfs(node,parent):

            dp[node][0] =  parent

            for nei,weight in graph[node]:
                if nei == parent:
                    continue
                depth[nei] = depth[node] + 1
                freq[nei] = freq[node][:]
                freq[nei][weight]  +=  1
                dfs(nei,node)

                

    
        def build():

            depth[0] = 0

            dfs(0,-1)

            for j in range(1,20):
                for i in range(n):

                    if dp[i][j-1] != -1:
                        dp[i][j] = dp[dp[i][j-1]][j-1]

           
        build()

        def lift(node,k):

            j = 0
          
            while k != 0 and node != -1:
                if k & 1:
                    node = dp[node][j]
                    
                
                j += 1
                k = k >> 1
                
            return node

    
        def lca(a,b):

            total_depth = depth[a] + depth[b]

            if depth[a] < depth[b]:
                a,b = b,a

            diff = depth[a] - depth[b]

            a = lift(a,diff)

            if a == b:
                return a
            
            for j in range(19,-1,-1):
                if dp[a][j] != dp[b][j]:
                    a = dp[a][j]
                    b = dp[b][j]
                   

            
          
            lca = dp[a][0]

            return lca

        def ans(u,v):

            anc = lca(u,v)

            ans = 0

            for i in range(27):
                ans = max(ans,freq[u][i] + freq[v][i] - 2 * freq[anc][i])

            dist = depth[u] + depth[v] - 2 * depth[anc]

            return dist - ans

            

        res = []
        for a , b in queries:
            res.append(ans(a,b))

        
        return res









        






            

        




        