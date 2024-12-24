def compact_disk(disk_map):
    # Parse the input disk map into a list of file sizes and free space sizes
    files = []
    free_spaces = []

    # Make sure the input length is even (alternating file and free space sizes)
    if len(disk_map) % 2 != 0:
        raise ValueError("Input string length is not valid! Should be even.")

    # Process the input string (alternating file and free space sizes)
    for i in range(0, len(disk_map), 2):
        file_size = int(disk_map[i])  # File size
        free_space_size = int(disk_map[i + 1])  # Free space size
        files.append(file_size)
        free_spaces.append(free_space_size)

    # Create a list to represent the blocks on the disk
    blocks = []
    for file_size in files:
        blocks.extend([len(blocks)] * file_size)  # Assign file IDs to the blocks
    for free_space in free_spaces:
        blocks.extend([-1] * free_space)  # Use -1 to represent free space

    # Now compact the disk by removing all free spaces and shifting files to the left
    compacted_blocks = [block for block in blocks if block != -1]

    # Calculate the checksum by multiplying each block's position with its file ID
    checksum = sum(i * block for i, block in enumerate(compacted_blocks))

    return checksum

def read_input_file(file_path):
    # Read the disk map input from a file
    with open(file_path, 'r') as f:
        return f.read().strip()  # Read and remove any surrounding whitespace/newlines

# Example usage
input_file = "/Users/tanumoykolay/Documents/AdventOfCode/day9.txt"  # Replace with your file path
disk_map = read_input_file(input_file)

try:
    checksum = compact_disk(disk_map)
    print("Checksum:", checksum)
except ValueError as e:
    print(f"Error: {e}")
