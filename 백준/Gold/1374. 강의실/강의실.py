#그리디 알고리즘, 우선순위큐

#1.강의들을 시작시간에 따라 정렬
#2.각 강의에 대해, 가장 먼저 끝나는 강의실이 다음강의를 수용할 수 있는지 확인
#3.만약 수용할 수 없다면, 새로운 강의실을 할당
#4.이 과정을 모든 강의에 대해 반복

import heapq

n = int(input())
lectures = [list(map(int,input().split())) for _ in range(n)]

#강의를 시작 시간 기준으로 정렬
lectures.sort(key=lambda x : x[1])

#우선 순위 큐 초기화
rooms = []
heapq.heappush(rooms,lectures[0][2]) # 첫번째 강의의 종료 시간을 힙에 삽입

#강의들을 순회하면서 강의실 할당
for i in range(1,n):
    if rooms[0] <= lectures[i][1]:
        heapq.heappop(rooms) #현재 강의실에서 수용가능하면, 그 강의실에서 진행
    heapq.heappush(rooms, lectures[i][2]) # 새로운 강의 종료 시간을 힙에 삽입
    
print(len(rooms))
