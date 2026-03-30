class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        N = len(nums)
        window_sum = sum(nums[:k])
        maxAvg = window_sum / k

        l , r = 0 ,k
        while r < N: 
            
            window_sum -= nums[l]
            window_sum += nums[r]


            avg = window_sum / k
            maxAvg = max(avg,maxAvg)

            l += 1
            r += 1

        
        return maxAvg
    



    