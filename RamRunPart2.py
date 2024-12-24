from collections import deque

# Constants for grid size (71x71 grid for the full problem)
GRID_SIZE = 71

def bfs(grid, start, goal):
    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS setup
    queue = deque([start])  # Start with the top-left corner
    visited = set()
    visited.add(start)

    while queue:
        x, y = queue.popleft()

        # If we reached the goal, return True
        if (x, y) == goal:
            return True

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:  # Ensure within bounds
                if (nx, ny) not in visited and grid[nx][ny] == '.':
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return False  # No path found

def simulate_falling_bytes(byte_positions):
    # Initialize a grid of safe locations ('.')
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Mark the starting point and the goal as safe initially
    grid[0][0] = '.'
    grid[GRID_SIZE-1][GRID_SIZE-1] = '.'

    # Simulate bytes falling and marking the corrupted locations
    for idx, (x, y) in enumerate(byte_positions):
        grid[x][y] = '#'
        # After each byte falls, check if a path is still possible
        if not bfs(grid, (0, 0), (GRID_SIZE-1, GRID_SIZE-1)):
            return (x, y)  # Return the first byte that blocks the path

    return None  # No byte blocks the path

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

    # Simulate the falling bytes and find the first one that blocks the path
    return simulate_falling_bytes(byte_positions)

# Example usage
file_path = '/Users/tanumoykolay/Documents/AdventOfCode/day18.txt'  # Replace with the actual path to your input file
result = solve(file_path)
print(f"{result[0]},{result[1]}")  # Print the coordinates of the first blocking byte
