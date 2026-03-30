class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        n = len(nums)
      
     

        def atMost(k):

            l = 0

            freq = defaultdict(int)

            distinct , cnt = 0 , 0

            for r in range(n):

                if freq[nums[r]] == 0:
                    distinct += 1
                freq[nums[r]] += 1

                while distinct > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        distinct -= 1
                    
                    l += 1

                
                cnt += (r - l + 1)

            return cnt

        

        return atMost(k) - atMost(k - 1)
           
            
        