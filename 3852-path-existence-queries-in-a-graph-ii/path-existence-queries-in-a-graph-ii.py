class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        snums = []
        answer = []

        for i , num in enumerate(nums):
            snums.append((num,i))

        
        snums.sort()

        pos = {}
        reachable = [0] * n
        
        for i , (num, original) in enumerate(snums):
            pos[original] = i


        for i in range(n):
            index = bisect.bisect_right(snums,snums[i][0] + maxDiff,key = lambda x : x[0])
            if index:
                reachable[i] = index - 1


        LOG = 20

        up = [[0] * LOG for _ in range(n)]

        for i in range(n):
            up[i][0] = reachable[i]
        
        for i in range(1,LOG):
            for node in range(n):
                up[node][i] = up[up[node][i-1]][i-1]


    
                


        for u , v in queries:

            su = pos[u]
            sv = pos[v]

            if su > sv:
                su ,sv = sv , su

           

            curr = su
            steps = 0
            
            for k in range(LOG - 1, -1 , -1):
                if up[curr][k] < sv:
                    curr = up[curr][k]
                    steps += (1 << k)

            if curr >= sv:
                answer.append(steps)
            elif reachable[curr] >= sv:
                answer.append(steps + 1)
            else:
                answer.append(-1)
            



        return answer


                



     

        



                



        