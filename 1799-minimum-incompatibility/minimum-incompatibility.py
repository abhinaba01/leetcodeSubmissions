class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:


        n = len(nums)
        nums.sort()

        cnt = 0

        if n % k != 0:
            return -1

        N = 1 << n
        

        valid = [False] * N
        group_size = n // k

        incomp = defaultdict(int)

        for mask in range(N):

          
            if mask.bit_count() != group_size:
                continue

            seen = set()
            isValid = True

            for i in range(n):
                if mask & (1 << i):
                    
                 
                    if nums[i] in seen:
                        isValid = False
                        break
                    
                    seen.add(nums[i])

            if isValid:
                valid[mask] = True

                maxE = 0
                minE = math.inf

                for i in range(n):
                    if mask & ( 1 << i):
                        maxE = max(maxE,nums[i])
                        minE = min(minE,nums[i])
                
                
                incomp[mask] = maxE - minE


        


        
        dp = [math.inf] * N
        dp[0] = 0

        
        for mask in range(1,N):


            if mask.bit_count() % group_size != 0:
                continue



            first = mask & -mask



         

            sub = mask

            while sub:

                
                

                if valid[sub] and (sub & first):
                    dp[mask] = min(dp[mask],dp[mask ^ sub] + incomp[sub]) 



                sub = (sub - 1) & mask

        
        return dp[N - 1] if dp[N - 1] != math.inf else -1

            
                 


       

     


        