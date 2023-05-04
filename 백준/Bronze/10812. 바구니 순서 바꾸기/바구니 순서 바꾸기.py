import sys

# 바구니의 범위가
# begin , end
# 기준이 되는 바구니를
# mid

# 1 2 3 4 5 6 7 8 9 10
# 4 5 6 1 2 3 7 8 9 10 ==> 1 6 4
# 4 5 8 9 6 1 2 3 7 10 ==> 3 9 8
# 4 6 1 2 3 7 10 5 8 9 ==> 2 10 5
# 1 4 6 2 3 7 10 5 8 9 ==> 1 3 3
# 1 4 6 2 3 7 10 5 8 9 ==> 2 6 2


N,M = list(map(int, sys.stdin.readline().split()))
A = [i for i in range(1,N+1)]
for p in range(M):
    i,j,k = list(map(int, sys.stdin.readline().split()))
    A[i-1:j] = A[k-1:j] + A[i-1:k-1]

print(*A)