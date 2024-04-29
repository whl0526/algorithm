# IF문 좀 대신 써줘
# 시간초과 나서 이진탐색으로 해야 한다...
# 이진탐색을 해도 시간초과가 났음. 
# menu를 만들 때 같은 능력치 값이 있으면 그것을 거르는 과정을 거쳤는데
# 이를 거르니까 시간초과가 나지 않음.
import sys

n, m = map(int, sys.stdin.readline().split(' '))

menu = []

for i in range(n):
    a, b = sys.stdin.readline().split(' ')
    menu.append([a, int(b)])

# 이진 탐색을 위해 오름차순으로 정렬
menu.sort(key=lambda x : x[1])

for j in range(m):
    temp = int(sys.stdin.readline().rstrip())
    start = 0
    end = len(menu) - 1
    while start <=  end:
        mid = (start+end) // 2
        if temp > menu[mid][1]:
            start = mid + 1
        else:
            end = mid - 1
    print(menu[start][0])