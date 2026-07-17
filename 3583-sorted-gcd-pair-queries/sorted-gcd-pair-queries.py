class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        MAX = max(nums)

        cd = [0] * (MAX + 1)

        cnt = [0] * (MAX + 1)

        for x in nums:
            cnt[x] += 1

        
        for d in range(1 , MAX + 1):
            for multiple in range(d , MAX + 1 , d):
                cd[d] += cnt[multiple]

        freq = [0] * (MAX + 1)


        for a in range(MAX , 0 , -1):

            freq[a] = (cd[a] * (cd[a] - 1)) // 2

            for b in range(2 * a , MAX + 1 , a):
                freq[a] -= freq[b]


        

        total = 0
        prefix = [0] * (MAX + 1)
        
        for i in range(1,MAX + 1):
            total += freq[i]
            prefix[i] = total


        res = [-1] * len(queries)

        for i in range(len(queries)):

            q = queries[i]

           

            low = 1 
            high = MAX
            ans = -1

            while low <= high:

                mid = (low + high) // 2

                if prefix[mid] - 1  >= q:
                    ans = mid
                    high = mid - 1

                else:
                    low = mid + 1

            res[i] = ans

        
        return res
            

        
        



        
        


        


        

        