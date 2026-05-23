class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        tree = [[] for _ in range(n)]
        

        for a , b in edges:
            tree[a].append(b)
            tree[b].append(a)


        if n == 1:
            return [1]


        LOG = math.ceil(math.log2(n))

        dp = [[-1] * LOG for _ in range(n)]
        cnt = [[0] * 26  for _ in range(n)]


        def dfs(node,parent):

            dp[node][0] = parent
            cnt[node][ord(labels[node]) - ord('a')] = 1
         
        
            for nei in tree[node]:
                if nei == parent:
                    continue
             

                dfs(nei,node)

                for j in range(26):
                    cnt[node][j] += cnt[nei][j]
              

                
        dfs(0,-1)

        res = []

        for i in range(n):
            ans = cnt[i][ord(labels[i]) - ord('a')]
            res.append(ans)

        
        return res
            


          
            
