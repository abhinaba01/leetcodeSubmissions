class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        res = []
        path = []

        def solve(i):

            if i == n:
                res.append(path[:])

            

            for j in range(i,n):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    path.append(s[i:j+1])
                    solve(j+1)
                    path.pop()

        solve(0)
        return  res
            


            





            


        