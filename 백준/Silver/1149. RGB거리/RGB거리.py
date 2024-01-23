#빨, 초 ,파  

# 1번 2번 색이 같지 않다
# N번집 N-1이랑 색이 같지 않다
# 2 <= i <= N-1 i-1, i+1는 색이 같지 않다

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * n

for i in range(n):
    dp[i] = list(map(int,input().split()))#dp[0][0] == 26 dp[0][1] == 40...
    
for i in range(1,n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]
    
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))    
