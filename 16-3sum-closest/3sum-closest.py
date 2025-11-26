class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        length = float("inf")
        n = len(nums)
        closest = 0

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L , R = i + 1 , n - 1

            while L < R:
                total =  nums[i] + nums[L] + nums[R]
                if abs(total - target) < length:
                    closest = total
                    length = abs(total - target)
                if total > target:
                    R -= 1
                elif total < target:
                    L += 1
                else:
                    return target
                
        return closest


        