class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []
        

        for i in range(1 << n):

            ans = []

            for k in range(n):

                if i & (1 << k):
                    ans.append(nums[k])
                
            result.append(ans)
        
        return result
                


            
