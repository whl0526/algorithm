import sys
input = sys.stdin.readline

_ = int(input())
n = list(map(int, input().split()))
_ = int(input())
m = list(map(int, input().split()))

new_list = {}
for i in n:
    if i in new_list:
        new_list[i] += 1
    else:
        new_list[i] = 1

for i in m:
    if i in new_list:
        print(new_list[i], end=' ')
    else:
        print(0, end=' ')
