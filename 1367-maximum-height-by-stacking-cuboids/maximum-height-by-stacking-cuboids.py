class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:

        n = len(cuboids)

        for i , (l , w , h) in enumerate(cuboids):

            cuboids[i] = sorted([l,w,h])

        cuboids.sort(key = lambda x: (x[0],x[1],x[2]))

        print(cuboids)

        dp = [cuboid[2] for cuboid in cuboids]
      
        for i in range(n):
            for j in range(i):

                if (cuboids[i][1] >= cuboids[j][1] and 
                cuboids[i][2] >= cuboids[j][2]):
                    dp[i] = max(dp[i],dp[j] + cuboids[i][2])
                   
                   

        
        return max(dp)


        


        