a, b = map(int,input().split())
X = ''
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while a:
    X += str(arr[a%b])
    a //= b
print (X[::-1])
    
