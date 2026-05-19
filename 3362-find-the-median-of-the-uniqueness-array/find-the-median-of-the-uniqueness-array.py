class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:


        n = len(nums)

        total = n * ( n + 1) // 2


        def f(k):

            l = 0

            freq = defaultdict(int)

            cnt , unique = 0 , 0

            for r in range(n):

                if freq[nums[r]] == 0:
                    unique += 1
                
                freq[nums[r]] += 1

                while unique > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        unique -= 1
                    l += 1

                
                cnt += (r - l + 1)

            
            return cnt >= ((total  + 1)// 2)



                
        low , high = 1 , n 
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2
            if f(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        






        