class UnionFind:

    def __init__(self,n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
        

    def find(self,x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False  # already connected
        if self.rank[rootX] < self.rank[rootY]:
            self.par[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.par[rootY] = rootX
        else:
            self.par[rootY] = rootX
            self.rank[rootX] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        
        n = len(accounts)
        unionFind = UnionFind(n)
        accountMap = {}

        for i in range(n):
            for email in accounts[i][1:]:
                
                if email not in accountMap:
                    accountMap[email] = i
                else:
                    unionFind.union(i,accountMap[email])
                

        emailGroup = defaultdict(list)
        for e,i in accountMap.items():
            leader = unionFind.find(i)
            emailGroup[leader].append(e)
        
        res = []

        for i,emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        
        return res

                
               
            
        

            
            
           

        

            
        