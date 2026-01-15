class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:


        low , high = max(nums) , sum(nums)
        
        if len(nums) <k:
            return -1
        
        def maxPages(limit):
            cnt = 0
            pages = 0
            for el in nums:
                if pages + el > limit:
                    cnt += 1
                    pages = 0
                
                pages += el
                    
          
            
            
            return cnt + 1
                    
                    
                
                
        
        while low <= high:
            mid = low + (high - low)// 2
            
            if maxPages(mid) > k:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
            
                
            
        





     
        