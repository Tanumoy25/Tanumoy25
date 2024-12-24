from collections import deque

# Directions for moving up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(map_data, start_x, start_y):
    """Perform BFS to count how many 9's are reachable from the start point."""
    rows, cols = len(map_data), len(map_data[0])
    visited = set()
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))
    reachable_9s = 0

    # Start BFS
    while queue:
        x, y = queue.popleft()

        # If we reached a 9, increment reachable 9s
        if map_data[x][y] == '9':
            reachable_9s += 1

        # Explore all 4 directions (up, down, left, right)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if int(map_data[nx][ny]) == int(map_data[x][y]) + 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return reachable_9s

def sum_of_scores(map_data):
    """Calculate the sum of the scores of all trailheads."""
    rows, cols = len(map_data), len(map_data[0])
    total_score = 0

    # Loop through the map and find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] == '0':  # Trailhead found
                score = bfs(map_data, i, j)
                total_score += score

    return total_score

def main():
    # Read input file
    with open("/Users/tanumoykolay/Documents/AdventOfCode/day10.txt") as f:
        map_data = [line.strip() for line in f.readlines()]

    # Calculate the sum of the scores
    result = sum_of_scores(map_data)
    print(f"The sum of the scores of all trailheads is: {result}")

if __name__ == "__main__":
    main()
