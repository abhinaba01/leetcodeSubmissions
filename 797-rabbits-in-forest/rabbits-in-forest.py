class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        freq =  Counter(answers)

        c = 0

        for ans , cnt  in freq.items():

            if cnt <= 1 + ans:
                c += (1 + ans)
            else:
                c += ((cnt + ans)// (1 + ans))  * (1 + ans)

        return c

        

        