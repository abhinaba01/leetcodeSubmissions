class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:


        quantity.sort(reverse = True)

        freq = defaultdict(int)

        for i in range(len(nums)):

            freq[nums[i]] += 1

        
        print(freq)


        counts = list(freq.values())


        def dfs(i):
            if i == len(quantity):
                return True

            for j in range(len(counts)):
                if counts[j] >= quantity[i]:
                    counts[j] -= quantity[i]

                    if dfs(i + 1):
                        return True

                    counts[j] += quantity[i]

            return False



        return dfs(0)


     


                

        
        

        