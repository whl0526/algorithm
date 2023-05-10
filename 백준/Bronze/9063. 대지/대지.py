N = int(input())  # 점의 개수 입력
points = []  # 옥구슬의 위치를 저장할 리스트

# 점의 좌표를 입력받아 points 리스트에 저장
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# 가장 왼쪽, 오른쪽, 위쪽, 아래쪽에 위치한 점 찾기
left = min(points, key=lambda p: p[0])
right = max(points, key=lambda p: p[0])
top = max(points, key=lambda p: p[1])
bottom = min(points, key=lambda p: p[1])

# 가로 길이와 세로 길이 계산
width = right[0] - left[0]
height = top[1] - bottom[1]

# 직사각형의 넓이 출력
area = width * height
print(area)