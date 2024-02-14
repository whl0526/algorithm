import sys

input = sys.stdin.readline

def fibonacci(n):
    zero = [1, 0, 1]
    one = [0, 1, 1]
    if n >= 3:
        for i in range(2, n):
            zero.append(zero[i - 1] + zero[i])
            one.append(one[i - 1] + one[i])
    print(f"{zero[n]} {one[n]}")
    
t = int(input())    
for _ in range(t):
    n = int(input())
    fibonacci(n)
    
    