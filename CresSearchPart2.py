# Define the function to search for 'XMAS' or 'SAMX' in all directions
def search_xmas_in_grid(grid, word="XMAS", reverse_word="SAMX"):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    # Directions for searching (horizontal, vertical, and diagonal)
    directions = [
        (0, 1),   # Right (horizontal)
        (0, -1),  # Left (horizontal)
        (1, 0),   # Down (vertical)
        (-1, 0),  # Up (vertical)
        (1, 1),   # Down-Right (diagonal)
        (-1, -1), # Up-Left (diagonal)
        (1, -1),  # Down-Left (diagonal)
        (-1, 1),  # Up-Right (diagonal)
    ]

    # Function to check if a word can be found starting at (r, c) in a given direction
    def check_direction(r, c, dr, dc, word):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    # Traverse the grid and check for 'XMAS' or 'SAMX' in each direction
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc, word):
                    count += 1
                if check_direction(r, c, dr, dc, reverse_word):
                    count += 1

    return count

file_path = '/Users/tanumoykolay/Documents/AdventOfCode/day4.txt'
with open(file_path, 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Count occurrences of the word 'XMAS' or 'SAMX'
count_xmas = search_xmas_in_grid(grid)

# Print the result
print(f"The word 'XMAS' appears {count_xmas} times.")
