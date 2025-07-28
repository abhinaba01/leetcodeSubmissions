class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        def dfs(node,isConnected,vis,component):

            vis[node] = True
            component.append(node)

            for neighbor, is_adjacent in enumerate(isConnected[node]):
                if is_adjacent == 1 and not vis[neighbor]:
                    dfs(neighbor,isConnected,vis,component)
            
        

        n  = len(isConnected)

        vis = [False] * n

        res = []
        cnt = 0
        for i in range(n):
            if not vis[i]:
                component = []

                dfs(i,isConnected,vis,component)

                if len(component) != 0:
                    cnt += 1

        return cnt

            


        