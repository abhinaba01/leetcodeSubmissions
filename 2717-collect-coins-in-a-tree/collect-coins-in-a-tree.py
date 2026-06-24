class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:

        n = len(coins)

        adj = defaultdict(list)
        degree = [0] * (n)

        for u , v in edges:
            
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        
        q = deque()

        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                q.append(i)



        while q:

            node = q.popleft()
            degree[node] = 0

            for nei in adj[node]:

                if degree[nei] == 0:
                    continue

                degree[nei] -= 1

                if degree[nei] == 1 and coins[nei] == 0:
                    q.append(nei)

        

        q = deque()

        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        
        for _ in range(2):

            sz = len(q)

            for _ in range(sz):

                node = q.popleft()
                degree[node] = 0


                for nei in adj[node]:

                    if degree[nei] == 0:
                        continue

                    for nei in adj[node]:

                        if degree[nei] == 0:
                            continue

                        degree[nei] -= 1

                        if degree[nei] == 1:
                            q.append(nei)

        remaining_edges = 0

        for u , v in edges:
            if degree[u] > 0 and degree[v] > 0:
                remaining_edges += 1

        
        return 2 * remaining_edges














