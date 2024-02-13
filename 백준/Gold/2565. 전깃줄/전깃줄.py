import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * n
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    
arr.sort()

for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            
max_lis = max(dp)
print(n - max_lis)
