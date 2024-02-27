import sys
input = sys.stdin.readline
mod=1000000009
MAX = 100001
d = [[0]*4 for _ in range(MAX)]
d[1]=[0,1,0,0] 
d[2]=[0,0,1,0]
d[3]=[0,1,1,1]
for i in range(4,MAX):
    d[i][1] = (d[i-1][2]+d[i-1][3])%mod
    d[i][2] = (d[i-2][1]+d[i-2][3])%mod
    d[i][3] = (d[i-3][1]+d[i-3][2])%mod
 
t = int(input())
for _ in range(t):
    n = int(input())
    print((d[n][1]+d[n][2]+d[n][3])%mod)