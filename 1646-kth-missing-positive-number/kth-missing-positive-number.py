class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        
        high = arr[-1] + k
        cnt = 0

        for i in range(1,high+1):

            
            if i not in arr:
                cnt += 1
                if cnt == k:
                    return i
        
            
            

      
        