import multiprocessing

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_chunk(chunk):
    """Process a chunk of numbers and check if they are prime."""
    return [num for num in chunk if is_prime(num)]

def process_file_multiprocessing(numbers, chunk_size=1000):
    """Process the file using multiprocessing to calculate primes."""
    with multiprocessing.Pool() as pool:
        chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
        results = pool.map(process_chunk, chunks)
        # Flatten the list of results
        return [prime for result in results for prime in result]
