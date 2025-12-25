class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        r = len(pizza)
        c = len(pizza[0])

        freq_row = defaultdict(list)
        freq_col = defaultdict(list)

        MOD = 10 ** 9 + 7


        for i in range(r):
            for j in range(c):
                if pizza[i][j] == 'A':
                    freq_row[i].append(j)
                    freq_col[j].append(i)
        
        def find(arr,n):
            for num in arr:
                if num >= n:
                    return num
            return -1
        
        @cache
        def count(sr,sc,k):

            start_r = -1
            start_c = -1

            ans = 0

            for i in range(sr,r):
                if find(freq_row[i],sc) != -1:
                    start_r = i
                    break
                
            

            if k == 0:
                if start_r == -1:
                    return 0
                else:
                    return 1
                


            if sr == r or sc == c:
                return 0

            
            for j in range(sc,c):
                if find(freq_col[j],sr) != -1:
                    start_c = j
                    break
               
            if start_r == -1 or start_c == -1:
                return 0
            
            for i in range(start_r,r):
                ans = (ans + count(i+1,sc,k-1)) % MOD

            for j in range(start_c,c):
                ans = (ans + count(sr,j+1,k-1)) % MOD
          
            
            return ans
        
        return count(0,0,k-1)