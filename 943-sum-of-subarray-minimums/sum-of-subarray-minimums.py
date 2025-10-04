class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        MOD = 10**9 + 7

        PGE = [-1] * n
        NGE = [n] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            PGE[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            NGE[i] = stack[-1] if stack else n
            stack.append(i)
    

        sumArr = 0

        for i in range(n):

            left = i - PGE[i]
            right = NGE[i] - i

            sumArr += (left * right* arr[i]) % MOD
        
        return sumArr % MOD
        
        
