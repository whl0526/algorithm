input = __import__('sys').stdin.readline

n,d,k,c = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(k-1): 	# 구간 시작하는 포인터가 n-1일때 index를 채워주기위해 arr뒤에 k-1개만큼 추가함
    arr.append(arr[i])

s = 0 			# 구간 시작 포인터
e = k-1 		# 구간 끝 포인터
temp = 0 		# 현재 구간에서의 서로 다른 초밥의 개수
dict = {} 		# 서로 다른 초밥의 개수를 판별하기 위한 딕셔너리
maxs = 0 		# 최댓값

while s < n:
    if s == 0:
        for i in range(k):
            if arr[i] in dict:
                dict[arr[i]] += 1
            else:
                dict[arr[i]] = 1
    else:
        if dict[arr[s-1]] == 1:
            del dict[arr[s-1]]
        else:
            dict[arr[s-1]] -= 1

        if arr[e] in dict:
            dict[arr[e]] += 1
        else:
            dict[arr[e]] = 1

    if c in dict:
        temp = len(dict)
    else:
        temp = len(dict)+1

    maxs = max(maxs,temp)
    s+=1
    e+=1

print(maxs)