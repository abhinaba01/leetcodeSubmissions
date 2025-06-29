class Solution:


    def createsubSet(self,outer,nums):

        if len(nums) == 0:
            return []
        el = nums[0]
        n = len(outer)
        for i in range(n):
            internal = outer[i] + [el]
            outer.append(internal)
        temp = nums[1:]

        self.createsubSet(outer,temp)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        outer = [[]]

        self.createsubSet(outer,nums)
       
        
        return outer
        

        
            

        