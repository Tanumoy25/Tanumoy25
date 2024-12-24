def simulate_guard_path(grid, start_pos, start_dir, new_obstacle=None):
    # Directions mapping: up, right, down, left
    directions = {
        '^': (-1, 0),  # Move up
        '>': (0, 1),   # Move right
        'v': (1, 0),   # Move down
        '<': (0, -1)   # Move left
    }

    # Get grid dimensions
    rows = len(grid)
    cols = len(grid[0])

    # If a new obstruction is added, update the grid
    if new_obstacle:
        x, y = new_obstacle
        grid = [list(row) for row in grid]  # Convert grid to mutable list of lists
        grid[x][y] = '#'  # Add new obstruction
        grid = [''.join(row) for row in grid]  # Convert back to list of strings

    # Start the simulation with the given starting position and direction
    dir_idx = {'^': 0, '>': 1, 'v': 2, '<': 3}[start_dir]

    # Tracking visited positions
    visited_positions = set()
    current_pos = start_pos
    visited_positions.add(current_pos)

    while True:
        x, y = current_pos
        dx, dy = directions[start_dir]
        new_x, new_y = x + dx, y + dy

        # Check if the guard goes out of bounds (left the grid)
        if not (0 <= new_x < rows and 0 <= new_y < cols):
            return False  # Guard left the grid

        # Check if there's an obstacle at the new position
        if grid[new_x][new_y] == '#':
            # Turn right (clockwise 90 degrees)
            dir_idx = (dir_idx + 1) % 4
            start_dir = ['^', '>', 'v', '<'][dir_idx]
        else:
            current_pos = (new_x, new_y)
            if current_pos in visited_positions:
                return True  # The guard is stuck in a loop
            visited_positions.add(current_pos)

    return False  # Guard exits grid without looping

def find_possible_obstruction_positions(grid):
    # Find the starting position and direction of the guard
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in ['^', '>', 'v', '<']:
                start_pos = (i, j)
                start_dir = grid[i][j]
                return start_pos, start_dir

    return None, None  # This should never happen if input is valid

def main():
    # Read the input grid from a file
    filename = "/Users/tanumoykolay/Documents/AdventOfCode/day6.txt"  # Replace with the actual file name
    with open(filename, "r") as file:
        grid = [line.strip() for line in file.readlines()]

    start_pos, start_dir = find_possible_obstruction_positions(grid)

    # Count valid positions where a new obstruction can cause the guard to get stuck
    valid_positions_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':  # Only consider empty spaces for placing a new obstruction
                if simulate_guard_path(grid, start_pos, start_dir, new_obstacle=(i, j)):
                    valid_positions_count += 1

    print(valid_positions_count)

if __name__ == "__main__":
    main()
