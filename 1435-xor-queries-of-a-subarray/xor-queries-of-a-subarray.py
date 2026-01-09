class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        prefix = defaultdict(int)
        prefix[-1] = 0
        n = len(arr)
        res = []
        ans = 0

        xor = 0
        for i in range(n):
            xor ^= arr[i]
            prefix[i] = xor

        for start , end in queries:
            ans = prefix[start-1] ^ prefix[end]
            res.append(ans)
        
        return res
        

        




     

        
        