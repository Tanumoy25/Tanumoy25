# Function to read the data from the file and calculate the total distance
def total_distance_from_file(filename):
    left_list = []
    right_list = []

    # Read the file and split the pairs into left and right lists
    with open(filename, 'r') as file:
        for line in file:
            # Split each line into two numbers and convert them to integers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the sum of absolute differences between corresponding elements
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

    return total_distance

# Example usage
filename = '/Users/tanumoykolay/Documents/AdventOfCode/day1.txt'  # The name of the input file

# Calculate the total distance
result = total_distance_from_file(filename)

# Print the result
print(f"Total distance: {result}")
