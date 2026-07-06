class Solution:
    def divisibleGame(self, nums: list[int]) -> int:

        limit = max(nums)
        N = len(nums)
        MOD = 10 ** 9 + 7
        INF = 10 ** 18



        candidates = set()

        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    candidates.add(d)
                    candidates.add(x // d)
                d += 1

            if x > 1:
                candidates.add(x)

        
        k = 2
        while k in candidates:
            k += 1

        candidates.add(k)



       
       
        max_score , k_val = -INF , 0

        for k in sorted(candidates):
            
            arr = nums[:]
          

            for i in range(N):
                if arr[i] % k != 0:
                    arr[i] = -arr[i]

            
            curr = arr[0]
            max_sum = arr[0]

            for i in range(1,N):

                curr = max(arr[i],curr + arr[i])
              
                max_sum = max(max_sum , curr)
            
            


              
           
            
            if max_score < max_sum:
                max_score , k_val = max_sum , k

            


        return (max_score * k_val) % MOD
            




            



            
                
                

        

            

        

        

        