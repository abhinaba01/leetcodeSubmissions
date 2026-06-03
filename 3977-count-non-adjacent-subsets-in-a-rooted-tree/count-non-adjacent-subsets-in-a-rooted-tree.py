from collections import defaultdict
from typing import List


class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:

        MOD = 10**9 + 7
        n = len(parent)

        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        def dfs(node):

           
            dp0 = {0: 1}

        
            dp1 = {nums[node] % k: 1}

            for child in adj[node]:

                child0, child1 = dfs(child)

                ndp0 = defaultdict(int)
                ndp1 = defaultdict(int)

               
                for r1, c1 in dp0.items():

                    for r2, c2 in child0.items():
                        ndp0[(r1 + r2) % k] = (
                            ndp0[(r1 + r2) % k] +
                            c1 * c2
                        ) % MOD

                    for r2, c2 in child1.items():
                        ndp0[(r1 + r2) % k] = (
                            ndp0[(r1 + r2) % k] +
                            c1 * c2
                        ) % MOD

           
                for r1, c1 in dp1.items():

                    for r2, c2 in child0.items():
                        ndp1[(r1 + r2) % k] = (
                            ndp1[(r1 + r2) % k] +
                            c1 * c2
                        ) % MOD

                dp0 = ndp0
                dp1 = ndp1

            return dp0, dp1

        dp0, dp1 = dfs(0)

        return (dp0.get(0, 0) + dp1.get(0, 0) - 1) % MOD