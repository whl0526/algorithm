count = int(input())

for index in range(1,count+1):
    a,b = map(int,input().split())
    print(f'Case #{index}: {a+b}')
    