class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []

        def solve(i,arr):
            if i == n:
                result.append(arr)
                return
                

         
            arr.append(nums[i])
            solve(i+1,arr[:])
            arr.pop()
            solve(i+1,arr[:])

        solve(0,[])
        return result
        