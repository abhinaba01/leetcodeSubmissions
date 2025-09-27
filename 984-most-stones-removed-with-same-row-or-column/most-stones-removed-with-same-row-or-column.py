class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = {}

    def add(self, x):
        if x not in self.par:
            self.par[x] = x
            self.rank[x] = 0

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.add(x)
        self.add(y)
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.par[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.par[rootY] = rootX
        else:
            self.par[rootY] = rootX
            self.rank[rootX] += 1
        return True

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        
        rowConnect = {}
        columnConnect = {}

        unionFind = UnionFind()

     

        for x,y in stones:
            unionFind.add((x, y))
            if x not in rowConnect:
                rowConnect[x] = []
            rowConnect[x].append((x,y))
            if y not in columnConnect:
                columnConnect[y] = []
            columnConnect[y].append((x,y))
        
        
        for k,v in rowConnect.items():
            for stone in v[1:]:
                unionFind.union(v[0], stone)
        
        for k,v in columnConnect.items():
            for stone in v[1:]:
                unionFind.union(v[0], stone)
        
        roots = set()
        for x,y in stones:
            root = unionFind.find((x,y))
            roots.add(root)
            
        
        return len(stones) - len(roots)
            




        


        


        