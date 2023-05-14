import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n,m = map(int,input().split())

for i in range(n,m+1):
    if isPrime(i):
        print(i)
        
    