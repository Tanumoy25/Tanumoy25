from collections import deque

# Directions for moving up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(map_data, x, y, visited, cache):
    """Perform DFS to find distinct hiking trails from a given position (x, y)."""
    rows, cols = len(map_data), len(map_data[0])
    if (x, y) in visited:
        return 0
    visited.add((x, y))

    # If we are at height 9, this is a valid trail
    if map_data[x][y] == '9':
        return 1

    trails_count = 0
    # Explore all 4 directions (up, down, left, right)
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if int(map_data[nx][ny]) == int(map_data[x][y]) + 1:
                trails_count += dfs(map_data, nx, ny, visited, cache)

    return trails_count

def calculate_trailhead_rating(map_data, start_x, start_y):
    """Calculate the rating of a given trailhead (start_x, start_y)."""
    rows, cols = len(map_data), len(map_data[0])
    visited = set()  # to avoid revisiting cells
    return dfs(map_data, start_x, start_y, visited, {})

def sum_of_ratings(map_data):
    """Calculate the sum of the ratings of all trailheads."""
    rows, cols = len(map_data), len(map_data[0])
    total_rating = 0

    # Loop through the map and find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] == '0':  # Trailhead found
                rating = calculate_trailhead_rating(map_data, i, j)
                total_rating += rating

    return total_rating

def main():
    # Read input file
    with open("/Users/tanumoykolay/Documents/AdventOfCode/day10.txt") as f:
        map_data = [line.strip() for line in f.readlines()]

    # Calculate the sum of the ratings
    result = sum_of_ratings(map_data)
    print(f"The sum of the ratings of all trailheads is: {result}")

if __name__ == "__main__":
    main()
