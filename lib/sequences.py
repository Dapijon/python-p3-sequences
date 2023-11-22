#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    
    if length == 0:
        print(fibonacci_sequence)
        return
    
    a, b = 0, 1
    fibonacci_sequence.append(a)
    
    for _ in range(1, length):
        fibonacci_sequence.append(b)
        a, b = b, a + b
    
    print(fibonacci_sequence)

