# Function to check if a report is safe
def is_safe(report):
    # Check if the levels are either strictly increasing or strictly decreasing
    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])

        # Condition for the difference constraint: must be between 1 and 3
        if diff < 1 or diff > 3:
            return False

        # Check for increasing or decreasing
        if report[i] < report[i + 1]:
            decreasing = False
        elif report[i] > report[i + 1]:
            increasing = False

    # A report is safe if it's either increasing or decreasing
    return increasing or decreasing

# Function to check if a report can become safe by removing one level
def can_become_safe_by_removing_one(report):
    # Try removing each level one by one and check if the resulting report is safe
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]  # Create a new report by removing the i-th level
        if is_safe(new_report):
            return True  # If any removal results in a safe report, return True
    return False  # If no removal makes the report safe, return False

# Function to read the data from the file and count safe reports
def count_safe_reports(filename):
    safe_report_count = 0

    # Read the file and process each report
    with open(filename, 'r') as file:
        for line in file:
            # Convert the line of text into a list of integers (levels)
            report = list(map(int, line.split()))

            # Check if the report is safe either directly or by removing one level
            if is_safe(report) or can_become_safe_by_removing_one(report):
                safe_report_count += 1

    return safe_report_count

# Example usage
filename = '/Users/tanumoykolay/Documents/AdventOfCode/day2.txt'  # The name of the input file

# Calculate the number of safe reports
result = count_safe_reports(filename)

# Print the result
print(f"Number of safe reports: {result}")
