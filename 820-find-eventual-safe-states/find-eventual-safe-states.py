class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)

        
        topSort = []
        visit = set()
        path = set()
       

        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            
            path.add(node)
            
            for neighbours in graph[node]:
                if not dfs(neighbours):
                    return False
            topSort.append(node)
            visit.add(node)
            path.remove(node)
            return True
            

        for i in range(n):
            if  not dfs(i):
                continue
        
        return sorted(topSort)




        