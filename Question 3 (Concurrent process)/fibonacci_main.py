import threading
from time import perf_counter_ns
from fibonacci import fibonacci

# Store Fibonacci results
results = {}

# Function executed by each thread
def calculate_fibonacci(n):
    results[n] = fibonacci(n)

# Perform Fibonacci calculations using multithreading
def run_multithreading():
    global results
    results = {}

    # Create three separate threads
    thread1 = threading.Thread(target=calculate_fibonacci, args=(35,))
    thread2 = threading.Thread(target=calculate_fibonacci, args=(38,))
    thread3 = threading.Thread(target=calculate_fibonacci, args=(40,))

    # Start timing before the first thread starts
    start_time = perf_counter_ns()

    # Start all three threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    # End timing after the last thread finishes
    end_time = perf_counter_ns()

    # Calculate total elapsed time
    elapsed_time = end_time - start_time

    return elapsed_time

# Test multithreading for 10 rounds
def test_multithreading():
    total_time = 0

    print("\n=== Fibonacci Computation (With Multithreading) ===")

    for round_number in range(1, 11):
        elapsed_time = run_multithreading()

        total_time += elapsed_time

        print(
            f"Round {round_number}: "
            f"Fib(35)={results[35]}, "
            f"Fib(38)={results[38]}, "
            f"Fib(40)={results[40]} "
            f"| T = {elapsed_time:,} ns"
        )

    average_time = total_time / 10

    print(f"\nAverage T (With Multithreading): {average_time:,.0f} ns")

# Perform Fibonacci calculations without multithreading
def run_without_multithreading():
    start_time = perf_counter_ns()

    fib35 = fibonacci(35)
    fib38 = fibonacci(38)
    fib40 = fibonacci(40)

    end_time = perf_counter_ns()

    elapsed_time = end_time - start_time

    return fib35, fib38, fib40, elapsed_time

# Test without multithreading for 10 rounds
def test_without_multithreading():
    total_time = 0

    print("\n=== Fibonacci Computation (Without Multithreading) ===")

    for round_number in range(1, 11):
        fib35, fib38, fib40, elapsed_time = run_without_multithreading()

        total_time += elapsed_time

        print(
            f"Round {round_number}: "
            f"Fib(35)={fib35}, "
            f"Fib(38)={fib38}, "
            f"Fib(40)={fib40} "
            f"| T = {elapsed_time:,} ns"
        )

    average_time = total_time / 10

    print(f"\nAverage T (Without Multithreading): {average_time:,.0f} ns")

if __name__ == "__main__":
    test_multithreading()
    test_without_multithreading()