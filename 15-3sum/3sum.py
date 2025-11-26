class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            L , R = i + 1 , n - 1

            while L < R:
                if nums[L] + nums[R] > target:
                    R -= 1
                    
                elif nums[L] + nums[R] < target:
                    L += 1
                    
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1

            
        return res

                

       