class Solution:
    def sumOfMultiples(self, n: int) -> int:

        div = [3 , 5 , 7 ]
        
        nums = set()

        for d in div:
            
            for x in range(d , n + 1, d):

                nums.add(x)



        return sum(nums)



        
        

                

      