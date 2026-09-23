class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:

        n = len(board)
        


        best_path = [[-1] * (n + 1) for _ in range(n + 1)]
        ways_path = [[-1] * (n + 1) for _ in range(n + 1)]

        MOD = 10 ** 9 + 7



        best_path[n - 1][n - 1] = 0
        ways_path[n - 1][n - 1] = 1


        for r in range(n - 1, -1 , -1):
            for c in range(n - 1 , - 1, -1):

                if r == n - 1 and c == n - 1:
                    continue

                if board[r][c] == 'X':
                    continue


                dire = [(1,0) , (0 , 1) , (1 , 1)]

                for dr , dc in dire:
                    nr = r + dr
                    nc = c + dc

                    if nr < n and nc < n:
                        best_path[r][c] = max(best_path[r][c] , best_path[nr][nc])

                if best_path[r][c] == -1:
                    continue

                path_count = 0
                for dr , dc in dire:
                    nr = r + dr
                    nc = c + dc

                    if nr < n and nc < n:

                        if best_path[nr][nc] == best_path[r][c]:
                            path_count += ways_path[nr][nc]


                ways_path[r][c] = path_count % MOD
                if board[r][c].isdigit(): 
                    best_path[r][c] += int(board[r][c])


        
        if best_path[0][0] == -1:
            return [0,0]

        return [best_path[0][0] , ways_path[0][0] % MOD]

        

                


                

        