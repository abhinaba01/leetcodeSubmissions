class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = [1] * n        
        ans = [0] * n          

      
        def dfs1(u, parent):
            for v in adj[u]:
                if v == parent:
                    continue
                dfs1(v, u)
                count[u] += count[v]
                ans[u] += ans[v] + count[v]

     
        def dfs2(u, parent):
            for v in adj[u]:
                if v == parent:
                    continue
               
                ans[v] = ans[u] - count[v] + (n - count[v])
                dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)

        return ans


        
          