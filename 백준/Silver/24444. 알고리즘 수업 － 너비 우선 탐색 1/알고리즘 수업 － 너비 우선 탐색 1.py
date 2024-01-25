import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int,input().split())
    
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n + 1):
    graph[i].sort()
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    count = 2
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = count 
                count += 1
bfs(graph, r, visited)                

for i in visited[1::]:
    print(i)

