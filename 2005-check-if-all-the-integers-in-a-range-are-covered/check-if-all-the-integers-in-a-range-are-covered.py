class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        diff = defaultdict(int)
        pop = [0] * 51

        for start,end in ranges:
            diff[start] += 1
            diff[end+1] -= 1

        

        for i in  range(51):
            pop[i] = pop[i-1] + diff[i]
            if i >= left and i <= right:
                if pop[i] == 0:
                    return False
        return True


        

        

        


        