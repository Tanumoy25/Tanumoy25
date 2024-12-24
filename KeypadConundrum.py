from collections import deque

# Define the keypad and its coordinates for easy access
KEYPAD = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

# Define movements (up, down, left, right) for the directional keypad
MOVES = {
    '^': (-1, 0),  # move up
    'v': (1, 0),   # move down
    '<': (0, -1),  # move left
    '>': (0, 1)    # move right
}

# Function to find the shortest path (using BFS) from start to end in the keypad
def bfs(start, end):
    """ Find the shortest number of moves from start to end using BFS """
    rows, cols = len(KEYPAD), len(KEYPAD[0])
    queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
    visited = set()
    visited.add(start)

    while queue:
        r, c, steps = queue.popleft()

        # If we reached the end, return the number of steps
        if (r, c) == end:
            return steps

        # Explore the neighbors (up, down, left, right)
        for dr, dc in MOVES.values():
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and KEYPAD[nr][nc] != ' ':
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))

    return -1  # In case there's no valid path (shouldn't happen)

# Function to calculate the complexity of a given code
def calculate_complexity(code):
    # Find the target code as a sequence of button presses
    target = [char for char in code]  # e.g., '029A' -> ['0', '2', '9', 'A']

    # Initialize the starting position of the arm at the 'A' button
    start_position = (3, 2)  # The 'A' is at (3, 2)
    total_steps = 0

    # We will move from 'A' to each target button, calculate the shortest path for each
    for digit in target:
        # Find the position of the digit on the keypad
        for r in range(4):
            for c in range(3):
                if KEYPAD[r][c] == digit:
                    end_position = (r, c)
                    break

        # BFS to get the shortest number of moves from current arm position to the target
        steps = bfs(start_position, end_position)
        total_steps += steps

        # Update the arm position to the newly pressed button
        start_position = end_position

    # Now, calculate the numeric part of the code
    numeric_value = int(code[:-1])  # Exclude 'A' to get the numeric part

    # Return the product of the number of button presses and the numeric value
    return total_steps * numeric_value

def main(input_file):
    # Read the input file and extract the list of codes
    with open(input_file, 'r') as file:
        codes = [line.strip() for line in file.readlines()]

    # Calculate the total complexity for all codes
    total_complexity = sum(calculate_complexity(code) for code in codes)

    # Output the total complexity
    print(total_complexity)

if __name__ == "__main__":
    input_file = '/Users/tanumoykolay/Documents/AdventOfCode/day21.txt'  # Replace this with the actual file path if necessary
    main(input_file)
