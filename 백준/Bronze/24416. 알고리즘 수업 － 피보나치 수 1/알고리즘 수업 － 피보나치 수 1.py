import sys

input = sys.stdin.readline


def fib(n):
    return n - 2 
    
def fibonacci(n):
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input())
print(fibonacci(n), fib(n))
        
    
    
    
    