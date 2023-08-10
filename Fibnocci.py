def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Example usage
n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is:", result)
