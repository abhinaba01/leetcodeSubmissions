class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        cnt = target[0]
        n = len(target)

        for i in range(1,n):
            cnt += max(0,(target[i] - target[i-1]))

        return cnt



        
      





        