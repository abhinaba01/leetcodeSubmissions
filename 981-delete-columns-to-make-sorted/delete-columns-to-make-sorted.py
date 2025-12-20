class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        n = len(strs)
        m = len(strs[0])

        freq = defaultdict(str)
        delete = []
        pos = 0
        ans = 0

      

        while pos < m:

            for i in range(n):
                if strs[i][pos] > strs[min(n-1,i+1)][pos]:
                    ans += 1
                    break
                  
                    
            
            pos += 1
        
        return ans
                
                


        