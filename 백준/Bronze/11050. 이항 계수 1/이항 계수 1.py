def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    return 1

n, k = map(int, input().split())

result = factorial(n) // (factorial(k) * factorial(n-k))
print(result)
