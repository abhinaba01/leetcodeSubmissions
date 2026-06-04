class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:


        ans = set()
        prev = set()

        for x in nums:
            curr = {x}

            for y in prev:
                curr.add(y|x)

            
            ans |= curr
            prev = curr

        
        diff = float("inf")
        for el in ans:
            diff = min(diff,abs(k - el))

        
        return diff
            
    
      