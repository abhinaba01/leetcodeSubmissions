class Solution:
    def partition(self, s: str) -> List[List[str]]:

        l = len(s)
        ans = []

        def isPalindrome(s1:str):
            return s1 == s1[::-1]

        def dfs(i,path):
            if i == l:

                for part in path:
                    if not isPalindrome(part):
                        return False
                
                ans.append(path[:])
                return 
            
            for j in range(i,l):
                part = s[i:j+1]
                path.append(part)
                dfs(j+1,path)
                path.pop()
        
        dfs(0,[])
        return ans

        

        
        


        