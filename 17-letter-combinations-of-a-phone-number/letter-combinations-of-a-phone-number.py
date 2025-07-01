class Solution:

    phoneMap = {
        "2":'abc',
        "3":'def',
        "4":'ghi',
        "5":'jkl',
        "6":'mno',
        "7":'pqrs',
        "8":'tuv',
        "9":'wxyz',
        
    }
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)
        path = ""
        ans = []


        phoneMap = {
        "2":'abc',
        "3":'def',
        "4":'ghi',
        "5":'jkl',
        "6":'mno',
        "7":'pqrs',
        "8":'tuv',
        "9":'wxyz',
        
    }

        def dfs (i,path):
           
            if i == n:
                if path:
                    ans.append(path)
                return
            else:
                letters = phoneMap[digits[i]]
                for letter in letters:
                    path = path + letter
                    dfs(i+1,path)
                    path = path[:-1]

        dfs(0,"")
        return ans


            



       

       
                
            
        


            

            