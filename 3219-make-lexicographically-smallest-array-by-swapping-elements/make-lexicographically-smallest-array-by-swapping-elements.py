class DSU:

    def __init__(self,n):
      
        self.parent = list(range(n))
        self.size = [1] * n

    
    def find(self,x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        
        return self.parent[x]


    def union(self , a , b):

        pa , pb = self.find(a) , self.find(b)

        if pa == pb:
            return False

        if self.size[pa] < self.size[pb]:
            pa , pb = pb , pa


        self.size[pa] += self.size[pb]
        self.parent[pb] = pa

        return True

        
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)
        dsu = DSU(n)

        arr = sorted([(num, i) for i, num in enumerate(nums)])

      
        for i in range(1, n):
            if arr[i][0] - arr[i - 1][0] <= limit:
              
                dsu.union(arr[i][1], arr[i - 1][1])

       
        groups = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            groups[root].append(i)

        ans = [0] * n
        
       
        for root, indices in groups.items():
            vals = sorted([nums[i] for i in indices])
          
            for idx, val in zip(indices, vals):
                ans[idx] = val

        return ans
