import heapq

# 입력 받기
n, m = map(int, input().split())
devices = list(map(int, input().split()))

# 충전 시간이 긴 순으로 정렬
devices.sort(reverse=True)

# 우선순위 큐 초기화
queue = [0 for _ in range(m)]

# 각 전자기기를 우선순위 큐에 삽입
for device in devices:
    # 가장 빨리 비워지는 콘센트 찾기
    shortest = heapq.heappop(queue)
    # 충전 시간 갱신하고 다시 콘센트에 추가
    heapq.heappush(queue, shortest + device)

# 가장 긴 충전 시간 출력
print(max(queue))
