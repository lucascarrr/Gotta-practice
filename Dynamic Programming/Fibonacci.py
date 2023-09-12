# Recursive Fibonacci
import sys

def fibonacci (n):
    fib = [0] * n
    fib[0] = 1
    fib[1] = 1

    for i in range (2, n):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n-1]

print(f"The {sys.argv[1]}th fibonacci number is {fibonacci(int(sys.argv[1]))}")

