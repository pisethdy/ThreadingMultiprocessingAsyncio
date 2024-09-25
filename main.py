import threading_task
import multiprocessing_task
import async_task
import asyncio
import generate_numbers

def read_numbers_file(filename):
    """Read numbers from file."""
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f]

if __name__ == "__main__":
    # Generate the numbers file before reading
    print("Generating numbers.txt file...")
    generate_numbers.generate_numbers_file("numbers.txt")  # Call to generate the file

    # Part 1: Multiprocessing - Prime number calculation
    print("Reading numbers from file...")
    numbers = read_numbers_file('numbers.txt')
    
    print("Processing numbers with multiprocessing...")
    prime_numbers = multiprocessing_task.process_file_multiprocessing(numbers)

    # Part 2: Threading - Simulate file downloads
    file_urls = ["file1.txt", "file2.txt", "file3.txt"]
    print("Simulating file downloads with threading...")
    threading_task.download_files_with_threads(file_urls)
    
    # Part 3: Async IO - Write prime numbers asynchronously
    print("Writing prime numbers to files asynchronously...")
    asyncio.run(async_task.write_primes_async(prime_numbers))

    print("All tasks completed successfully!")
