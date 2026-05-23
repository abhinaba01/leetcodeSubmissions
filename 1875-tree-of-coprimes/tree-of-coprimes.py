class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        

        n = len(nums)
        path = [[] for _ in range(51)]
        ans = [-1] * len(nums)

        adj = [[] for _ in range(n)]

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node,parent,depth):

            largestDepth = -1

            for x in range(1,51):
                if gcd(nums[node],x) == 1:
                    if len(path[x]) > 0:

                        topNode,topDepth = path[x][-1]
                        if largestDepth < topDepth:
                            largestDepth = topDepth
                            ans[node] = topNode
            path[nums[node]].append((node,depth))
            for nei in adj[node]:
                if nei == parent:
                    continue

                dfs(nei,node,depth + 1)
            path[nums[node]].pop()


        dfs(0,-1,0)

        return ans