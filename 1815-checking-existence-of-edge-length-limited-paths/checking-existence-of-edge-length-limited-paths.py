class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:


        class DSU:
            def __init__(self,n):
                self.parent = list(range(n))
                self.size = [1] * n

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

                
                self.size[px] += self.size[py]
                self.parent[py] = self.parent[px]


                return True


       

        i = 0
        new_query = []
        for p , q , limit in queries:
            new_query.append((limit,p,q,i))
            i += 1

        res = [False] * (i) 
        new_query.sort()

        dsu = DSU(n)


        edgeList.sort(key = lambda x:x[2])
        ptr = 0

        for limit , p , q , index in new_query:

            if dsu.find(p) == dsu.find(q):
                res[index] = True
                continue
        
            while ptr < len(edgeList) and  edgeList[ptr][2] < limit:
                u , v = edgeList[ptr][0] , edgeList[ptr][1]
                dsu.union(u,v)
                ptr += 1

            if dsu.find(p) == dsu.find(q):
                res[index] = True
            else:
                res[index] = False
            
        
        return res
            


        