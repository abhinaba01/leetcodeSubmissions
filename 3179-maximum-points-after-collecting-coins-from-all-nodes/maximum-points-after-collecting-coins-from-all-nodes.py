class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:

        adj = [[] for _ in range(len(edges)+1)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        @cache
        def solve(node,parent,c):

            ans = 0
            res = 0

            firstChoice = ((coins[node] >> c) - k)
            secondChoice = (coins[node] >> (c+1))

            for child in adj[node]:
                if child == parent:
                    continue

                firstChoice += solve(child,node,min(c,14))
                secondChoice +=  + solve(child,node,min(c+1,14))
                  
            return max(firstChoice,secondChoice)

        return solve(0,-1,0)

        
             


        