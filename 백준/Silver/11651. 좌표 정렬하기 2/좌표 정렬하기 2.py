# 점의 개수 N 입력 받기
N = int(input())

# N개의 점을 입력 받아 리스트에 저장
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# 점을 정렬하여 출력
points.sort(key=lambda point: (point[1], point[0]))

# 정렬된 점 출력
for point in points:
    print(point[0], point[1])