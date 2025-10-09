"""

417. Pacific Atlantic Water Flow


dfs up from pacific and atlantic, find intersection

"""

def solve(matrix):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def is_in_bounds(r, c):
        return 0 <= r and r < len(matrix) and 0 <= c and c < len(matrix[0])

    def search(starts):
        visited = set(starts)

        while starts:
            r, c = starts.pop()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if is_in_bounds(nr, nc) and (nr, nc) not in visited and matrix[r][c] <= matrix[nr][nc]: # next is higher
                    starts.append((nr, nc))
                    visited.add((nr, nc))
        
        return visited

    pacific = []
    for row in range(len(matrix)):
        pacific.append((row, 0))
    for col in range(len(matrix[0])):
        pacific.append((0, col))
    pacific_visited = search(pacific)

    atlantic = []
    for row in range(len(matrix)):
        atlantic.append((row, len(matrix[0]) - 1))
    for col in range(len(matrix[0])):
        atlantic.append((len(matrix) - 1, col))
    atlantic_visited = search(atlantic)

    return list(pacific_visited.intersection(atlantic_visited))


    