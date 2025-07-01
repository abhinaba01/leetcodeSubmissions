class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
       
        n = len(nums)
        path = []
        mylist =[]

        def dfs(i):
            
            sortedPath = sorted(path)
            ans.append(sortedPath)
            if i == n:
                return
            else:
                for j in range(i,n):
                    path.append(nums[j])
                   
                    dfs(j+1) 
                    path.pop() 

        dfs(0)

        for a in ans:
           
            if a not in mylist:
                mylist.append(a)
                
        return mylist
        
       
