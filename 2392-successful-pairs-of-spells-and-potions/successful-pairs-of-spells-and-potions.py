class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        n = len(spells)
        m = len(potions)
        ans = [0] * n

        potions.sort()

        def successPotion(i):

            low = 0
            high = m - 1

            while low <= high:

                mid = (low + high) // 2
                
                if spells[i] * potions[mid] >= success:
                    high = mid - 1
                else:
                    low = mid + 1
               
            
            return low
            
            


   
        

        for i in range(n):
            count = 0

           
            ans[i] = m - successPotion(i)
            
        
        return ans
            

        