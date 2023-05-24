import sys
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
T = int(sys.stdin.readline())
for t in range(T):
    cnt = 0
    a = list(map(int, sys.stdin.readline().split()))
    for i in range(1, a[0]):
        for j in range(i+1, a[0]+1):
            cnt += gcd(a[i], a[j])
    print(cnt)
