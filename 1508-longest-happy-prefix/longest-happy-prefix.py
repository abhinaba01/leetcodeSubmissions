class Solution:
    def longestPrefix(self, s: str) -> str:

        pre = defaultdict(str)
        suf = defaultdict(str)
        n = len(s)

        prefix = ""
        suffix = ""
        ans = ""
        for i in range(n-1):

            prefix += s[i]
            suffix = s[n-1-i] + suffix
            if prefix == suffix:
                ans = prefix
           

                
        return ans



            





       

        
        

        


        