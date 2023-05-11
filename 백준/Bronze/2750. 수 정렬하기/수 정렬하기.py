N = int(input())
M = []

for i in range(N):
    M.append(int(input()))
M = sorted(M)
print(*M)