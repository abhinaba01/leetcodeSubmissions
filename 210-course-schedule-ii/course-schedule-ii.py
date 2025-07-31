from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        vis = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited
        order = []
        has_cycle = False

        def dfs(node):
            nonlocal has_cycle
            if vis[node] == 1:
                # cycle detected
                has_cycle = True
                return
            if vis[node] == 2:
                return

            vis[node] = 1  # mark as visiting

            for neighbor in graph[node]:
                dfs(neighbor)
                if has_cycle:
                    return

            vis[node] = 2  # mark as visited
            order.append(node)  # post-order appending

        for i in range(numCourses):
            if vis[i] == 0:
                dfs(i)
                if has_cycle:
                    return []

        return order[::-1]  # reverse post-order




        



        

       