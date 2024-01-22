import sys

#n, n-1, n-2, n-3, n-4, n-5, 시작

input = sys.stdin.readline

n = int(input())

stairs = [0] * 301
for index in range(1, n + 1):
    stairs[index] = int(input())
    
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

#점화식 계산
for index in range(4, n + 1):#n-1 밟는 경우, n-2 밟는 경우
    dp[index] = max(stairs[index] + stairs[index-1] + dp[index-3], stairs[index] + dp[index-2])

print(dp[n])
