import sys
#A,B 입력 받기
A,B =sys.stdin.readline().split()
minresult=len(A)#최댓값으로 가정
for i in range(len(B)-len(A)+1):#B의 시작점 지정
    result=0
    #A와 문자열 비교
    for j in range(len(A)):
        if A[j]!=B[i+j]:
            result+=1
        #최솟값이 앞에 구한것보다 커지면 그만두기(시간을 줄이기 위해 추가)
        if result>minresult:
            break
    #앞에서 구한 최솟값과 현재 구한 최솟값 비교
    minresult=min(minresult,result)
 
print(minresult)