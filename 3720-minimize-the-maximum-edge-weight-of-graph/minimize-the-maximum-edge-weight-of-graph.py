class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:


        edges.sort(key = lambda x:x[2])

        low = edges[0][2]
        high = edges[-1][2]

       

        def check(limit):
            
            graph = [[] for _ in range(n)]
            for u, v, w in edges:
                if w > limit:
                    continue
             
                graph[v].append((u, w))
           

       
            visited = set([0])
            
            def dfs(node):
                
                for nei, _ in graph[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    dfs(nei)

            dfs(0)

            return len(visited) == n

       

      
        ans  = -1

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans  = mid
                high = mid - 1
            else:
                low  = mid + 1

        return ans


