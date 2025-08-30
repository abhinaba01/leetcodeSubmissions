class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(k):
            n = len(nums)
            count = 0
            countOdd = 0
            l,r =  0,0

            while r < n:

                if (nums[r] & 1):
                    countOdd += 1
                
                while countOdd > k:
                    if (nums[l] & 1):
                        countOdd -= 1
                    l += 1
                
                count += r - l + 1
                r += 1

            return count

        return atMost(k) - atMost(k - 1) 



            

        