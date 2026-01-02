class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        diff = [0] * 102
        cars = [0] * 102

        for start,end in nums:
            diff[start] += 1
            diff[end+1] -= 1
        
        cnt = 0

        for i in range(102):
            cars[i] = cars[i-1] + diff[i]
            if cars[i] >= 1:
                cnt += 1

      
        return cnt



        



        