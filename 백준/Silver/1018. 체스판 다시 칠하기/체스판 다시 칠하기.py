N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input())

min_count = float('inf')

for i in range(N-7):
    for j in range(M-7):
        # 첫 번째 칸이 W로 시작하는 경우와 B로 시작하는 경우에 대해 각각 칠해야 하는 정사각형 개수를 센다
        count_w = 0
        count_b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 체스판 모양을 확인하여 칠해야 하는 정사각형의 개수를 센다
                if (k+l) % 2 == 0:  # 흰색으로 시작해야 하는 경우
                    if board[k][l] != 'W':
                        count_w += 1
                    if board[k][l] != 'B':
                        count_b += 1
                else:  # 검은색으로 시작해야 하는 경우
                    if board[k][l] != 'B':
                        count_w += 1
                    if board[k][l] != 'W':
                        count_b += 1
        # 현재 부분에서 칠해야 하는 정사각형의 개수와 최소 개수를 비교하여 갱신한다
        min_count = min(min_count, count_w, count_b)

print(min_count)