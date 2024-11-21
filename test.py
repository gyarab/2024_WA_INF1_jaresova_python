def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n == 0:
        return 0
    
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]  # Calculate the next number in the sequence
        sequence.append(next_number)  # Add the next number to the sequence
    return sum(sequence)

def celsius_to_fahrenheit(n):
    if not isinstance(n, (int, float)):
        raise ValueError("n must be a number")
    return (n * 9/5) + 32

def fahrenheit_to_celsius(n):
    if not isinstance(n, (int, float)):
        raise ValueError("n must be a number")
    return (n - 32) * 5/9

def is_prime(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("number must be a positive integer greater than 0")
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


