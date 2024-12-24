import re

def extract_and_sum_multiplications(corrupted_memory):
    # Regular expression to match mul(X, Y) where X and Y are integers
    # X and Y are 1-3 digit numbers and should be surrounded by parentheses
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Start with the mul instructions enabled
    mul_enabled = True
    total_sum = 0

    i = 0
    while i < len(corrupted_memory):
        # Check for "do()" enabling mul instructions
        if corrupted_memory[i:i+3] == "do(":
            mul_enabled = True  # Enable mul instructions
            i += 3  # Skip "do("
            while i < len(corrupted_memory) and corrupted_memory[i] != ')':
                i += 1
            i += 1  # Skip over the closing parenthesis
        # Check for "don't()" disabling mul instructions
        elif corrupted_memory[i:i+6] == "don't":
            mul_enabled = False  # Disable mul instructions
            i += 6  # Skip "don't()"
        # Check for a valid "mul(X, Y)" instruction
        elif corrupted_memory[i:i+3] == "mul":
            if mul_enabled:
                match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", corrupted_memory[i:])
                if match:
                    x = int(match.group(1))
                    y = int(match.group(2))
                    total_sum += x * y
                    i += len(match.group(0))  # Move past the mul instruction
                else:
                    i += 1  # Skip invalid mul patterns
            else:
                # Skip over the mul pattern if mul instructions are disabled
                i += 3  # Skip "mul"
                while i < len(corrupted_memory) and corrupted_memory[i] != '(':
                    i += 1
                while i < len(corrupted_memory) and corrupted_memory[i] != ')':
                    i += 1
                i += 1  # Skip over the closing parenthesis
        else:
            # Skip over non-relevant characters
            i += 1

    return total_sum

def main():
    # Read the corrupted memory from a file
    filename = "/Users/tanumoykolay/Documents/AdventOfCode/day3.txt"  # You can replace this with the actual file name
    with open(filename, "r") as file:
        corrupted_memory = file.read()

    # Call the function and print the result
    result = extract_and_sum_multiplications(corrupted_memory)
    print(result)

if __name__ == "__main__":
    main()
