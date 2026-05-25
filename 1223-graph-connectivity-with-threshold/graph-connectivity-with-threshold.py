class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:

        class DSU:

            def __init__(self,n):
                self.parent = list(range(n + 1))
                self.size = [1] * (n + 1)

            
            def find(self,x):
                
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])

                
                return self.parent[x]

            

            def union(self,x,y):

                px = self.find(x)
                py = self.find(y)

                if px == py:
                    return False

                if self.size[px] < self.size[py]:
                    px,py = py,px
                

                self.parent[py] = px
                self.size[px] += self.size[py]

                return True

        dsu = DSU(n)

        for i in range(threshold + 1,n + 1):

            for j in range(2 * i,n + 1,i):
                
                dsu.union(i,j)


        res = []

        for u , v in queries:

            if dsu.find(u) == dsu.find(v):
                res.append(True)
            else:
                res.append(False)

        return res

