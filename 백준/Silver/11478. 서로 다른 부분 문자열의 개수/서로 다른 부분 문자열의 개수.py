s = input()

subStrings = set() # 서로 다른 부분 문자열 저장할 집합(set)

#모든 가능한 부분 문자열 생성
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        subStrings.add(s[i:j])

print(len(subStrings))
