class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)
        res = []
      

        def solve(i,path,count):

            if count > 4:
                return 

            if i == n and count == 4:
                path = path[:-1]
                res.append(path)

            for j in range(i,min(i+3,n)):
                temp = s[i:j+1]
                if int(temp) < 256 and len(temp) <= 3:
                    if len(temp) > 1 and temp[0] == "0":
                        continue
                
                    path += (s[i:j+1] + ".")
                    solve(j+1,path,count + 1)
                    path = path[:-(len(temp) + 1)]

        solve(0,"",0)
        return  res
            


            





            


        

      