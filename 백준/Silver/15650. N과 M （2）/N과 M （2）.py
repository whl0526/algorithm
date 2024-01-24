import sys
input = sys.stdin.readline

N, M = list(map(int,input().split()))

s = []

def backtracking(start):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, N+ 1):
        if i not in s:
            s.append(i)
            backtracking(i+1)
            s.pop()

backtracking(1)            
