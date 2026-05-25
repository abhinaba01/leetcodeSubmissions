class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:


        class DSU:

            def __init__(self,n):
                self.parent = list(range(n))
                self.size = [1] * n
                self.components = n


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


        def isConnected(dsu:DSU):

            root = set()

            for i in range(1,n + 1):
                root.add(dsu.find(i))
            
            return len(root) == 1

            


        alice = DSU(n + 1)
        bob = DSU(n + 1)


        cnt = 0

        for typ, u , v in edges:
            if typ == 3:
                if alice.union(u,v):
                    bob.union(u,v)
                    cnt += 1 
               

        a , b = 0 , 0 
    
        for typ , u , v in edges:

                if typ == 1:
                    if alice.union(u,v):
                        a += 1
                if typ == 2:
                    if bob.union(u,v):
                        b += 1

        
        if not(isConnected(alice) and  isConnected(bob)):
            return -1


        return len(edges) - ( a + b + cnt)

        
                
        

            



        


            

        




            