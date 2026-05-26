class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

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
                    px , py = py , px

                
                self.size[px] += self.size[py]
                self.parent[py] = self.parent[px]

                return True
            

        n = len(s)

        dsu = DSU(n)

        for a , b in pairs:
            dsu.union(a,b)
        
        components = defaultdict(list)
        
        for i in range(n):
            root = dsu.find(i)
            components[root].append(i)

        arr = list(s)
        
        for component in components.values():
            s1 = []
            component.sort()
            for pos in component:
                s1.append(s[pos])
            s1.sort()
            for i in range(len(component)):
                arr[component[i]] = s1[i]
                   


        return "".join(arr)

            





        




      

        