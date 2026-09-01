class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        rows, cols = len(classroom), len(classroom[0])
        grid = [[''] * cols for _ in range(rows)]

        dire = [(0,1) , (0,-1) , (1,0) , (-1,0)]
        INF = 10 ** 18 

        sr , sc = 0 , 0

        coord = defaultdict(int)
        index= 0

        for r in range(rows):
            for c in range(cols):

                if classroom[r][c] == 'L':
                    coord[(r,c)] = index
                    index +=1
                
                if classroom[r][c] == 'S':
                    sr , sc = r , c
                
                grid[r][c] = classroom[r][c]

        
      
        visited = {(sr, sc, 0): energy}
        target_mask = (1 << index) - 1

    
        
        dq = deque([(0 , sr,sc,energy,0)])
       

        while dq:

            moves , r , c , eng , mask = dq.popleft()

            if mask == target_mask:
                return moves

            if eng == 0:
                continue


            for dr , dc in dire:
                nr , nc = r + dr , c + dc

                if (0 <= nr < rows and 0<= nc < cols):
                    cell = grid[nr][nc]

                    if cell == 'X':
                        continue

                    n_mask = mask
                    n_eng = eng - 1

                    if cell == 'L':
                        idx = coord[(nr,nc)]
                        n_mask = mask | (1 << idx)

                    elif cell == 'R':
                        n_eng = energy
                        


                    if n_eng < 0:
                        continue

                    state = (nr , nc , n_mask)
                    
                    if state not in visited or visited[state] < n_eng:


                    
                        visited[state] = n_eng
                            
                        dq.append((moves + 1 , nr , nc , n_eng , n_mask))

                    
        
        return -1

            




                

            

            





        



                
        
       
