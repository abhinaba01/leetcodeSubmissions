class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low , high = 1 , sum(weights)

        def canShip(cap):

            totw = 0
            ans = 0

            for w in weights:
                if w > cap:
                    return math.inf
                if totw + w > cap:
                    ans += math.ceil(totw / cap)
                    totw = 0
                totw += w

            ans += math.ceil(totw / cap)
                
                    

            return ans
                


        while low <= high:
            mid = low + (high - low ) // 2
            if canShip(mid) > days:
                low = mid + 1
            else:
                high = mid - 1
        return low