import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):# 1 ~ 5 # 2, #3
    for j in range(i): # 1 # 1, #1,2 ,#
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))            