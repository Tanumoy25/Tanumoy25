def count_ways_to_display_design(towel_patterns, design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # There's one way to form an empty string: do nothing

    # Iterate over the positions in the design string
    for i in range(1, n + 1):
        for towel in towel_patterns:
            towel_len = len(towel)
            if i >= towel_len and design[i - towel_len:i] == towel:
                dp[i] += dp[i - towel_len]

    return dp[n]

def count_total_ways(towel_patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_display_design(towel_patterns, design)
    return total_ways

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

# Call the function to count total ways for all designs
result = count_total_ways(towel_patterns, designs)
print(result)  # This will print the total number of ways to form the designs
