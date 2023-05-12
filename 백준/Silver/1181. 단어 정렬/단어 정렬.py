# 단어의 개수 N 입력 받기
N = int(input())

# N개의 단어를 입력 받아 리스트에 저장
words = []
for _ in range(N):
    word = input()
    words.append(word)

# 중복 제거를 위해 set으로 변환 후 다시 리스트로 변환
unique_words = list(set(words))

# 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬
unique_words.sort(key=lambda x: (len(x), x))

# 정렬된 단어 출력
for word in unique_words:
    print(word)