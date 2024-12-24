from itertools import combinations

# Function to parse the input from a file and build the graph
def build_graph_from_file(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        connections = file.readlines()
        for connection in connections:
            comp1, comp2 = connection.strip().split('-')
            if comp1 not in graph:
                graph[comp1] = set()
            if comp2 not in graph:
                graph[comp2] = set()
            graph[comp1].add(comp2)
            graph[comp2].add(comp1)
    return graph

# Function to find all sets of 3 interconnected computers
def find_triads(graph):
    triads = []
    # Iterate over all combinations of 3 computers
    for comp1, comp2, comp3 in combinations(graph.keys(), 3):
        # Check if all three computers are interconnected
        if (comp2 in graph[comp1] and comp3 in graph[comp1] and
                comp1 in graph[comp2] and comp3 in graph[comp2] and
                comp1 in graph[comp3] and comp2 in graph[comp3]):
            triads.append((comp1, comp2, comp3))
    return triads

# Function to filter triads where at least one computer starts with 't'
def filter_triads_with_t(triads):
    return [triad for triad in triads if any(comp.startswith('t') for comp in triad)]

# Main function
def main(file_path):
    graph = build_graph_from_file(file_path)
    triads = find_triads(graph)
    filtered_triads = filter_triads_with_t(triads)
    return len(filtered_triads)

# Path to the input file
input_file_path = '/Users/tanumoykolay/Documents/AdventOfCode/day23.txt'  # Replace with your actual file path

# Calculate and print the result
result = main(input_file_path)
print(result)
