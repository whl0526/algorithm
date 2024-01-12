def dfs(start, current, visited, graph):
    if visited[current]:
        if current == start:
            return True # 순환 구조 발견
        return False # 순환 구조 아님
    visited[current] = True
    return dfs(start,graph[current],visited,graph)

    
n = int(input())
graph = [0] + [int(input()) for _ in range(n)]
selected = []

for i in range(1, n+1):
    visited = [False] * (n + 1)
    if dfs(i,i,visited,graph):
        selected.append(i)
    
print(len(selected))    
for num in selected:
    print(num)
