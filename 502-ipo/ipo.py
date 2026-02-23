class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        

        # n = len(profits)
        # ratio = [None] * n

        # for i in range(n):
        #     if capital[i] != 0:
        #         ratio[i] = (profits[i] / capital[i]) , i
        #     else:
        #         print(i)
        #         ratio[i] = math.inf , i

        # ratios = sorted(ratio,reverse = True)

        # for ratio , index in ratios:
        #     if w >= capital[index] and k > 0:
        #         w += profits[index]
        #         k -= 1

        # return w

        indices = list(range(len(profits)))

        indices.sort(key=lambda i: (-profits[i], capital[i]))

       
        
        while k > 0:
            taken = False
            i = 0
            while i < len(indices):
                index = indices[i]
                if w >= capital[index]:
                    w += profits[index]
                    indices.pop(i)
                    k -= 1
                    taken = True
                    break
                else:
                    i += 1

            if not taken:
                break

        return w




        