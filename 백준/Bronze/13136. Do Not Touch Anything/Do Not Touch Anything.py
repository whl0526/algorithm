import sys
input = sys.stdin.readline

r,c,n = map(int,input().split())

cctv_rows = (r + n - 1) // n
cctv_cols = (c + n - 1) // n

print(cctv_rows * cctv_cols)