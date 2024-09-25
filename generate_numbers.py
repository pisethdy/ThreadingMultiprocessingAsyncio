import random
import os

def generate_numbers_file(filename, count=10000):
    """Generate a file with large random numbers."""
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(f"{random.randint(10**5, 10**7)}\n")
    print("File generated successfully:", filename)

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    generate_numbers_file("numbers.txt")

