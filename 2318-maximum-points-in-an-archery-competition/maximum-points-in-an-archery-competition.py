class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:

        best_score = 0
        best_mask = 0

        for mask in range(1 << 12):

            arrows = 0
            score = 0

            for i in range(12):

                if mask & (1 << i):
                    arrows += aliceArrows[i] + 1
                    score += i

            if arrows <= numArrows and score > best_score:
                best_score = score
                best_mask = mask

        res = [0]*12
        arrows_used = 0

        for i in range(12):
            if best_mask & (1 << i):
                res[i] = aliceArrows[i] + 1
                arrows_used += res[i]

        res[0] += numArrows - arrows_used

        return res