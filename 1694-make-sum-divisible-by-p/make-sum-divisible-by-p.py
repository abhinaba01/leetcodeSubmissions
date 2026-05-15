class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        prefix = 0


        n = len(nums)

        prefixSum  =  [0] * (n + 1)
        modulo = defaultdict(list)

        modulo[0] = [-1]
        
        for i in range(1,n+1):
            prefix += nums[i-1]
            prefixSum[i] = prefix % p
            modulo[prefixSum[i]].append(i - 1)



       

        

        rem = prefix % p

        if rem == 0:
            return 0

       

        

        # for k in range(1,n):
        #     for i in range(n):

        #         if i + k < n + 1:
                    
        #             if (prefixSum[i+k] - prefixSum[i]) % p == rem:
        
        #                 return k
                    
        #         else:
        #             break

        # return -1

        
        ans = math.inf
        for i in range(n + 1):

            res = (prefixSum[i] - rem) % p

            if res in modulo:
                for val in modulo[res]:
                    if val < i:
                        ans = min(ans,(i - 1- val))
               

        return ans if ans != math.inf and ans != n else -1



        


        


