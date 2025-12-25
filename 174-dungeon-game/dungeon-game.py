class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        row = len(dungeon)
        col = len(dungeon[0])

        @cache
        def dfs(r,c):

            if r == row - 1 and c == col - 1:
                needed = dungeon[r][c]
                return max(1, 1 - needed)

            if r >= row or c >= col:
                return float("inf")

            down = dfs(r+1,c)
            right = dfs(r,c+1)

            future_health = min(down,right)
           

            current_health = future_health - dungeon[r][c]
            return max(1,current_health)

        return dfs(0,0)



            