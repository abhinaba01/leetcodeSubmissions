class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        diff = [0] * 101
        n = len(logs)
        pop = [0] * 101

        for i in range(n):
            birth,death = logs[i]
            diff[birth-1950] += 1
            diff[death - 1950] -= 1

      

        prefixSum = 0
        maxPop = -math.inf
        for i in range(101):
            prefixSum += diff[i]
            pop[i] = prefixSum
            maxPop = max(pop[i],maxPop)

        
        return pop.index(maxPop) + 1950
        
        


        