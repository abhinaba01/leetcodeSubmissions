class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = sum(piles)
        total = sum(piles)

        def time(k):
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile/k)
            
            return cnt
                

        while low <= high:
            mid = (low + high) // 2
            if time(mid) > h:
                low = mid + 1
               
            else:
                high = mid - 1
        return low 

        