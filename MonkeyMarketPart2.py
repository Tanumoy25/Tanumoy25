def generate_next_secret(secret):
    """
    This function simulates the evolution of the secret number according to the rules:
    1. Multiply by 64 and XOR with the secret number.
    2. Prune the number (modulo 16777216).
    3. Divide by 32, XOR again, and prune.
    4. Multiply by 2048, XOR again, and prune.
    """
    secret = (secret * 64) ^ secret
    secret %= 16777216  # prune
    secret = (secret // 32) ^ secret
    secret %= 16777216  # prune
    secret = (secret * 2048) ^ secret
    secret %= 16777216  # prune
    return secret

def simulate_secret_numbers(initial_secret, steps=2000):
    """
    This function simulates the next `steps` secret numbers for a given initial secret number.
    The result is a list of prices (last digits of the secret numbers).
    """
    secret = initial_secret
    prices = []
    for _ in range(steps):
        secret = generate_next_secret(secret)
        prices.append(secret % 10)  # Store the last digit as the price
    return prices

def find_best_sequence(prices):
    """
    This function finds the sequence of four consecutive price changes
    that maximizes the sum of the prices where the monkey would sell.
    """
    # Calculate the price changes
    price_changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

    max_bananas = 0
    best_sequence = None

    # We need to check all possible sequences of 4 price changes
    for i in range(len(price_changes) - 3):  # Stop 3 steps before the end
        # Extract the 4 consecutive changes starting from index i
        sequence = tuple(price_changes[i:i + 4])

        # Now look for the first occurrence of this sequence in the prices
        for j in range(i + 4, len(price_changes)):
            # If we find a matching sequence, the monkey will sell at the price at the end of the sequence
            if tuple(price_changes[j-3:j+1]) == sequence:
                max_bananas += prices[j]  # Add the price at the end of the sequence where the monkey sells
                break

    return max_bananas

def main(input_file):
    """
    The main function that reads the initial secret numbers from the input file, simulates
    the price changes for each buyer, and calculates the best possible sequence of price
    changes that maximizes the total bananas.
    """
    with open(input_file, 'r') as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    total_bananas = 0

    # For each buyer, simulate the price changes and find the best sequence
    for secret in initial_secrets:
        prices = simulate_secret_numbers(secret)
        bananas = find_best_sequence(prices)
        total_bananas += bananas

    print(f"Total Bananas: {total_bananas}")

if __name__ == "__main__":
    input_file = '/Users/tanumoykolay/Documents/AdventOfCode/day22.txt'  # Replace with actual input file path
    main(input_file)
