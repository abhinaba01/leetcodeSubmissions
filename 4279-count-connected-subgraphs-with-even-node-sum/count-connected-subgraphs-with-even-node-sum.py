class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:

       
        subsets  = [[]]

        n = len(nums)

        cnt = 0

        temp = []

        
        edge = defaultdict(list)


        for u , v in edges:

            edge[u].append(v)
            edge[v].append(u)



        def isConnected(arr):

            

            visited = set()

        
            def dfs(node):

                visited.add(node)

                

                for nei in edge[node]:
                    if nei not in visited and nei in arr:
                        dfs(nei)

            dfs(arr[0])
            if len(visited) == len(arr):
                return True

            return False




        for i in range(n):
            temp.append(i)

        for num in  temp:

            subsets += [current + [num] for current in subsets]

        for subset in subsets:

            if not subset:
                continue

            total = 0

            for index in subset:
                total += nums[index]

            if total % 2 != 0:
                continue

            elif isConnected(subset):
                cnt += 1

        return cnt

        

                

        
        