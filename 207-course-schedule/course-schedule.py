class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visit = set()
        path = set()

        adj = [[] for _ in range(numCourses)]

        for start,end in prerequisites:
            adj[start].append(end)

        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            
            path.add(node)

            for neighbours in adj[node]:
                if not dfs(neighbours):
                    return False
            
            visit.add(node)
            path.remove(node)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

                


        