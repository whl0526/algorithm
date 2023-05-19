from collections import deque

N, M = map(int, input().split())
positions = list(map(int, input().split()))

queue = deque(range(1, N+1))
count = 0

for pos in positions:
    idx = queue.index(pos)  # 뽑아내려는 원소의 현재 위치 인덱스

    if idx <= len(queue) // 2:  # 현재 위치가 큐의 앞쪽에 가까운 경우
        while queue[0] != pos:
            queue.append(queue.popleft())
            count += 1
    else:  # 현재 위치가 큐의 뒷쪽에 가까운 경우
        while queue[0] != pos:
            queue.appendleft(queue.pop())
            count += 1

    queue.popleft()  # 원소 뽑아내기
    N -= 1  # 큐의 크기 갱신

print(count)
