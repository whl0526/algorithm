import sys
from collections import deque

input = sys.stdin.readline

def bfs(h, w):
    queue = deque()
    queue.append([h, w])
    visited[h][w] = 1
    
    while queue:
        a, b = queue.popleft()
        
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if x < 0 or x >= H or y < 0 or y >= W:  # 범위를 벗어나는지 확인
                continue
            if grid[x][y] != "#" or visited[x][y]:  # 방문한 곳 또는 울타리가 아닌 경우 넘어감
                continue
            queue.append([x, y])
            visited[x][y] = 1

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    sheep_count = 0
    for h in range(H):
        for w in range(W):
            if visited[h][w]:
                continue
            if grid[h][w] == "#":
                bfs(h, w)
                sheep_count += 1

    print(sheep_count)
