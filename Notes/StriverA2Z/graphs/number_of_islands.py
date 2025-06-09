from queue import Queue

def traverse(n, m, grid, visited_matrix, point):
    q = Queue()
    q.put_nowait(point)

    while not q.empty():
        cur = q.get_nowait()
        row, col = cur
        visited_matrix[row][col] = 1

        for a in range(-1, 2):
            for b in range(-1, 2):
                mod_row = row + a
                mod_col = col + b
                if mod_row >= 0 and mod_row < n and mod_col >= 0 and mod_col < m and grid[mod_row][mod_col] == 1 and visited_matrix[mod_row][mod_col] != 1:
                    q.put_nowait((mod_row, mod_col))

    return

def number_of_islands(grid):
    n = len(grid)
    m = len(grid[0])

    visited_matrix = [[0 for _ in range(m)] for _ in range(n)]

    island_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and visited_matrix[i][j] != 1:
                traverse(n, m, grid, visited_matrix, (i, j))
                island_count += 1

    print(visited_matrix)
    
    return island_count


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid_matrix = []
    for i in range(n):
        row = list(map(lambda x: 1 if x.upper()=="L" else 0,  input().split()))
        grid_matrix.append(row)
    
    print(number_of_islands(grid_matrix))

