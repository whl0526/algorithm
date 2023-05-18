from collections import deque
N = int(input())
Q = deque([i for i in range(1,N+1)])

while (len(Q) > 1):
    Q.popleft()
    temp = Q.popleft()
    Q.append(temp)
    
print(Q[0])