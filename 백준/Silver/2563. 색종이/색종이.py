arr = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())

for _ in range(N):
    x,y = list(map(int,input().split()))
    
    for row in range(x,x+10):
        for col in range(y,y+10):
            arr[row][col] = 1
result = 0

for i in arr:
    result += sum(i)
    
print(result)    