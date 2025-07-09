class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
  


        def atMostK(k):
            l , r = 0 , 0
            cnt, unique = 0 ,0
            n = len(nums)
            freq = {}
            while r < n:
                
                if freq.get(nums[r],0) == 0:
                    unique += 1
                freq[nums[r]] = freq.get(nums[r],0) + 1

                while unique > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        unique -= 1
                    l += 1

                cnt += (r-l+1)

                r += 1

            return cnt
            
        return atMostK(k) - atMostK(k-1)


            


