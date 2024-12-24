def execute_program(program, registers):
    # Registers A, B, and C
    A, B, C = registers
    ip = 0  # Instruction pointer
    output = []  # List to collect outputs

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:  # adv
            # A // (2 ** operand) and store in A
            A = A // (2 ** operand)
        elif opcode == 1:  # bxl
            # XOR B with operand and store in B
            B = B ^ operand
        elif opcode == 2:  # bst
            # Store operand % 8 in B
            B = operand % 8
        elif opcode == 3:  # jnz
            # Jump if A != 0
            if A != 0:
                ip = operand  # Jump directly to the operand address
                continue  # Skip the increment of ip, since we've jumped
        elif opcode == 4:  # bxc
            # XOR B with C and store in B (ignore operand)
            B = B ^ C
        elif opcode == 5:  # out
            # Output operand % 8
            output.append(operand % 8)
        elif opcode == 6:  # bdv
            # A // (2 ** operand) and store in B
            B = A // (2 ** operand)
        elif opcode == 7:  # cdv
            # A // (2 ** operand) and store in C
            C = A // (2 ** operand)

        # Move to the next instruction (unless jump occurred)
        ip += 2

    return output

def run_program(program, initial_values):
    # Run the program with given initial values for registers A, B, C
    return execute_program(program, initial_values)

# Example Input (registers A=729, B=0, C=0, program: 0,1,5,4,3,0)
program = [0, 1, 5, 4, 3, 0]
initial_values = (729, 0, 0)

# Run the program and get the output
output = run_program(program, initial_values)

# Print the output as a comma-separated string
print(",".join(map(str, output)))
