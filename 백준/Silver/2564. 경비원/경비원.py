import sys
input=sys.stdin.readline

#북쪽 왼쪽 모서리를 0으로 잡고 펼쳤을 때 0으로부터 얼마나 떨어졌는 지 위치를 계산해주는 함수
def cal_dist(loc, distance) :
    if loc==1 : #북쪽
        return distance
    elif loc==4 : #동쪽
        return w+distance
    elif loc==2 : #남쪽
        return w+h+w-distance
    elif loc==3 : #서쪽
        return w+h+w+h-distance


#블록의 가로길이 세로길이 입력받기
w, h = map(int,input().split())

#상점의 개수 입력받기
num=int(input())

#상점의 위치를 저장할 리스트 만들어 놓기
locations=[0]*(num+1)

dist=[]
#각 상점의 위치와 동근이의 위치 입력받기
for i in range(num+1) :
    loc, distance=map(int, input().split())
    dist.append(cal_dist(loc, distance))

#동근이의 0에서 부터 떨어진 위치를 저장
dong_dist=dist[-1]


answer=0
for i in range(num):
    #0에서 떨어진 각 가게의 거리와, 0에서 떨어진 동근의 위치 차이의 절댓값을 구해준다.
    cal_distance=abs(dist[i]-dong_dist)

    #전체 길이를 구해준다.
    total=2*(w+h)

    #더 작은 값을 answer에 누적시킨다.
    answer+=min(cal_distance,total-cal_distance)

print(answer)
