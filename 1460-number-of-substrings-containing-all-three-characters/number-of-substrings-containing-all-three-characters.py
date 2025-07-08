class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        cnt = 0
        hashMap = {"a":-1,"b":-1,"c":-1}


           
        for i in range(n):
            hashMap[s[i]] = i

            if hashMap["a"] != -1 and hashMap["b"] != -1 and hashMap["c"] != -1:
                index = min(hashMap["a"],hashMap["b"],hashMap["c"])
                cnt += (index + 1)

        return cnt

        

        