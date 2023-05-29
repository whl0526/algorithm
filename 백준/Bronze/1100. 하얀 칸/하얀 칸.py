chess = []
cnt = 0
for _ in range(8):
    chess.append(input())
for i in range(8):
    for j in range(8):
        if i % 2 == 1 and j%2 == 1 and chess[i][j] == "F":
            cnt += 1
        if i % 2 == 0 and j%2 == 0 and chess[i][j] == "F": 
            cnt += 1
print(cnt)            