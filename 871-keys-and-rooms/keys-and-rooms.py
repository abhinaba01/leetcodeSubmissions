class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)

        adj = [[] for _ in range(n)]

        node  = 0
        for room in rooms:
            for x in room:
                adj[node].append(x)

            node += 1

        visited = set()
        
        def dfs(node,parent):

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    
                
                    dfs(nei,node)

        
        dfs(0,-1)
        if len(visited) == n:
            return True
        
        return False



        