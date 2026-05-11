class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        n = len(nums)

        diff = [0] * (n + 1)

        flip = 0
        c = 0


        for i in range(n):
            
            flip += diff[i]

            if (nums[i] == 0 and flip % 2 == 0)  or (nums[i] == 1 and flip % 2 != 0):
                
                diff[i] += 1

                if i + k > n:
                    return -1

                diff[i+k] -= 1

               

                c += 1 
                flip += 1

        

        return c