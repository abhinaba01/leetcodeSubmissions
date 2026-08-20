class Solution:
    def countBits(self, n: int) -> List[int]:


        def countOnes(i):

            cnt = 0

            while i != 0:

                if i & 1:
                    cnt += 1

                i >>= 1

            
            return cnt

        arr = [0] * (n + 1)
        
        for i in range(n + 1):
            arr[i] = countOnes(i)


        return arr