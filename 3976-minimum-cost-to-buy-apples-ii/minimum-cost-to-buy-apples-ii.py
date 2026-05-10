class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:


        
        weight = [[] for _ in range(n)]

        weight_tax = [[] for _ in range(n)]

        for u , v , cost , tax  in roads:
            
            weight[u].append((v,cost))
            weight_tax[u].append((v,cost * tax))

            weight[v].append((u,cost))
            weight_tax[v].append((u,cost * tax))

        
        fdist = [[float("inf")] * n for _ in range(n)]
        
        bdist = [[float("inf")] * n for _ in range(n)]

        def forward(src):

            

            fdist[src][src] = 0

            pq = [(0, src)]   

            while pq:

                d, u = heapq.heappop(pq)

               
                if d > fdist[src][u]:
                    continue

                for v, w in weight[u]:

                    newDist = d + w

                    if newDist < fdist[src][v]:

                        fdist[src][v] = newDist

                        heapq.heappush(pq, (newDist, v))

            

        def backward(src):

            

            bdist[src][src] =0

            pq = [(0, src)]   

            while pq:

                d, u = heapq.heappop(pq)

               
                if d > bdist[src][u]:
                    continue

                for v, w in weight_tax[u]:

                    newDist = d + w

                    if newDist < bdist[src][v]:

                        bdist[src][v] = newDist

                        heapq.heappush(pq, (newDist, v))

            return bdist[src]

        
        for i in range(n):
            forward(i)
            backward(i)

        ans = prices[:]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                ans[i] = min(ans[i] , fdist[i][j] + bdist[j][i] + prices[j])

        
        return ans






      