def generate_next_secret(secret):
    # Step 1: Multiply by 64 and mix
    secret = (secret * 64) ^ secret
    # Step 2: Prune
    secret %= 16777216

    # Step 3: Divide by 32 (round down) and mix
    secret = (secret // 32) ^ secret
    # Step 4: Prune
    secret %= 16777216

    # Step 5: Multiply by 2048 and mix
    secret = (secret * 2048) ^ secret
    # Step 6: Prune
    secret %= 16777216

    return secret

def simulate_secret_numbers(initial_secret, steps=2000):
    secret = initial_secret
    for _ in range(steps):
        secret = generate_next_secret(secret)
    return secret

def main(input_file):
    # Read the input from the file
    with open(input_file, 'r') as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    # Calculate the sum of the 2000th secret number for each buyer
    total_sum = 0
    for secret in initial_secrets:
        total_sum += simulate_secret_numbers(secret)

    # Output the result
    print(total_sum)

if __name__ == "__main__":
    input_file = '/Users/tanumoykolay/Documents/AdventOfCode/day22.txt'  # Replace this with the actual file path if necessary
    main(input_file)
