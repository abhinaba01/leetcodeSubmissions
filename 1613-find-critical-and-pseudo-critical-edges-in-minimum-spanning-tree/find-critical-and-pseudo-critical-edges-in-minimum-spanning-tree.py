class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

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

                
                if self.size[px] <self.size[py]:
                    px,py = py, px

                
                self.parent[py] = px
                self.size[px] += self.size[py]
                self.components -= 1

                return True

       
        sorted_edges = []   
        for i , ( u , v , weight) in enumerate(edges):
            sorted_edges.append((weight,u,v,i))
            

        sorted_edges.sort()

        dsu = DSU(n)

        res = [[] for _ in range(2)]

        mst_weight = 0

        first_mst = []

        for w , u , v , index in sorted_edges:
            
            if dsu.union(u,v):
                first_mst.append(index)
                mst_weight += w
            

        k = len(first_mst)

        for i in range(k):

            j = first_mst[i]

            dsu1 = DSU(n)

            total = 0
            
            for w , u , v , index in sorted_edges:

                if index == j:
                    continue

            
                if dsu1.union(u,v):
                    total += w


            if total > mst_weight or dsu1.components > 1:
                res[0].append(j)


        for j in range(len(edges)):

            if j in res[0]:
                continue


            dsu2 = DSU(n)

            a , b , weight = edges[j]

            total = 0

            dsu2.union(a,b)
            total += weight
            
            for w , u , v , index in sorted_edges:

               
                if index == j:
                    continue
            
                if dsu2.union(u,v):
                    total += w

            
            if total == mst_weight and dsu2.components == 1:
                res[1].append(j)


        return res




        



    
                




            



            
               

            
            
                




        
        
        

        