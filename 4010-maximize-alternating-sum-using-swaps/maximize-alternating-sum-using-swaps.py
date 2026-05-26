class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:

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
                    px,py = py , px

                
                self.size[px] += self.size[py]
                self.parent[py] = self.parent[px]

                return True


        n = len(nums)
        total = sum(+x if i % 2 == 0 else -x for i , x in enumerate(nums))
        
        dsu = DSU(n)

        if not swaps:
            return total

        for u , v in swaps:
            dsu.union(u,v)

        components = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            components[root].append(i)

        
        for component in components.values():
            
            arr = [nums[x] for x in component]
            
            arr.sort(reverse =  True)

            num_even , num_odd = 0 , 0

            for x in component:
                if x % 2 == 0:
                    num_even += 1
                    total -= nums[x]
                else:
                    total += nums[x]


            num_odd = len(component) - num_even

            sum_even = sum(arr[:num_even])
            sum_odd = sum(arr[num_even:])

            total = total + (sum_even - sum_odd)

        return total
                

            



        