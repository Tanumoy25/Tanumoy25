import itertools

def evaluate_expression(numbers, operators):
    # Start with the first number
    result = numbers[0]

    # Apply each operator in order
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]

    return result

def can_be_made_true(test_value, numbers):
    n = len(numbers)
    if n == 1:
        return numbers[0] == test_value

    # Generate all combinations of '+' and '*' for n-1 positions
    operator_combinations = itertools.product(['+', '*'], repeat=n - 1)

    for ops in operator_combinations:
        if evaluate_expression(numbers, ops) == test_value:
            return True

    return False

def calculate_total_calibration(input_data):
    total_calibration = 0

    # Process each line
    for line in input_data:
        test_value_str, numbers_str = line.split(":")
        test_value = int(test_value_str)
        numbers = list(map(int, numbers_str.split()))

        # Check if the equation can be made true
        if can_be_made_true(test_value, numbers):
            total_calibration += test_value

    return total_calibration

# Example input
file_path = '/Users/tanumoykolay/Documents/AdventOfCode/day7.txt'

with open(file_path, 'r') as file:
    input_data = [line.strip() for line in file.readlines()]


# Calculate and print the total calibration result
total_calibration = calculate_total_calibration(input_data)
print(f"Total Calibration Result: {total_calibration}")
