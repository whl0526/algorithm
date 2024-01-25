import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []

def backtracking(startNum):
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(startNum, N + 1):
        arr.append(i)
        backtracking(i)
        arr.pop()

backtracking(1)        
        
    
