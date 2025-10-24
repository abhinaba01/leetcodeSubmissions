from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def is_balanced(x):
            freq = Counter(str(x))

            for key,value in freq.items():
                if int(key) != value or key == 0:
                    return False
            return True

        num = n + 1
        while True:
            
            if is_balanced(num):
                return num
            
            num += 1
            


        



        

            
            


