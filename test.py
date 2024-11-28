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

    if number == 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0 and number != i:
            return False

    return True

def primes_in_range(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("Invalid input. a and b must be positive integers")

    if a > b:
        a, b = b, a  # Swap the values of a and b

    primes = []
    for num in range(a, b + 1):
        if is_prime(num):
            primes.append(num)

    return primes

def rotate_array(arr, n):
        if not isinstance(arr, list) or not isinstance(n, int):
            raise ValueError("Invalid input. arr must be a list and n must be an integer")

        if len(arr) == 0:
            return arr

        if n < 0:
            n = abs(n) % len(arr)  # Normalize n to be within the length of the array
            return arr[n:] + arr[:n]
        else:
            n = n % len(arr)  # Normalize n to be within the length of the array
            return arr[-n:] + arr[:-n]
        
def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if len(text) % 3 != 0:
        last_string = text[-(len(text) % 3):]
        text = text[:-(len(text) % 3)]
        return [text[i:i+3] for i in range(0, len(text), 3)] + [last_string]
    else:
        return [text[i:i+3] for i in range(0, len(text), 3)]

def class_and_break_time(start_class, end_class):
    if not isinstance(start_class, int) or not isinstance(end_class, int) or start_class < 0 or end_class < 0:
        raise ValueError("Invalid input. start_class and end_class must be non-negative integers")

    if start_class > end_class or start_class > 12 or end_class > 12:
        raise ValueError("Invalid input. start_class and end_class must be between 0 and 12")

    class_duration = 45
    break_durations = [0, 5, 10, 20, 10, 10, 5, 5, 10, 10, 5, 5]

    total_class_time = (end_class - start_class + 1) * class_duration
    total_break_time = sum(break_durations[start_class:end_class])

    return total_class_time, total_break_time



