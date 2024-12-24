import re
from collections import defaultdict

# Define the gate operations
def AND(x, y):
    return x & y

def OR(x, y):
    return x | y

def XOR(x, y):
    return x ^ y

# Main function to parse the input
def parse_input(file_path):
    initial_values = {}
    gates = []
    wire_dependencies = defaultdict(list)
    reverse_dependencies = defaultdict(list)

    # Read the input file
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            # Process direct wire assignments
            match = re.match(r"([a-z0-9]+): (\d+)", line)
            if match:
                wire = match.group(1)
                value = int(match.group(2))
                initial_values[wire] = value
            else:
                # Process gates
                match = re.match(r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)", line)
                if match:
                    input1, gate_type, input2, output = match.groups()
                    gates.append((input1, gate_type, input2, output))
                    wire_dependencies[output].append((input1, gate_type, input2))
                    reverse_dependencies[input1].append(output)
                    reverse_dependencies[input2].append(output)

    return initial_values, gates, wire_dependencies, reverse_dependencies

# Evaluate the system of gates
def evaluate_gates(initial_values, gates, wire_dependencies, reverse_dependencies):
    wire_values = initial_values.copy()
    evaluated = set(wire_values.keys())  # Initially, the wires with known values are evaluated

    # Queue to process gates whose inputs are available
    processing_queue = []

    # Initially add gates to the processing queue if both their inputs are known
    for input1, gate_type, input2, output in gates:
        if input1 in wire_values and input2 in wire_values:
            processing_queue.append((input1, gate_type, input2, output))

    # Process the queue until all gates are evaluated
    while processing_queue:
        input1, gate_type, input2, output = processing_queue.pop(0)

        # Evaluate the gate
        if output not in wire_values:
            if gate_type == 'AND':
                wire_values[output] = AND(wire_values[input1], wire_values[input2])
            elif gate_type == 'OR':
                wire_values[output] = OR(wire_values[input1], wire_values[input2])
            elif gate_type == 'XOR':
                wire_values[output] = XOR(wire_values[input1], wire_values[input2])

            evaluated.add(output)

            # Once we evaluate the wire, we can process other gates that depend on it
            for dependent_gate in reverse_dependencies[output]:
                dep_input1, dep_gate_type, dep_input2 = wire_dependencies[dependent_gate][0]
                if dep_input1 in wire_values and dep_input2 in wire_values:
                    processing_queue.append((dep_input1, dep_gate_type, dep_input2, dependent_gate))

    return wire_values

# Get the binary number formed from wires starting with 'z'
def get_password(wire_values):
    z_values = []
    for wire, value in wire_values.items():
        if wire.startswith('z'):
            z_values.append(str(value))
    return ''.join(z_values)

# Main function
def main(file_path):
    # Parse the input file
    initial_values, gates, wire_dependencies, reverse_dependencies = parse_input(file_path)

    # Evaluate the gates and propagate values to all wires
    wire_values = evaluate_gates(initial_values, gates, wire_dependencies, reverse_dependencies)

    # Get the binary number from wires starting with 'z'
    binary_number = get_password(wire_values)

    # Convert the binary number to decimal
    decimal_number = int(binary_number, 2)

    return decimal_number

# Example usage
input_file_path = '/Users/tanumoykolay/Documents/AdventOfCode/day24.txt'  # Replace with your actual file path
result = main(input_file_path)
print(result)
