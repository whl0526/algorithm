import sys
#setrecursionlimit(100000)
input = sys.stdin.readline

def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    

n = int(input())#6
m = int(input())#9

parent = [i for i in range(n + 1)]
arr = []
cost = 0

for i in range(m):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))
    
arr.sort(key = lambda x : x[2])
for a, b, c in arr:
    if find_parent(a) != find_parent(b):
        union(a, b)
        cost += c
        
print(cost)        
        
    
    
    
    



