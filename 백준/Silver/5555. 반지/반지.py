import sys
s = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
cnt = 0
for n in range(N):
    a = sys.stdin.readline().strip()
    for i in range(10):
        a = a[1:] + a[0]
        if s in a:
            cnt += 1
            break
print(cnt)