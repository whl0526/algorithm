a,b = map(int,input().split())

m = int(input())

arr = list(map(int,input().split()))
arr.reverse() # 첫째자리부터 계산하기 위해서 뒤집었다.

ten = 0		#각 자릿수를 10진수로 바꾸고 변수에 더해서 저장한다
for i in range(m):
    ten += arr[i]*(a**i) #**은 거듭제곱 표현이다

result = []   #10진수의 진법을 변환하고 저장될 배열이다.
while ten//b:	#몫이 0이 될때까지 반복해서 나눈다.
    result.append(ten%b) #나머지를 배열에 추가한다.
    ten = ten//b
result.append(ten) #마지막 몫을 배열에 추가한다.

result.reverse() #첫째자리가 맨뒤에 있어야하므로 뒤집는다
print(' '.join(map(str,result)))