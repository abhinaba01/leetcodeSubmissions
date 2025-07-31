class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        vis = [-1 for i in range(n)]

        def dfs(node,color):

            if vis[node] == -1:
                vis[node] = color



            for neighbor in graph[node]:
                if vis[neighbor] == -1:
                    if not dfs(neighbor,(color+1)%2):
                        return False
                else:
                    if vis[neighbor] == color:
                        return False
                    
            return True
        
        for i in range(n):
            if vis[i] == -1:
                if not dfs(i,0):
                    return False
        return True
        