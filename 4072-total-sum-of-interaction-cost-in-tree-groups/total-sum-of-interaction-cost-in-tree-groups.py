class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:

        adj = defaultdict(list)

        total_grp = defaultdict(int)

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        for g in group:
            total_grp[g] += 1

        res = 0

        def dfs(node,parent):

            nonlocal res 

            curr_count = [0] * 21
            curr_count[group[node]] = 1

            for nei in adj[node]:
                if nei == parent:
                    continue
                
                child_count = dfs(nei,node)
                
                for i in range(21):
                    curr_count[i] += child_count[i]

            for i in range(21):
                res += curr_count[i] * (total_grp[i] - curr_count[i])

            return curr_count


        dfs(0,-1)
        return res

                  




        
        






       
       