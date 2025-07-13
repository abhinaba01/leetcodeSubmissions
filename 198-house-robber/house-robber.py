class Solution:

    
    def rob(self, nums: List[int]) -> int:


        dp1 = [-1] * 101

        def dp(i) -> int:

            arr = nums[i:]


            if dp1[i] != -1:
                return dp1[i]


            elif len(arr) == 3:
                return max(arr[0] + arr[2],arr[1])

            elif len(arr) == 2:
                return max(arr[0],arr[1])

            elif len(arr) == 1:
                return arr[0]
            
            dp1[i] = max(nums[i] + dp(i+2), dp(i+1))
            return dp1[i]


        return dp(0)
        







        

        



        