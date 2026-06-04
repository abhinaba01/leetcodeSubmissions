class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

    
        def distinct_or_values(arr):
            ans = set()
            prev = set()

            for x in arr:
                curr = {x}

                for y in prev:
                    curr.add(y | x)

                ans |= curr
                prev = curr

            return ans

        or_list = distinct_or_values(nums)

        diff = float("inf")
        for el in or_list:
            print(el)
            diff  = min(diff,abs(k - el))

        
        return diff
