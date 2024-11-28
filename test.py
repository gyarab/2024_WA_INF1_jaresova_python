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

def vowels_and_consonants(text):
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    vowels = "aeiouáéíóúůý"
    consonants = "bcčdďfghjklmnňpqrřsštťvwxzž"

    text = text.lower()
    import string
    
    text = ''.join(c for c in text if c.isalpha() and c not in string.digits and c not in string.punctuation)

    vowel_count = sum(1 for c in text if c in vowels)
    consonant_count = sum(1 for c in text if c in consonants)

    return {"vowels": vowel_count, "consonants": consonant_count}
