from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(numCourses)]

        for start, end in prerequisites:
            adj[start].append(end)

        topSort = []
        path = set()
        visit = set()

        def dfs(node):

            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            
            for neighbours in adj[node]:
                if not dfs(neighbours):
                    return False
            topSort.append(node)
            visit.add(node)
            path.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return topSort

        




        

       