class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        pos = []
        neg = []

        for i in range(n):

            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
            

        p = len(pos)
        n = len(neg)

        print(pos)
        print(neg)

       
        k = 0
        i , j = 0 , 0

        while i < p and j < n:
            nums[k] = pos[i]
            nums[k + 1] = neg[j]

            
            k += 2
            i += 1
            j += 1

        return nums

        
        


        