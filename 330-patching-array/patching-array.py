class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        reach = 0
        c = 0


        for num in nums:

            if reach >= n:
                return c


            if num > reach + 1:
                while reach < n and reach + 1 < num:
                    reach = 2 * reach + 1
              
                    c += 1

            reach += num

 
        while reach  < n:
            reach = 2 * reach + 1
            c += 1

        
                


        return c



        
