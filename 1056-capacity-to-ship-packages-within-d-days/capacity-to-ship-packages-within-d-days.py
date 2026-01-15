class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low , high = max(weights) , sum(weights)

        def canShip(cap):

            totw = 0
            ans = 0

            for w in weights:
                
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