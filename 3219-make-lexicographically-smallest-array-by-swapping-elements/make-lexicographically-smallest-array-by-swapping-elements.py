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

        pos = defaultdict(list) 

        for i , num in enumerate(nums):
            pos[num].append(i)

        nums.sort()

        

        l , r = 0 , 1

        arr = []
        while r < n:
            if abs(nums[r] - nums[r - 1]) > limit:
                arr.append(nums[l:r])
                l = r

            r += 1

        arr.append(nums[l:r])


        for num in arr:

            indices = []

            for el in num:
                indices.append(pos[el].pop())

            indices.sort()

            for idx , el in zip(indices,num):
                nums[idx] = el


        
        return nums
      
            


                



