def simulate_guard_path(grid):
    # Directions map: up, right, down, left (clockwise rotation)
    directions = {
        '^': (-1, 0),  # Move up
        '>': (0, 1),   # Move right
        'v': (1, 0),   # Move down
        '<': (0, -1)   # Move left
    }

    # Find initial guard position and direction
    rows = len(grid)
    cols = len(grid[0])
    guard_pos = None
    guard_dir = None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in directions:
                guard_pos = (i, j)
                guard_dir = grid[i][j]
                grid[i] = grid[i][:j] + '.' + grid[i][j+1:]  # Replace the direction with an empty space
                break
        if guard_pos:
            break

    # Simulate the guard's movement
    visited_positions = set()
    visited_positions.add(guard_pos)

    # Direction index (0 = up, 1 = right, 2 = down, 3 = left)
    dir_idx = {'^': 0, '>': 1, 'v': 2, '<': 3}[guard_dir]

    # Move the guard until she leaves the grid
    while True:
        # Get current position
        x, y = guard_pos
        dx, dy = directions[guard_dir]

        # Try to move forward
        new_x, new_y = x + dx, y + dy

        # Check if the guard is out of bounds
        if not (0 <= new_x < rows and 0 <= new_y < cols):
            break

        # If the new position is an obstacle, turn right (clockwise 90 degrees)
        if grid[new_x][new_y] == '#':
            # Turn right
            dir_idx = (dir_idx + 1) % 4
            guard_dir = ['^', '>', 'v', '<'][dir_idx]
        else:
            # Move forward
            guard_pos = (new_x, new_y)
            visited_positions.add(guard_pos)

    return len(visited_positions)


def main():
    # Read the input grid from a file
    filename = "/Users/tanumoykolay/Documents/AdventOfCode/day6.txt"  # Replace with the actual file name
    with open(filename, "r") as file:
        grid = [line.strip() for line in file.readlines()]

    # Simulate the guard's path and print the result
    result = simulate_guard_path(grid)
    print(result)


if __name__ == "__main__":
    main()
