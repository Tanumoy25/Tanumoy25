from collections import deque

# Constants for grid size (71x71 grid for the full problem)
GRID_SIZE = 71

def bfs(grid, start, goal):
    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS setup
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        # If we reached the goal, return the number of steps
        if (x, y) == goal:
            return steps

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:  # Ensure within bounds
                if (nx, ny) not in visited and grid[nx][ny] == '.':
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

    return -1  # No path found

def simulate_falling_bytes(byte_positions):
    # Initialize a grid of safe locations ('.')
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Mark the starting point and the goal as safe initially
    grid[0][0] = '.'
    grid[GRID_SIZE-1][GRID_SIZE-1] = '.'

    # Simulate bytes falling and marking the corrupted locations
    for idx, (x, y) in enumerate(byte_positions):
        if idx >= 1024:  # Stop after the first 1024 bytes
            break
        grid[x][y] = '#'

    return grid

def read_input(file_path):
    # Read byte positions from a file
    byte_positions = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                x, y = map(int, line.split(','))
                byte_positions.append((x, y))
    return byte_positions

def solve(file_path):
    # Read the input file to get byte positions
    byte_positions = read_input(file_path)

    # Simulate the first 1024 bytes falling
    grid = simulate_falling_bytes(byte_positions)

    # Perform BFS to find the shortest path from (0, 0) to (70, 70)
    start = (0, 0)
    goal = (GRID_SIZE - 1, GRID_SIZE - 1)
    return bfs(grid, start, goal)

# Example usage
file_path = '/Users/tanumoykolay/Documents/AdventOfCode/day18.txt'  # Replace with the actual path to your input file
result = solve(file_path)
print(f"Minimum steps to reach the exit: {result}")
