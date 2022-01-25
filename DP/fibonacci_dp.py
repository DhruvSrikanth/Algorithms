# Tine complexity is O(2^n)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Time complexity is O(n)
def fibonacci_dp(n):
    if n == 0:
        return 0
    else:
        fibonacci_sequence = [-1]*n
        fibonacci_sequence[0] = 0
        fibonacci_sequence[1] = 1
        for i in range(2,n):
            fibonacci_sequence[i] = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        return fibonacci_sequence[-1]

