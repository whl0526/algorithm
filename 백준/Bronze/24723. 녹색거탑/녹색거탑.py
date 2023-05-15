N = int(input())

# dp[i]: i층짜리 녹색거탑을 내려오는 경우의 수
dp = [0] * (N + 1)

# 초기값 설정
dp[0] = 1  # 녹색거탑의 높이가 0인 경우의 수는 1

# dp[i]를 구하기 위해 이전 층의 경우의 수를 활용
for i in range(1, N + 1):
    dp[i] = dp[i - 1] * 2

print(dp[N])
