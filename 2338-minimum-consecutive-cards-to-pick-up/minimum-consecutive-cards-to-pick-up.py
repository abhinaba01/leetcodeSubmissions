class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:


        index = defaultdict(list)

        n = len(cards)

        ans = math.inf

        for i in range(n):
            index[cards[i]].append(i)

     

        

        for c in index:
            for i in range(1,len(index[c])):
               
                ans = min(ans , index[c][i] - index[c][i-1] + 1)

        return ans if ans != math.inf else -1

        
