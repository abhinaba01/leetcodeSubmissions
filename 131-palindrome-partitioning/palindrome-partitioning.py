class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []

        def isPalindrome(path):
            if path == path[::-1]:
                return True
            return False
       

        n = len(s)

        def dfs(i,path):
            if i == n:

                for part in path:
                    if isPalindrome(part) == False:
                        return
                
                    
                        
                ans.append(path[:])

                return
            
            for j in range(i,n):
                part = s[i:j+1]
                path.append(part)
                dfs(j+1, path)
                path.pop()
                
                


        dfs(0,[])
        return ans

       