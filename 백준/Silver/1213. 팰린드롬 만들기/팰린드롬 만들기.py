from collections import Counter

# 문자열 입력 받기
string = input()
counter = Counter(string)

# 팰린드롬 생성을 위한 변수들
mid = ""
result = ""
odd_count = 0

# 문자 빈도 수에 따라 팰린드롬 생성
for char, freq in sorted(counter.items()):
    if freq % 2 != 0:
        mid = char
        odd_count += 1
        freq -= 1
    result += char * (freq // 2)

# 팰린드롬 가능 여부 확인
if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 출력
    print(result + mid + result[::-1])
