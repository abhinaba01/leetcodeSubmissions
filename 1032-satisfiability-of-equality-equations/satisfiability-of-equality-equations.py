class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        n = len(equations)

        parent = list(range(26))
        size = [0] * 26

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(a,b):

            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False
            

            if size[pa] < size[pb]:
                pa , pb = pb , pa

            
            size[pa] += size[pb]
            parent[pb] = parent[pa]

            return True
            




        for eq in equations:

            ch1 , ch2 = eq[0] , eq[3]
            x = ord(ch1) - ord('a')
            y = ord(ch2) - ord('a')

            if eq[1] == "=":
                if find(x) != find(y):
                    union(x,y)
        
        
            
        for eq in equations:

            ch1 , ch2 = eq[0] , eq[3]
            x = ord(ch1) - ord('a')
            y = ord(ch2) - ord('a')

            if eq[1] == "!":
                if find(x) == find(y):
                    return False
        
        

        return True





        
        