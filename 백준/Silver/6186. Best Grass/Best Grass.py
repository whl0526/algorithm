import sys
input = sys.stdin.readline

R, C = list(map(int, input().split()))
grass = [list(input().strip()) for _ in range(R)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    clump = 0
    visit = [[0] * C for _ in range(R)]
    
    for r in range(R): #5
        for c in range(C): #6
            if not visit[r][c] and grass[r][c] == '#':
                visit[r][c] = 1
                clump += 1
                
                for i in range(4):
                    ar, ac = r + dx[i], c + dy[i]
                    if 0 <= ar < R and 0 <= ac < C:
                        if not visit[ar][ac]:
                            visit[ar][ac] = 1
    return clump
print(bfs())        
