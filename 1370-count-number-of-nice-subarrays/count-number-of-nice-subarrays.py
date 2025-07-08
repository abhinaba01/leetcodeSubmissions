class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        countOdd = {}
        cnt, count = 0, 0
        countOdd[0] = 1
        for i in range(len(nums)):
            if (nums[i] % 2 != 0):
                cnt += 1
               
            
      

            rem = cnt - k
            if rem in countOdd:
                count += countOdd[rem]

            countOdd[cnt] = countOdd.get(cnt,0) + 1

       
        print(countOdd)
        return count
        