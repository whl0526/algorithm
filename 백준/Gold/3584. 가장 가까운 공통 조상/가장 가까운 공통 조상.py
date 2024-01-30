import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    parent = [0] * (n + 1)
    
    #각 노드 부모 노드 저장하기
    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a
        
    #구하고 싶은 두 노드 저장하기
    a, b = map(int, input().split())
    node_a = [a]
    node_b = [b]
    
    # 두 노드의 부모 노드들을 저장한다
    while parent[a]:
        node_a.append(parent[a])
        a = parent[a]
        
    while parent[b]:
        node_b.append(parent[b])
        b = parent[b]
        
    node_a_depth = len(node_a) - 1
    node_b_depth = len(node_b) -1
        
    #공통 조상 찾기
    while node_a[node_a_depth] == node_b[node_b_depth]:
        node_a_depth -= 1
        node_b_depth -= 1
        
    print(node_a[node_a_depth + 1])        
       
    
     
    
