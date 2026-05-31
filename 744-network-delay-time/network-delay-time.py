class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for u , v , w in times:
            adj[u].append((v,w))
        
        pq = [(0,k)]

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        while pq:

            curr_dist , curr_node = heapq.heappop(pq)
            

            if curr_dist > dist[curr_node]:
                continue
            

            for nei , wt in adj[curr_node]:
                distance = curr_dist + wt

                if distance < dist[nei]:
                    dist[nei] = distance
                    heapq.heappush(pq,(distance,nei))

        
        ans = max(dist[1:])
        return -1 if ans == float("inf") else ans

                    

        