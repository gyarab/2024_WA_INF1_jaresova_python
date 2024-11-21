def fibonacci(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number in the sequence
        sequence.append(next_number)  # Add the next number to the sequence
    return sequence

print (fibonacci(5))