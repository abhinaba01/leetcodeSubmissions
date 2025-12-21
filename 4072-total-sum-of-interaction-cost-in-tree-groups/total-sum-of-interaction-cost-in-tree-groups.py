class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:

       
        total_sum = 0
        ans = 0

        total_grp = [0] * 21

       

        adj = defaultdict(list)

        for start , end in edges:
            adj[start].append(end)
            adj[end].append(start)

        for g in group:
            total_grp[g] += 1

        def dfs(node,parent):

            nonlocal ans

            res = [0] * 21

            for child in adj[node]:
                if child == parent:
                    continue
                    
                cnt = dfs(child,node)

                for i in range(21):
                    res[i] += cnt[i]
                    ans += cnt[i] * (total_grp[i] - cnt[i])
                    
            res[group[node]] += 1
                

               

            return res 

        dfs(0,-1)
        return ans

            

                
                
                
            
        
            
           

        

     
            

            
            
            
            
        
        
            
        