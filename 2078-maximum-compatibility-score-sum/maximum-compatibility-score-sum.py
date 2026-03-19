class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        m = len(students)
        n = len(students[0])


        comp = [[0]  * m for _ in range(m)]  
        
        for i in range(m):
            for j in range(m):

                score = 0

                for k in range(n):

                    
                    
                    score += (students[i][k] == mentors[j][k])

                
                comp[i][j] = score

        
        cache = [[-1] * (1 << m) for _ in range(m)]
        
        def dp(i , mask):


            if (i == m):
                return 0

            if cache[i][mask] != -1:
                return cache[i][mask]
            
            ans = 0

            for j in range(m):

                if (mask & (1 << j)) == 0:
                    ans = max(ans,dp(i+1,mask | (1 << j)) + comp[i][j])

            cache[i][mask] = ans
            return ans

        
        return dp(0,0)


            

               

        