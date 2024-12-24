def can_display_design(towel_patterns, design):
    # Create a DP table to check if we can form the design
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can always be formed

    # Iterate over the design's length
    for i in range(1, n + 1):
        for towel in towel_patterns:
            towel_len = len(towel)
            if i >= towel_len and dp[i - towel_len] and design[i - towel_len:i] == towel:
                dp[i] = True
                break

    # The last position in dp tells if we can form the entire design
    return dp[n]

def count_possible_designs(towel_patterns, designs):
    possible_count = 0
    for design in designs:
        if can_display_design(towel_patterns, design):
            possible_count += 1
    return possible_count

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Separate the towel patterns and the designs
    towel_patterns = lines[0].strip().split(', ')  # The first line has the towel patterns
    designs = [line.strip() for line in lines[2:] if line.strip()]  # Skip blank line and read designs

    return towel_patterns, designs

# Example usage
file_path = '/Users/tanumoykolay/Documents/AdventOfCode/day19.txt'  # Replace with the path to your input file
towel_patterns, designs = read_input_from_file(file_path)

# Call the function to count possible designs
result = count_possible_designs(towel_patterns, designs)
print(result)  # This will print the number of designs that are possible
