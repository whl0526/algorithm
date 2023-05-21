from collections import deque

def josephus(n,k):
    circle = deque(range(1,n+1))
    result = [] #요세푸스 순열을 저장할 리스트
    
    while circle:
        circle.rotate(-(k-1))
        result.append(circle.popleft())
        
    return result
n,k = map(int,input().split())
print("<"+", ".join(map(str,josephus(n,k)))+">")