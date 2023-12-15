n = int(input())

for _ in range(n):
    s, word = map(str, input().split())

    cnt = 0
    # s내에 word가 포함되어 있다면, 횟수 증가
    cnt = s.count(word)

    # word에 해당하는 단어 삭제
    replaced_s = s.replace(word, "")
    print(cnt + len(replaced_s))