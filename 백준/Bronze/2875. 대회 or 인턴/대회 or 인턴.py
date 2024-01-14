N, M, K = map(int, input().split())

# 최대 팀 수 계산
max_teams = min(N // 2, M)

# 남는 인원 계산
remaining = N + M - max_teams * 3

# 인턴쉽 참가 인원 처리
while K > remaining:
    K -= 3
    max_teams -= 1

print(max_teams)
