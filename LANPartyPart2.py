from collections import defaultdict, deque

# Function to build the graph from input
def build_graph_from_file(file_path):
    graph = defaultdict(set)
    with open(file_path, 'r') as file:
        connections = file.readlines()
        for connection in connections:
            comp1, comp2 = connection.strip().split('-')
            graph[comp1].add(comp2)
            graph[comp2].add(comp1)
    return graph

# Function to perform DFS to find all computers in a connected component
def dfs(graph, start, visited):
    stack = [start]
    component = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            component.append(node)
            stack.extend(graph[node] - visited)
    return component

# Function to find all connected components in the graph
def find_connected_components(graph):
    visited = set()
    components = []
    for computer in graph:
        if computer not in visited:
            component = dfs(graph, computer, visited)
            components.append(component)
    return components

# Main function to solve the problem
def main(file_path):
    graph = build_graph_from_file(file_path)
    components = find_connected_components(graph)

    # Find the largest connected component
    largest_component = max(components, key=len)

    # Sort the component alphabetically and join them with commas to form the password
    password = ",".join(sorted(largest_component))
    return password

# Path to the input file
input_file_path = '/Users/tanumoykolay/Documents/AdventOfCode/day23.txt'  # Replace with your actual file path

# Calculate and print the result (password)
result = main(input_file_path)
print(result)
