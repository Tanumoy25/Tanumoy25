# Function to calculate the similarity score from the file
def calculate_similarity_score(filename):
    left_list = []
    right_list = []

    # Read the file and split the pairs into left and right lists
    with open(filename, 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Calculate the similarity score
    similarity_score = 0
    for left in left_list:
        # Count how many times the number in the left list appears in the right list
        count = right_list.count(left)
        # Add the contribution of this number to the total similarity score
        similarity_score += left * count

    return similarity_score

# Example usage
filename = '/Users/tanumoykolay/Documents/AdventOfCode/day1.txt'  # The name of the input file

# Calculate the similarity score
result = calculate_similarity_score(filename)

# Print the result
print(f"Total similarity score: {result}")
