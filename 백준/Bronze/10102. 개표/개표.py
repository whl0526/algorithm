v = int(input())
arr = list(input())

a, b = 0, 0 
for i in range(v):
    if arr[i] == 'A':
        a += 1
    else: 
        b += 1
        
if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')