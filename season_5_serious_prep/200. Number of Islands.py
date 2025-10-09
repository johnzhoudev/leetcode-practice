"""

200. Number of Islands

number of islands

just dfs with visited array

Tactic: just dfs, use grid as visited!

"""

def solve(grid):
    state = [] # r, c to visit
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_invalid_cell(r, c):
        return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0"
    
    def clear_island(r, c):
        # Now clear the island
        state = [(r, c)]
        grid[r][c] = "0" # Mark visited
        while state:
            r, c = state.pop() # CAREFUL don't mangle names
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if not is_invalid_cell(nr, nc):
                    state.append((nr, nc))
                    grid[nr][nc] = "0"
    
    # Use grid as visited, just mark as 0
    num_islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "0":
                continue
            num_islands += 1
            clear_island(r, c)
    
    return num_islands

def solve(grid):
    state = [] # r, c to visit
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_invalid_cell(r, c):
        return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0"
    
    # Use grid as visited, just mark as 0
    num_islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "0":
                continue
            num_islands += 1

            # Now clear the island
            state.append((r, c))
            grid[r][c] = "0"
            while state:
                new_r, new_c = state.pop() # CAREFUL don't mangle names
                for dr, dc in directions:
                    nr = new_r + dr
                    nc = new_c + dc
                    if not is_invalid_cell(nr, nc):
                        state.append((nr, nc))
                        grid[nr][nc] = "0"
    
    return num_islands

print(solve([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

