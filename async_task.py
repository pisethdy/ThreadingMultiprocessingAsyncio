import aiofiles
import asyncio

async def write_to_file(filename, data):
    """Asynchronously write data to a file."""
    async with aiofiles.open(filename, 'w') as f:
        await f.write(data)

async def write_primes_async(prime_numbers):
    """Asynchronously write prime numbers to a maximum of 5 files."""
    tasks = []
    num_files = 5
    total_primes = len(prime_numbers)

    # Calculate the number of primes per file
    chunk_size = (total_primes + num_files - 1) // num_files  # Ceiling division

    # Split prime numbers into up to 5 files
    for i in range(num_files):
        start_index = i * chunk_size
        end_index = min(start_index + chunk_size, total_primes)  # Ensure we don't go out of bounds
        # Slice the prime numbers for this file
        primes_chunk = prime_numbers[start_index:end_index]

        # Only write if there are primes to write
        if primes_chunk:
            filename = f'prime_numbers_{i + 1}.txt'  # Change file naming to start from 1
            task = write_to_file(filename, '\n'.join(map(str, primes_chunk)))  # Join and prepare the string
            tasks.append(task)

    # Run all the asynchronous tasks concurrently
    await asyncio.gather(*tasks)

# import importlib
# import aiofiles
# import async_task
# import asyncio

# importlib.reload(async_task)

# async def write_to_file(filename, data):
#     """Asynchronously write data to a file."""
#     async with aiofiles.open(filename, 'w') as f:
#         await f.write(data)

# async def write_primes_async(prime_numbers):
#     """Asynchronously write prime numbers to a maximum of 5 files."""
#     tasks = []
#     num_files = 5
#     total_primes = len(prime_numbers)

#     # Calculate the number of primes per file
#     chunk_size = (total_primes + num_files - 1) // num_files  # Ceiling division

#     # Split prime numbers into up to 5 files
#     for i in range(num_files):
#         start_index = i * chunk_size
#         end_index = min(start_index + chunk_size, total_primes)  # Ensure we don't go out of bounds
#         # Slice the prime numbers for this file
#         primes_chunk = prime_numbers[start_index:end_index]

#         # Only write if there are primes to write
#         if primes_chunk:
#             filename = f'prime_numbers_{i + 1}.txt'  # Change file naming to start from 1
#             task = write_to_file(filename, '\n'.join(map(str, primes_chunk)))  # Join and prepare the string
#             tasks.append(task)

#     # Run all the asynchronous tasks concurrently
#     await asyncio.gather(*tasks)