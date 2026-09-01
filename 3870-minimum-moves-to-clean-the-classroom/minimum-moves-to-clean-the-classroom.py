from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])
        
        # 1. Setup variables
        sr, sc = 0, 0
        litter_coords = {}
        litter_id = 0
        
        # Find start and all litter locations
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'L':
                    litter_coords[(r, c)] = litter_id
                    litter_id += 1
                elif classroom[r][c] == 'S':
                    sr, sc = r, c
                    
        total_litter = litter_id
        target_mask = (1 << total_litter) - 1  # All bits set to 1
        
        # Queue: (moves, row, col, collected_mask, current_energy)
        dq = deque([(0, sr, sc, 0, energy)])
        
        # Visited: maps (row, col, mask) -> max_energy_recorded
        # We only revisit a state if we get there with MORE energy
        visited = {(sr, sc, 0): energy}
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while dq:
            moves, r, c, mask, eng = dq.popleft() # Use popleft() for BFS
            
            # Target reached
            if mask == target_mask:
                return moves
                
            # If out of energy, we can't move further from this cell
            if eng == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid bounds
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                    
                cell = classroom[nr][nc]
                if cell == 'X':
                    continue
                    
                n_mask = mask
                n_eng = eng - 1  # Create a new energy variable for this step
                
                # Handle cell types
                if cell == 'L':
                    # Turn on the bit for this specific piece of litter
                    n_mask |= (1 << litter_coords[(nr, nc)])
                elif cell == 'R':
                    # Refill energy
                    n_eng = energy
                    
                # If we have valid energy and this is a better path to this state
                if n_eng >= 0:
                    state = (nr, nc, n_mask)
                    if state not in visited or visited[state] < n_eng:
                        visited[state] = n_eng
                        dq.append((moves + 1, nr, nc, n_mask, n_eng))
                        
        return -1