import sys
input = sys.stdin.readline

_ = int(input())
n = list(map(int, input().split()))
_ = int(input())
m = list(map(int, input().split()))

count_dict = {}

# n 리스트의 요소를 카운트하여 딕셔너리에 저장
for num in n:
    count_dict[num] = count_dict.get(num, 0) + 1

# m 리스트의 각 요소에 대해 count_dict에서 값을 찾아 출력
print(' '.join(str(count_dict.get(num, 0)) for num in m))
