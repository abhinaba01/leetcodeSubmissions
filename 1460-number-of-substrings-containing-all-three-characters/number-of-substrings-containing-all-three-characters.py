class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        cnt = 0
        hashMap = {"a":-1,"b":-1,"c":-1}


           
        for i in range(n):
            hashMap[s[i]] = i

            a = hashMap["a"]
            b = hashMap["b"]
            c = hashMap["c"]

            if a!= -1 and b!= -1 and  c!= -1:
                index = min(a,b,c)
                cnt += (index + 1)

        return cnt

        

        