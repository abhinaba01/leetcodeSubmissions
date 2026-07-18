class Solution:
    def findGCD(self, nums: List[int]) -> int:

        INF = 10 ** 18 

        MIN , MAX = INF , -INF

        for num in nums:
            MIN = min(MIN , num)
            MAX = max(MAX , num)

        return gcd(MIN , MAX)

        

        
        
        