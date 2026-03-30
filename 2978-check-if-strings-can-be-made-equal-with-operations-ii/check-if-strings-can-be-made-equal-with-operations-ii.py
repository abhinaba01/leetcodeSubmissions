from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        

        if len(s1) != len(s2):
            return False
        

        freq1 = Counter(s1)
        freq2 = Counter(s2)

        if freq1 != freq2:
            return False

        n = len(s1)

        even1 = []
        even2 = []

        odd1 = []
        odd2 = []
        

        for i in range(n):
            if i % 2 == 0:
                even1.append(s1[i])
                even2.append(s2[i])
            else:
                odd1.append(s1[i])
                odd2.append(s2[i])
       
        if sorted(even1) == sorted(even2) and sorted(odd1) == sorted(odd2):
            return True
        return False
                


        
