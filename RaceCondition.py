from collections import deque

# Directions for movement: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def read_input(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def bfs(grid, start, end):
    """ Perform BFS to find the shortest path from start to end """
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True

    while queue:
        r, c, dist = queue.popleft()

        # If we reached the end, return the distance
        if (r, c) == end:
            return dist

        # Explore the neighbors
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != '#':
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))

    return -1  # In case there's no path

def find_cheats(grid, start, end):
    """ Find all cheats and their time savings """
    rows, cols = len(grid), len(grid[0])
    cheats = []

    # BFS to get the shortest path without cheating
    base_time = bfs(grid, start, end)

    # Try cheating at every position and calculate the saved time
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                # Try to cheat by disabling collision for 2 picoseconds
                # Temporarily modify the grid and rerun BFS
                grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                new_time = bfs(grid, start, end)
                if new_time != -1 and new_time < base_time:
                    cheats.append(base_time - new_time)
                # Restore the original grid
                grid[r] = grid[r][:c] + '.' + grid[r][c+1:]

    return cheats

def main(filename):
    grid = read_input(filename)

    # Find the start ('S') and end ('E') positions
    start, end = None, None
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    # Find all cheats and their time savings
    cheats = find_cheats(grid, start, end)

    # Count how many cheats save at least 100 picoseconds
    count = sum(1 for cheat in cheats if cheat >= 100)

    print(count)

if __name__ == "__main__":
    filename = '/Users/tanumoykolay/Documents/AdventOfCode/day20.txt'  # Input file containing the racetrack
    main(filename)
