class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        s = "123456789"
        res = []

        for i in range(9):

            for j in range(i,9):
                num = s[i:j + 1]
             

                if low <= int(num) <= high:
                    res.append(int(num))

        
        res.sort()
        return res

     
       

            

        