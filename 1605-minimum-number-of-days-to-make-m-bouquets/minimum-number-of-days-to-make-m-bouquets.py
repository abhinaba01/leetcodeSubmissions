class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) < (m * k):
            return -1

        
        low , high = 0 , max(bloomDay)

        def check(days):

            res = []

            ans = 0
            cnt = 0
            for bloom in bloomDay:
                if bloom <= days:
                    cnt += 1
                else:

                    ans += math.floor(cnt / k)
                    cnt = 0
                    
            ans += math.floor(cnt / k)
    

            
            print(days,ans)
            return ans
                    


        while low <= high:
            mid = low + (high - low) // 2
            if check(mid) < m:
                low = mid + 1
            else:
                high = mid - 1

        return low
            


        