class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        N = len(online)
        if len(edges) == 0:
            return -1
        INF = 10 **  18

        adj = [[] for _ in range(N)]
        indegree = [0] * (N)

        for u , v , cost in edges:

            indegree[v] += 1
            if not (online[v] and online[u]):
                cost = INF
            adj[u].append((v,cost))

        topo = []
        q = deque()

        for u in range(N):
            if indegree[u] == 0:
                q.append(u)
            

        while q:

            node  = q.popleft()
            topo.append(node)
            for nei , _  in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)


        dp = [INF] * N
        dp[0] = 0


        for u in topo:

            for v , w in adj[u]:

                dp[v] = min(dp[v],dp[u] + w)
                

        # print(min_edge)



        def solve(val):

            dp = [INF] * N
            dp[0] = 0


            for u in topo:

                for v , w in adj[u]:

                    if w < val:
                        continue

                    dp[v] = min(dp[v],dp[u] + w)

        
            if  dp[N - 1] > k:
                return False

            else:
                return True



        

        low , high = 0 , max(edges , key = lambda x: x[2])[2]
        ans = -1

        while low <= high:

            mid = low + (high - low) // 2

            if solve(mid):
                low = mid + 1
                ans = mid

            else:
                high = mid - 1

        return ans

        
            


        

       

        
                

        


        
        