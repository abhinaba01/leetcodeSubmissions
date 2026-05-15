class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        n = len(original)

        grid = [[math.inf] * 26 for _ in range(26)]

        for i in range(n):

            start = ord(original[i]) - 97
            end = ord(changed[i]) - 97

            grid[start][end] = min(grid[start][end], cost[i])

        dist = [[math.inf] * 26 for _ in range(26)]

        def dijkstra(src):

            dist[src] = [math.inf] * 26
            dist[src][src] = 0

            pq = [(0, src)]

            while pq:

                d, u = heapq.heappop(pq)

                if d > dist[src][u]:
                    continue

                for v in range(26):

                    w = grid[u][v]

                    if w == math.inf:
                        continue

                    newdist = d + w

                    if newdist < dist[src][v]:

                        dist[src][v] = newdist
                        heapq.heappush(pq, (newdist, v))

        for i in range(26):

            dijkstra(i)

        s = len(source)

        cost = 0
        for i in range(s):

            start = ord(source[i]) - 97
            end = ord(target[i]) - 97

            if dist[start][end] != math.inf:

                cost += dist[start][end]
            else:
                return -1


        return cost


